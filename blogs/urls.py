from django.urls import path
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from . import views

app_name ="blogs"

urlpatterns = [
   path('',views.index,name="blogs"),
    path('<slug:slug>/', views.BlogDetails, name='blogs-detail'),


    
]

