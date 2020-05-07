from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('recipe/', views.recipe_list, name='recipe_list'),
    path('recipe/<slug:category_slug>/', views.recipe_list, name='recipe_category'),
    path('<int:id>/', views.product_detail, name='product_detail'),
    path('<slug:category_slug>/', views.product_list, name='product_category'),
    path('answers/<int:q_id>/', views.q_and_a, name='staff_answer'),
    path('', views.product_list, name='product_list'),
    
    ]