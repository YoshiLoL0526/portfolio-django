from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all-projects/', views.all_projects, name='all_projects'),
]
