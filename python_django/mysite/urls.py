from django.urls import path,include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('job/', include('job.joburls')),
    path('team/', include('job.teamurls')),
    path('match/', include('job.matchurls')),
]