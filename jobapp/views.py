from django.shortcuts import render
from website.models import Mainlogo, Service

# Create your views here.
def index(request):
    logo_obj= Mainlogo.objects.last() 
    services_obj=Service.objects.filter(is_active=True)
    

    context={

        "logo_obj":logo_obj,
        "services_obj":services_obj,

    }
    return render(request,'jobapp/jobs.html',context)