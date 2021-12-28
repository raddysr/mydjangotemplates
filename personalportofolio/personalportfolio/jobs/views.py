from django.shortcuts import render, get_object_or_404
from .models import Job
def home(req):
    jobs = Job.objects
    return render(req, 'jobs/home.html', {
        'jobs':jobs
    })

def detail(req, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(req, 'jobs/detail.html', {'job':job_detail})