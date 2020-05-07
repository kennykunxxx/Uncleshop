from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('dashboard/', views.dashboard, name='dashboard'),
    ]
    
