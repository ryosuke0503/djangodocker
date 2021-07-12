from django.shortcuts import render, redirect
from django.http import HttpResponse
from job.models import Job, Team, Match
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .form import JobForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.utils import timezone
from django.urls import reverse_lazy
from .models import FileUpload
import io, csv

class JobListView(ListView):
  model = Job
  template_name = 'job_home.html'

class JobDetailView(DetailView):
  model = Job
  template_name = 'job_detail.html'

class JobCreateView(CreateView):
  model = Job
  template_name = 'job_new.html'
  fields = ['job_name']
  model.pub_date = timezone.datetime.now()
  success_url = reverse_lazy('job_home')
  
class JobUpdateView(UpdateView):
  model = Job
  template_name = 'job_edit.html'
  fields = ['job_name']
  model.pub_date = timezone.datetime.now()
  success_url = reverse_lazy('job_home')

class JobDeleteView(DeleteView):
  model = Job
  template_name = 'job_delete.html'
  success_url = reverse_lazy('job_home')

#------Team----------------------

class TeamListView(ListView):
  model = Team
  template_name = 'team_home.html'

class TeamDetailView(DetailView):
  model = Team
  template_name = 'team_detail.html'

class TeamCreateView(CreateView):
  model = Team
  template_name = 'team_new.html'
  fields = ['name']
  model.pub_date = timezone.datetime.now()
  success_url = reverse_lazy('team_home')
  
class TeamUpdateView(UpdateView):
  model = Team
  template_name = 'team_edit.html'
  fields = ['name']
  model.pub_date = timezone.datetime.now()
  success_url = reverse_lazy('team_home')

class TeamDeleteView(DeleteView):
  model = Team
  template_name = 'team_delete.html'
  success_url = reverse_lazy('team_home')

def TeamUpload(request):
    """
    トップページ
    """
    file_obj = FileUpload.objects.all()
    context = {
            'file_obj': file_obj,
    }
    return render(request, 'team_upload.html', context)

def TeamImport(request):
    if 'csv' in request.FILES:
        data = io.TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_content = csv.reader(data)
        #print(csv_content)
        for i in csv_content:
            Team.objects.create(name=i[0])
            print(i)
    #return render(request, 'team_home.html')
    response = redirect('team_home')
    return response

#----Match-----------------------------------------

class MatchListView(ListView):
  model = Match
  template_name = 'match_home.html'

class MatchDetailView(DetailView):
  model = Match
  template_name = 'match_detail.html'

class MatchCreateView(CreateView):
  model = Match
  template_name = 'match_new.html'
  fields = ['year', 'league', 'kind', 'date', 'time', 'home', 'homescore', 'awayscore', 'away', 'stadium', 'viewers', 'broadcasts']
  model.pub_date = timezone.datetime.now()
  success_url = reverse_lazy('match_home')
  
class MatchUpdateView(UpdateView):
  model = Match
  template_name = 'match_edit.html'
  fields = ['year', 'league', 'kind', 'date', 'time', 'home', 'homescore', 'awayscore', 'away', 'stadium', 'viewers', 'broadcasts']
  model.pub_date = timezone.datetime.now()
  success_url = reverse_lazy('match_home')

class MatchDeleteView(DeleteView):
  model = Match
  template_name = 'match_delete.html'
  success_url = reverse_lazy('match_home')

def MatchImport(request):
  if 'csv' in request.FILES:
      data = io.TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
      csv_content = csv.reader(data)
      #print(csv_content)
      for i in csv_content:
          Match.objects.create(year=i[0], league=i[1], kind=i[2], date=i[3], time=i[4],
                               home=i[5], homescore=i[6], awayscore=i[7], away=i[8],
                               stadium=i[9], viewers=i[10], broadcasts=i[11])
          print(i)
  #return render(request, 'team_home.html')
  response = redirect('match_home')
  return response