from django import forms

class JobForm(forms.Form):
    job_name = forms.CharField(label='job_name', max_length=255)