from django.urls import path
from . import views
from .views import JobListView, JobCreateView, JobDetailView, JobUpdateView, JobDeleteView

urlpatterns = [
    path('post/<int:pk>/', JobDetailView.as_view(), name='job_detail'), 
    path('', JobListView.as_view(), name='job_home'),
    path('post/new/', JobCreateView.as_view(), name='job_create'),
    path('post/<int:pk>/edit/', JobUpdateView.as_view(), name='job_edit'),
    path('post/<int:pk>/delete/', JobDeleteView.as_view(), name='job_delete'),
]
