from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('cart/', views.cart_detail, name='cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove'),
    path('checkout/', views.checkout, name='checkout'),
    path('order_history/<int:order_id>/', views.order_history_detail, name='order_history_detail'),
    path('order_history/', views.order_history_list, name='order_history_list')
    ]

