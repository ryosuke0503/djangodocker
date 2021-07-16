from django.db import models
from django.urls import reverse
from django.core.validators import FileExtensionValidator
import os

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
    #home = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL)
    #home = models.ForeignKey(Team, on_delete = models.SET_NULL, null = True)
    homescore = models.IntegerField()
    awayscore = models.IntegerField()
    away = models.IntegerField()
    #away = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL)
    #away = models.ForeignKey(Team, on_delete=models.CASCADE)
    stadium = models.CharField(max_length=64)
    viewers = models.IntegerField()
    broadcasts = models.CharField(max_length=64)

    def __str__(self):
        return self.kind
    def get_absolute_url(self):
        return reverse('match_detail', args=[str(self.id)])

class FileUpload(models.Model):
    """
    ファイルのアップロード
    """
    title = models.CharField(default='CSVアフィル', max_length=50)
    upload_dir = models.FileField(upload_to='csv', validators=[FileExtensionValidator(['csv',])])
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def file_name(self):
        """
        相対パスからファイル名のみを取得するカスタムメソッド
        """
        path = os.path.basename(self.upload_dir.name)
        return path