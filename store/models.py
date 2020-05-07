from django.db import models
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField



#from streams import blocks  

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.CharField(max_length=200, null=True)
    category_image = models.ImageField(upload_to='store/category/', null=True)
    
    def get_absolute_url(self):
        return reverse('store:product_category', args=[self.slug])
        
    def get_absolute_url_recipe(self):
        return reverse('store:recipe_category', args=[self.slug])
        
    def __str__(self):
        return '%s' % (self.name)
    
class Product(models.Model):
    category = models.ManyToManyField(Category, related_name='product_category')
    product_name = models.CharField(max_length=250)
    product_quantity = models.IntegerField()
    product_price = models.FloatField()
    product_description = models.TextField()
    product_image = models.ImageField(upload_to='store/product/', blank=True)
    avaliable = models.BooleanField(default=True)
    
    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.id])

    
    def __str__(self):
        return '%s' % (self.product_name)
    
        

    def image(self):
        """
        for admin thumb nail pic thing
        """
        
        if self.product_image:
            return mark_safe('<img src="%s" style="width: 45px; height: 45px" />' % self.product_image.url)
        else:
            return 'No image found'
            
    image.short_description = 'Image'
    
    
class Fish_Recipe(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='recipe_product', blank=False, null=True)
    title = models.CharField(max_length=200, blank=False, null=True)
    text = RichTextField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Fish Recipe'
        verbose_name_plural = 'Fish Recipes'
        
    
        
class QandA(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_QandA', blank=False, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_QandA', null=True)
    question = models.CharField(max_length=200, blank=False, null=False)
    answer = models.TextField()
    staff_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
        verbose_name = ' Q and A'
        verbose_name_plural = 'Qs and As'
