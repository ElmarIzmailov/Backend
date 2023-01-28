from django.shortcuts import render
from .models import Home, About, Resume_one, Resume_two, Resume_three, Resume_four, Resume_five, Services, Portfolio, Save, Contact

# Create your views here.

def index_views(request):
    context = {
        "Home":Home.objects.last(),
        
        "About":About.objects.last(),
        
        "Resume_one":Resume_one.objects.last(),
        
        "Resume_two":Resume_two.objects.last(),
        
        "Resume_three":Resume_three.objects.last(),
        
        "Resume_four":Resume_four.objects.last(),
        
        "Resume_five":Resume_five.objects.last(),
        
        "Services":Services.objects.last(),
        
        "Portfolio":Portfolio.objects.all(),
        }

    if request.method == 'POST':

        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        Save.objects.create(name=name, email=email, subject=subject, message=message)

    return render(request, 'index.html', context)

