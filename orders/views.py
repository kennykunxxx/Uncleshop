from django.shortcuts import render, get_object_or_404, redirect
from orders.cart import Cart
from store.models import Product
from orders.forms import QuantityForm, UserInfoForm
from orders.models import Order, OrderItem, UserInfo
from django.http import HttpResponse
# Create your views here.

"""
Change Quantity in Cart
Add remove item from template
"""

def cart_detail(request):
    """get cart detail"""
    cart = Cart(request)
    context = {
        'cart': cart,
    }
    return render(request, 'orders/cart.html', context)
    
def add_to_cart(request, product_id):
    cart = Cart(request)
    product_object = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        forms = QuantityForm(product_id, request.POST)
        if forms.is_valid():
            cd = forms.cleaned_data
            cart.add(product=product_object, quantity=cd['product_quantity']
                                             )
                                             
    return redirect('orders:cart')
        
    
def remove_from_cart(request, product_id):
    """remove cart item"""
    cart = Cart(request)
    product_object = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        cart.remove(product_object)
        cart.save_session()
    return redirect('orders:cart')


    
def checkout(request):
    """checkout process"""
    cart = Cart(request)
    if request.method == 'POST':
        form = UserInfoForm(request.POST, instance=request.user.userinfo)
        if form.is_valid():
            form.save()
            order_total = cart.get_total_price()
            get_order = Order.objects.create(paid=False,
                                                 total_price=order_total)
            get_userinfo = UserInfo.objects.get(user=request.user)
            get_order.user_info = get_userinfo
            get_order.save()
            for item in cart:
                create_item = OrderItem.objects.create(
                                         order = get_order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'],
                                         )
                cart.stock_management(item['product'], item['quantity'])
            cart.clear()
            return redirect('home:dashboard')
            
            
    form = UserInfoForm(instance=request.user.userinfo)
    context = {
        'form': form,
    }
    return render(request, 'orders/checkout.html', context)


def order_history_detail(request, order_id):
    order_history_list = {}
    orders = Order.objects.get(id=order_id)
    order_items = OrderItem.objects.filter(order=orders)
    for order in order_items:
        order_history_list[str(order.id)] = order
    
    context = {
        'order': orders,
        'order_history': order_history_list
    }
    return render(request, 'orders/order_history_detail.html', context)
    
def order_history_list(request):
    user = UserInfo.objects.get(user=request.user)
    orders = Order.objects.filter(user_info=user)
    context = {
        'order_history': orders,
    }
    return render(request, 'orders/order_history.html', context)