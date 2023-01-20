from django.urls import path
from . import views

app_name ="frontend"


urlpatterns = [
  
   
    path('',views.index,name="homepage"),
     path('about-us/',views.about,name="aboutpage"),
    # path('services/',views.services,name="services"),
     path('services/<slug:slug>/', views.Services, name='service'),



]

