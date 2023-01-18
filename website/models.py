from django.db import models
from ckeditor.fields import RichTextField



# Create your models here.
# This should be include on all views
class Mainlogo(models.Model):
    title=models.CharField(max_length=100)
    background_image = models.ImageField(upload_to="logo", help_text="1920x801 px image for fit background")

    def __str__(self):
        return self.title


class About(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="about", help_text="1920x801 px image for fit background")
    about = RichTextField()
    # Encareer Recruitment Process
    stage_one_title=models.CharField(null=True, max_length=100)
    firstprocess = RichTextField(max_length=600)
    stage_two_title=models.CharField(null=True, max_length=100)
    secondprocess = RichTextField(max_length=600)
    stage_three_title=models.CharField(null=True, max_length=100)
    thirdprocess = RichTextField(max_length=600)
    stage_four_title=models.CharField(null=True, max_length=100)
    fourthprocess = RichTextField(max_length=600)
    # End of the recruitment Process

    def __str__(self):
        return self.title



