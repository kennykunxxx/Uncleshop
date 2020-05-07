from django.shortcuts import render, get_object_or_404
from store.models import Product, Category, Fish_Recipe, QandA
from orders.forms import QuantityForm
from store.forms import QandAForms, AnswerForm
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(avaliable=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {'categories': categories,
               'products': products,
              }
    return render(request, 'store/item_list.html', context)


def product_detail(request, id):
    product = get_object_or_404(Product, id=id, avaliable=True)
    quantity_form = QuantityForm(id)
    qa = QandA.objects.filter(product__id=id)
    similar_products = get_similar_product(id)
    if request.method == 'POST':
        form = QandAForms(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            q_and_a = QandA.objects.create(product=product,
                                           user=request.user,
                                           question=cd['question'])
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            return HttpResponse('it went wrong')
                                           
    question_form = QandAForms()
    answer_form = AnswerForm()
    context = {
        'product': product,
        'quantity_form': quantity_form,
        'qa': qa,
        'question_form': question_form,
        'answer_form': answer_form,
        'similar_products': similar_products
        
    }
    try:
        context['recipe'] = Fish_Recipe.objects.get(product=product)
    except ObjectDoesNotExist:
        pass
        
        
    return render(request, 'store/item_detail.html', context)
    
def get_similar_product(product_id):
    category_ids = list(Product.objects.filter(id=product_id).values_list(
                                                str('category__id'), flat=True))
    category = Category.objects.filter(id__in=category_ids)
    similar_product = Product.objects.filter(
                    category__in = category).distinct().exclude(id=product_id)[0:5]
    return similar_product



def recipe_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    recipe = Fish_Recipe.objects.all()
    products = Product.objects.filter(avaliable=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        recipe = Fish_Recipe.objects.filter(product__in=products)
    context = {'categories': categories,
               'products': products,
               'recipe': recipe,
              }
    return render(request, 'store/recipe_list.html', context)
# Create your views here.

@staff_member_required
def q_and_a(request, q_id):
    if request.method == 'POST':
        q_n_a = QandA.objects.get(id=q_id)
        form = AnswerForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            q_n_a.answer = cd['answer']
            q_n_a.staff_user = request.user
            q_n_a.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
   



"""

"""
    
            
