from django.shortcuts import render
from django.http import HttpResponse
from job.models import Job, Team, Match
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .form import JobForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.utils import timezone
from django.urls import reverse_lazy

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