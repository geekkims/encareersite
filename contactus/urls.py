from django.urls import path
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from . import views

app_name ="contact-us"

urlpatterns = [
   path('contact-us/',views.index,name="contactus"),
  


    
]

