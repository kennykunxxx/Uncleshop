from store.models import Product
from decimal import Decimal
import datetime


class Cart(object):
    def __init__(self, request):
        
        """
        get cart session or create one if there isn't
        """
        
        self.session = request.session
        user = request.user
        self.user = user
        cart = self.session.get('cart')
        if cart is None:
            cart = self.session['cart'] = {}
        self.cart = cart
        
    def add(self, product, quantity):
        
        """
        update dictionary with product ID
        Take away from stock
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.product_price),
            }
            
        self.cart[product_id]['quantity'] += int(quantity)
        self.save_session()
        
        """
        might need to add update_quantity for basket page
        date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
        """
        
    def save_session(self):
        
        """
        Save Session
        """
        
        self.session.modified = True
                                                    
    
    def remove(self, product):
        
        """
        removes item from cart session
        """
        
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save_session()
            
    def __iter__(self):
        
        """
        Iterates through the product ID and add products to cart
        Adds total price of each products to dictionary
        """
        
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        
        cart = self.cart.copy()
        for product in products:
                cart[str(product.id)]['product'] = product
            
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = str(item['quantity'] * item['price'])
            item['price'] = str(item['price'])
            yield item
        
    def __len__(self):
        
        """
        Calculates the number of product in the cart
        """
        
        return sum(item['quantity'] for item in self.cart.values())
        
    def get_total_price(self):
        
        """
        Calculates total price
        """
        
        return sum(item['quantity']*Decimal(item['quantity']) for item in self.cart.values())
        
    def stock_management(self, product, quantity):
        product.product_quantity -= quantity
        product.save()
        
        
        
    def clear(self):
        """
        Clear cart by deleting the session
        """
        del self.session['cart']
        self.save_session()
            
        
            