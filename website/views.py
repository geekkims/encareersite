from django.shortcuts import render
from jobapp.models import Applicant, Job
from website.models import About, Mainlogo

# Create your views here.
def index(request):
    logo_obj= Mainlogo.objects.last() 

    context={

        "logo_obj":logo_obj

    }
    return render(request,'jobapp/index.html',context)


def about(request):
    logo_obj= Mainlogo.objects.last() 
    about_obj=About.objects.last() 
    totaljob_obj=Job.objects.count()
    activejob_obj=Job.objects.filter(is_closed=True).count()

    total_applicants=Applicant.objects.count()
    context={

        "logo_obj":logo_obj,
        "about_obj":about_obj,
        "totaljob_obj":totaljob_obj,
        "activejob_obj":activejob_obj,
        "total_applicants":total_applicants,


    }
    return render(request,'jobapp/about.html',context)