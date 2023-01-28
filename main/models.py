from django.db import models

# Create your models here.

class Home(models.Model):
    '''page Home'''
    
    bio = models.CharField(max_length=150)
    desc = models.CharField(max_length=150)
    link1 = models.EmailField(verbose_name='linkedin')
    link2 = models.EmailField(verbose_name='facebook')
    link3 = models.EmailField(verbose_name='instagram')
    link4 = models.EmailField(verbose_name='telegram')
    link5 = models.EmailField(verbose_name='twitter')

    def __str__(self):
        return self.bio

class About(models.Model):
    '''page About'''

    bio = models.CharField(max_length=255)
    desc1 = models.CharField(max_length=255)
    birthday = models.CharField(max_length=20)
    age = models.IntegerField()
    website = models.CharField(max_length=30)
    phone = models.IntegerField()
    city = models.CharField(max_length=30)
    degree = models.CharField(max_length=30)
    phemailone = models.EmailField()
    freelance = models.CharField(max_length=25)
    desc2 = models.CharField(max_length=255)

    name1 = models.CharField(max_length=200)
    happyclients = models.IntegerField()

    name2 = models.CharField(max_length=200)
    projects = models.IntegerField()

    name3 = models.CharField(max_length=200)
    hours_of_support = models.IntegerField()
    
    name4 = models.CharField(max_length=200)
    awards = models.IntegerField()


    def __str__(self):
        return self.desc1


class Resume_one(models.Model):
    '''page Resume'''

    name = models.CharField(max_length=200)
    small_desc = models.CharField(max_length=35)
    desc = models.CharField(max_length=200)

    bio = models.CharField(max_length=20)
    phone = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} - {self.small_desc}"

class Resume_two(models.Model):

    name = models.CharField(max_length=200)
    small_desc = models.CharField(max_length=35)
    year = models.CharField(max_length=20)
    desc = models.CharField(max_length=200)
    text = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} - {self.small_desc}"
    
class Resume_three(models.Model):

    name = models.CharField(max_length=200)
    year = models.CharField(max_length=20)
    small_desc = models.CharField(max_length=35)
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Resume_four(models.Model):
    name = models.CharField(max_length=200)
    small_desc = models.CharField(max_length=35)
    year = models.CharField(max_length=20)
    desc = models.CharField(max_length=200)

    text_one = models.CharField(max_length=255)
    text_two = models.CharField(max_length=255)
    text_three = models.CharField(max_length=255)
    text_four = models.CharField(max_length=255)


    def __str__(self):
        return self.name

    
class Resume_five(models.Model):

    name = models.CharField(max_length=200)
    year = models.CharField(max_length=20)
    small_desc = models.CharField(max_length=35)
    desc = models.CharField(max_length=200)

    text_one = models.CharField(max_length=255)
    text_two = models.CharField(max_length=255)
    text_three = models.CharField(max_length=255)
    text_four = models.CharField(max_length=255)


    def __str__(self):
        return self.name


class Services(models.Model):
    '''page Service'''

    name1 = models.CharField(max_length=50)
    desc1 = models.CharField(max_length=200)
    
    name2 = models.CharField(max_length=50)
    desc2 = models.CharField(max_length=200)
    
    name3 = models.CharField(max_length=50)
    desc3 = models.CharField(max_length=200)
    
    name4 = models.CharField(max_length=50)
    desc4 = models.CharField(max_length=200)
    
    name5= models.CharField(max_length=50)
    desc5 = models.CharField(max_length=200)
    
    name6 = models.CharField(max_length=50)
    desc6 = models.CharField(max_length=200)

    
    def __str__(self):
        return self.name1
    

class Portfolio(models.Model):
    '''page Portfolio'''
    
    img_one = models.ImageField()

    img_two = models.ImageField()

    img_three = models.ImageField()

    img_four = models.ImageField()

    img_five = models.ImageField()

    img_six = models.ImageField()

    img_seven = models.ImageField()


class Contact(models.Model):
    '''page Contact'''

    adress = models.CharField(max_length=60)
    email = models.EmailField()


class Save(models.Model):
    '''Save models'''
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"
    


