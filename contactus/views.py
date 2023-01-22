from django.shortcuts import render
from django.contrib import  messages
from contactus.forms import ContactUsForm
from website.models import Mainlogo, Service

# Create your views here.
def index(request):
    html_template = "front-end/contact-us/index.html"
    form  = ContactUsForm()
    logo_obj= Mainlogo.objects.last() 
    services_obj=Service.objects.filter(status=True)

    context = {
        "form": form,
        "logo_obj":logo_obj,
        "services_obj":services_obj,

    }
    
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            print("Form is Valid", request.POST)
            form.save()
            messages.success(request,"Thank you for contacting us, we shall get back to you within 24 Hours")
            return render(request,html_template, context)
        else:
            messages.warning(request,"Sorry, there was a problem, kindly try later")
            return render(request,html_template, context) 
    
    return render(request,html_template, context)