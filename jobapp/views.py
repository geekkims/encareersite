from django.shortcuts import render
import jobapp
from jobapp.models import Job
from website.models import Jobphoto, Mainlogo, Service
from django.views.generic import CreateView, DetailView, ListView
from django.http import Http404, HttpResponseRedirect, JsonResponse, HttpResponseNotAllowed


# Create your views here.
def index(request):
    try:
        logo_obj = Mainlogo.objects.last()
    except:
        logo_obj = None
        
    job_obj = Job.objects.filter(is_closed=False)
    
    try:
        photo = Jobphoto.objects.last()
    except:
        photo = None
        
    try:
        services_obj = Service.objects.filter(status=True)
    except:
        services_obj = []

    context = {
        "logo_obj": logo_obj,
        "job_obj": job_obj,
        "photo": photo,
        "services_obj": services_obj,
    }
    return render(request, 'front-end/jobs/index.html', context)


def JobDetails(request, slug):
    try:
        logo_obj = Mainlogo.objects.last()
    except:
        logo_obj = None
        
    single_job = Job.objects.get(slug=slug)
    
    try:
        services_obj = Service.objects.filter(status=True)
    except:
        services_obj = []
        
    try:
        photo = Jobphoto.objects.last()
    except:
        photo = None

    context = {
        'logo_obj': logo_obj,
        'single_job': single_job,
        "services_obj": services_obj,
        "photo": photo,
    }

    return render(request, 'front-end/jobs/detail.html', context)


class JobDetailsView(DetailView):
    model = Job
    template_name = "jobs/details.html"
    context_object_name = "job"
    pk_url_kwarg = "id"

    def get_object(self, queryset=None):
        obj = super(JobDetailsView, self).get_object(queryset=queryset)
        if obj is None:
            raise Http404("Job doesn't exists")
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Move database queries here instead of class level
        try:
            context['logo_obj'] = Mainlogo.objects.last()
        except:
            context['logo_obj'] = None
            
        try:
            context['services_obj'] = Service.objects.filter(status=True)
        except:
            context['services_obj'] = []
            
        try:
            context['photo'] = Jobphoto.objects.last()
        except:
            context['photo'] = None
            
        return context

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            # raise error
            raise Http404("Job doesn't exists")
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)