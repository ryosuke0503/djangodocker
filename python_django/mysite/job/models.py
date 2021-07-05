from django.db import models

# Create your models here.
class Job(models.Model):
    job_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')