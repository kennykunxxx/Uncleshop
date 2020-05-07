from django.contrib import admin
from store.models import Product, Category, Fish_Recipe, QandA
from django.utils.safestring import mark_safe

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','product_quantity', 'product_price', 'avaliable', 'image')
    list_filter = ['category', 'avaliable']
    list_editable = ('product_quantity', 'product_price', 'avaliable')
    search_fields = ('product_name',)
    ordering = ('product_name',)
    readonly_fields = ['image']

    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug':('name',)}
    
@admin.register(Fish_Recipe)
class FishRecipeAdmin(admin.ModelAdmin):
    list_display=['title', 'product']

admin.site.register(QandA)