from django.db import models
from ckeditor.fields import RichTextField
import uuid
import os




# Create your models here.
# This should be include on all views
class Mainlogo(models.Model):
    title=models.CharField(max_length=100)
    background_image = models.ImageField(upload_to="logo", help_text="1920x801 px image for fit background")
    

    def __str__(self):
        return self.title


class Slider(models.Model):
    title=models.CharField(max_length=100)
    slider_image = models.ImageField(upload_to="logo", help_text="1920x801 px image for fit background")
    created_at=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=True)
    
    def __str__(self):
        return self.title


class About(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="about", help_text="1920x801 px image for fit background")
    about = RichTextField()
  
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


def upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join('services', filename)


class Service(models.Model):
    title=models.CharField(max_length=300)
    slug = models.CharField(max_length=255)
    
    service_image = models.ImageField(upload_to=upload_to,help_text="1920x801 px image for fit background",null=True)

    description=RichTextField(blank=True)
    status=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)

 



