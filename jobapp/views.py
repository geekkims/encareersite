from django.shortcuts import render
import jobapp
from jobapp.models import Job
from website.models import Mainlogo, Service
from django.views.generic import CreateView, DetailView, ListView
from django.http import Http404, HttpResponseRedirect, JsonResponse, HttpResponseNotAllowed


# Create your views here.
def index(request):
    logo_obj= Mainlogo.objects.last() 
    job_obj=Job.objects.filter(is_closed=False)
    

    context={

        "logo_obj":logo_obj,
        "job_obj":job_obj,

    }
    return render(request,'jobapp/jobs.html',context)


def JobDetails(request,slug):
    logo_obj= Mainlogo.objects.last() 
    job=Job.objects.get(slug=slug)


    


    context={

        'logo_obj':logo_obj,
        'job':job,

    }



    return render(request,'jobs/details.html',context)



class JobDetailsView(DetailView):
    model = Job
    template_name = "jobs/details.html"
    context_object_name = "job"
    logo_obj= Mainlogo.objects.last() 
    pk_url_kwarg = "id"

    def get_object(self, queryset=None):
        obj = super(JobDetailsView, self).get_object(queryset=queryset)
        logo_obj= Mainlogo.objects.last() 
        if obj is None:
            raise Http404("Job doesn't exists")
        return obj

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            # raise error
            raise Http404("Job doesn't exists")
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)



