from django.urls import path
from . import views
from .views import MatchListView, MatchCreateView, MatchDetailView, MatchUpdateView, MatchDeleteView

urlpatterns = [
    path('post/<int:pk>/', MatchDetailView.as_view(), name='match_detail'), 
    path('', MatchListView.as_view(), name='match_home'),
    path('post/new/', MatchCreateView.as_view(), name='match_create'),
    path('post/<int:pk>/edit/', MatchUpdateView.as_view(), name='match_edit'),
    path('post/<int:pk>/delete/', MatchDeleteView.as_view(), name='match_delete')
]
