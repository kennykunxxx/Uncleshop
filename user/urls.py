from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.log_in, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logged_out.html'), name='logout'),
    path('account_creation/', views.account_creation, name='account_creation'),
    ]