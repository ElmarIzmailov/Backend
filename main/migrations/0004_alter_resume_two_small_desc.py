# Generated by Django 4.1.3 on 2023-01-28 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_about_name1_about_name2_about_name3_about_name4"),
    ]

    operations = [
        migrations.AlterField(
            model_name="resume_two",
            name="small_desc",
            field=models.CharField(max_length=200),
        ),
    ]
