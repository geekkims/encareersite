from django.db import models

# Create your models here.
class ContactUs(models.Model):
    first_name = models.CharField(max_length=250, blank=True, null=True)
    last_name = models.CharField(max_length=250, blank=True, null=True)
    phone_number = models.CharField(max_length=250, blank=True, null=True)
    email_address = models.CharField(max_length=1024*4,blank=True, null=True)
    message = models.CharField(max_length=1024*4,blank=True, null=True)
    created_date = models.DateField(auto_now=True,blank=True, null=True)
    updated_date = models.DateField(auto_now_add=True,blank=True, null=True) 

    def __str__(self):
        return str(self.first_name)