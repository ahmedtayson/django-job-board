from django.shortcuts import render
from . models import job

def job_list(request):
    job_list = job.objects.all()
    context = {'jobs':job_list}
    return render(request,'job/job_list.html',context)

def job_dateil(request,id):
    
    job_dateil = job.objects.get(id=id)
    context = {'job':job_dateil}
    return render(request,'job/job_detail.html',context)

# Create your views here.
