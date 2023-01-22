from django.shortcuts import render
from blogs.models import Blog, Category

from website.models import Mainlogo, Service

# Create your views here.
def index(request): 

    logo_obj= Mainlogo.objects.last() 
    services_obj=Service.objects.filter(status=True)
    blogs_obj=Blog.objects.all().order_by('-id')
    context={

        "logo_obj":logo_obj,
        "services_obj":services_obj,
        "blogs_obj":blogs_obj
 
    }
   

    return render(request, "front-end/blogs/index.html",context)


def BlogDetails(request,slug): 

    logo_obj= Mainlogo.objects.last() 
    blog_obj=Blog.objects.get(slug=slug)
    recentblogs_obj=Blog.objects.all()[0:4]
    services_obj=Service.objects.filter(status=True)
    cat_obj=Category.objects.all().order_by('-id')[0:6]

    context={

        "logo_obj":logo_obj,
        "blog_obj":blog_obj,
        "services_obj":services_obj,
        "recentblogs_obj":recentblogs_obj,
        "cat_obj":cat_obj


    }
   

    
    return render(request, "front-end/blogs/detail.html",context)