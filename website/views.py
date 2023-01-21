from django.shortcuts import render
from blogs.models import Blog
from jobapp.models import Applicant, Company, Job
from website.models import About, Mainlogo, Offer, Service

# Create your views here.
def index(request):
    logo_obj= Mainlogo.objects.last() 
    offer_obj=Offer.objects.last()
    services_obj=Service.objects.filter(status=True)
    jobscount_obj=Job.objects.count()
    jobs_obj=Job.objects.filter(is_closed=False).order_by('-id')[:3]
    company_obj=Company.objects.all()
    blog_obj=Blog.objects.all()

    context={

        "logo_obj":logo_obj,
        "services_obj":services_obj,
        "jobscount_obj":jobscount_obj,
        "jobs_obj":jobs_obj,
        "offer_obj":offer_obj,
        "company_obj":company_obj,
        "blog_obj":blog_obj,

    }
    return render(request,'jobapp/index.html',context)


def about(request):
    logo_obj= Mainlogo.objects.last() 
    about_obj=About.objects.last() 
    totaljob_obj=Job.objects.count()
    activejob_obj=Job.objects.filter(is_closed=True).count()
    services_obj=Service.objects.filter(is_active=True)
    total_applicants=Applicant.objects.count()
    context={

        "logo_obj":logo_obj,
        "about_obj":about_obj,
        "totaljob_obj":totaljob_obj,
        "activejob_obj":activejob_obj,
        "total_applicants":total_applicants,
        "services_obj":services_obj,
        


    }
    return render(request,'jobapp/about.html',context)


def Services(request,slug):
    logo_obj= Mainlogo.objects.last() 
    services_obj=Service.objects.filter(is_active=True)
    slug_obj = Service.objects.get(slug=slug)
 
    context={

        "logo_obj":logo_obj,
        "services_obj":services_obj,
        "slug_obj":slug_obj,

    }
    return render(request,'jobapp/services.html',context)