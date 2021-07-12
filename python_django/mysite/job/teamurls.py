from django.urls import path
from . import views
from .views import TeamListView, TeamCreateView, TeamDetailView, TeamUpdateView, TeamDeleteView

urlpatterns = [
    path('post/<int:pk>/', TeamDetailView.as_view(), name='team_detail'), 
    path('', TeamListView.as_view(), name='team_home'),
    path('post/new/', TeamCreateView.as_view(), name='team_create'),
    path('post/<int:pk>/edit/', TeamUpdateView.as_view(), name='team_edit'),
    path('post/<int:pk>/delete/', TeamDeleteView.as_view(), name='team_delete'),
    path('upload', views.TeamUpload, name='team_upload'),
    path('import', views.TeamImport, name='team_import'),
]
