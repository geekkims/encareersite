from django.shortcuts import render
from blogs.models import Blog
from jobapp.models import Applicant, Category, Company, Job
from website.models import About, Mainlogo, Offer, Service, Slider

# Create your views here.
def index(request):
    logo_obj= Mainlogo.objects.last() 
    offer_obj=Offer.objects.last()
    services_obj=Service.objects.filter(status=True)
    jobscount_obj=Job.objects.count()
    jobs_obj=Job.objects.filter(is_closed=False).order_by('-id')[:3]
    company_obj=Company.objects.all()
    companycount_obj=Company.objects.count()
    blog_obj=Blog.objects.all()[:3]
    cat_obj=Category.objects.all()[0:4]
    appcount_obj=Applicant.objects.count()
    slider_obj=Slider.objects.filter(status=True).last
    category_stats = {}
    for category in cat_obj:
        category_stats[category.name] = Job.objects.filter(category=category).count()

    context={

        "logo_obj":logo_obj,
        "services_obj":services_obj,
        "jobscount_obj":jobscount_obj,
        "jobs_obj":jobs_obj,
        "offer_obj":offer_obj,
        "company_obj":company_obj,
        "blog_obj":blog_obj,
        "cat_obj":cat_obj,
        "appcount_obj":appcount_obj,
        "slider_obj":slider_obj,
        "category_stats":category_stats,
        "companycount_obj":companycount_obj

    }
    return render(request,'homepage/index.html',context)


def about(request):
    logo_obj= Mainlogo.objects.last() 
    about_obj=About.objects.last() 
    companycount_obj=Company.objects.count()
    jobscount_obj=Job.objects.count()
    appcount_obj=Applicant.objects.count()

    
  
    
    context={

        "logo_obj":logo_obj,
        "about_obj":about_obj,
        "companycount_obj":companycount_obj,
        "jobscount_obj":jobscount_obj,
        "appcount_obj":appcount_obj,
       
        


    }
    return render(request,'front-end/about/index.html',context)


def Services(request):

    return render(request,'services/services.html')

def Servicedetails(request,slug):
    logo_obj= Mainlogo.objects.last() 
    services_obj=Service.objects.filter(status=True)
    slug_obj = Service.objects.get(slug=slug)
 
    context={

        "logo_obj":logo_obj,
        "services_obj":services_obj,
        "slug_obj":slug_obj,

    }
    return render(request,'front-end/services/details.html',context)