from django.urls import path
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from . import views
from .views import *


app_name ="jobapp"

urlpatterns = [
    # path('register',RegistrationView.as_view(), name="register"),
     path('jobs/',views.index,name="jobs"),
    path('job/<slug:slug>/', views.JobDetails, name='jobs-detail'),
    # path("job/<slug:slug>/", JobDetailsView.as_view(), name="jobs-detail"),


    
]

