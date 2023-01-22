from django.shortcuts import render
from blogs.models import Blog

from website.models import Mainlogo

# Create your views here.
def index(request): 
   

    
    return render(request, "front-end/blogs/index.html")


def BlogDetails(request,slug): 

    logo_obj= Mainlogo.objects.last() 
    blog_obj=Blog.objects.get(slug=slug)

    context={

        "logo_obj":logo_obj,
        "blog_obj":blog_obj,


    }
   

    
    return render(request, "front-end/blogs/detail.html",context)