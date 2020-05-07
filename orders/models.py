from django.db import models
from django.contrib.auth.models import User
from store.models import Product
from django.utils.html import format_html

# Create your models here.

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=250, blank=True)
    postal_code = models.CharField(max_length=250, blank=True)
    city = models.CharField(max_length=250, blank=True)
    
    def __str__(self):
        return 'Order {}'.format(self.user)
        
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.orders_items.all())
        

class Order(models.Model):
    paid = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=5, decimal_places=2)
    create = models.DateTimeField(auto_now_add=True)
    user_info = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='user_infos', null=True)
    

"""
may need to add is it sent
"""


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_orderitem', null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders_product')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return '{}'.format(self.product)
        
        
    def get_cost(self):
        return self.price * self.quantity



    
