from django.db import models
from django.urls import reverse

# Create your models here.
class Job(models.Model):
    job_name = models.CharField(max_length=200)

    def __str__(self):
        return self.job_name

    def get_absolute_url(self):
        return reverse('job_detail', args=[str(self.id)])

class Team(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('team_detail', args=[str(self.id)])

class Match(models.Model):
    year = models.IntegerField()
    league = models.CharField(max_length=64)
    kind = models.CharField(max_length=64)
    date = models.CharField(max_length=64)
    time = models.CharField(max_length=64)
    home = models.IntegerField()
    homescore = models.IntegerField()
    awayscore = models.IntegerField()
    away = models.IntegerField()
    stadium = models.CharField(max_length=64)
    viewers = models.IntegerField()
    broadcasts = models.CharField(max_length=64)

    def __str__(self):
        return self.kind
    def get_absolute_url(self):
        return reverse('match_detail', args=[str(self.id)])