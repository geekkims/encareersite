from django.urls import path
from . import views

app_name ="frontend"


urlpatterns = [
  
   
    path('',views.index,name="homepage"),
     path('about-us/',views.about,name="aboutpage"),
    # path('services/',views.Services,name="services"),
     path('service/<slug:slug>/', views.Servicedetails, name='service-details'),



     



]

