from django.contrib import admin
from orders.models import OrderItem, Order, UserInfo
from django import forms
from store.models import Product



    
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'view_username', 'create', 'total_price', 'paid')
    list_editable = ('paid',)
    readonly_fields = ('view_username', 'view_total_price', 'create', 'total_price', )
    list_fields = ('paid')
    exclude = ['user_info']

    def view_total_price(self, obj):
        trial = []
        for x in obj.order_orderitem.all().values():
            products = Product.objects.get(id=x['product_id'])
            trial.append(' {}'.format(products))
            trial.append('({}) '.format(x['quantity']))

        return trial
    
    def view_username(self, obj):
        return obj.user_info.user
    
    
    
admin.site.register(Order, OrderAdmin)
# Register your models here.





"""
admin.site.register(OrderItem, Order)

class CustomModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % (obj.user.username)

@admin.register(Order)
class OrdersAdmin(admin.ModelAdmin):
    inlines = [
        OrderItemInline,
        ]

class OrderAdminForm(forms.ModelForm):
    orders = CustomModelChoiceField(queryset=UserInfo.objects.all())
    class Meta:
        models = OrderItem


class OrderItemAdmin(admin.ModelAdmin):
    form = OrderAdminForm

class OrderItemInline(admin.TabularInline):
    model = OrderItem


            trial.append('Quantity: ({})'.format(x['Quantity']))
            

"""