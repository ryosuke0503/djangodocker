from django.shortcuts import render
from django.http import HttpResponse
from job.models import Job

# Create your views here.
def hellofunction(request):
    jobData = Job.objects.get(id=1)
    message = jobData.job_name
    #message = "はろーわーるど"
    params = {
        'message': message,
    }
    return render(request, 'aaaa.html', params)
