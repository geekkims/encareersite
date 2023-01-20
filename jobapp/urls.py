from django.urls import path
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from . import views

app_name ="jobapp"

urlpatterns = [
    # path('register',RegistrationView.as_view(), name="register"),
     path('jobs/',views.index,name="jobs"),


    
]

