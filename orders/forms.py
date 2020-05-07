from django import forms
from store.models import Product, QandA
from orders.models import UserInfo
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404




class QuantityForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ('product_quantity',)

    def __init__(self, id, *args, **kwargs):
        super(QuantityForm, self).__init__(*args, **kwargs)
        quantity = get_object_or_404(Product, id=id)
        quantity = quantity.product_quantity
        choice = [(i, str(i)) for i in range(1, quantity+1)]
        self.fields['product_quantity'].widget = forms.Select(choices=choice)
        
    """
    May be Change widget to typing version
    """
    
class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['user', 'first_name', 'last_name', 'email', 'address',
                  'postal_code', 'city']

    def __init__(self, *args, **kwargs):
        super(UserInfoForm, self).__init__(*args, **kwargs)
        self.fields['user'].disabled = True

