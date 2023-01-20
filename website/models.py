from django.db import models
from ckeditor.fields import RichTextField
import uuid




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
  
    # End of the recruitment Process

    def __str__(self):
        return self.title


class Service(models.Model):
    title=models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image=models.ImageField(upload_to="about", help_text="1920x801 px image for fit background")
    about = RichTextField()
    # Encareer Services Process Process
    stage_one_title=models.CharField(null=True, max_length=100)
    firstprocess = RichTextField(max_length=600,blank=True)
    stage_two_title=models.CharField(null=True, max_length=100)
    secondprocess = RichTextField(max_length=600,blank=True)
    stage_three_title=models.CharField(null=True, max_length=100)
    thirdprocess = RichTextField(max_length=600,blank=True)
    stage_four_title=models.CharField(null=True, max_length=100)
    fourthprocess = RichTextField(max_length=600,blank=True)
    is_active = models.BooleanField(default=False)
    # End of the recruitment Process

    def __str__(self):
        return self.title




class Offer(models.Model):
    name=models.CharField(max_length=300)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.CharField(max_length=255)
    offer_image=models.ImageField(upload_to="offers", help_text="1920x801 px image for fit background")
    description=RichTextField(blank=True)
    status=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        self.slug = str(self.uuid)
        super().save(*args, **kwargs)

 



