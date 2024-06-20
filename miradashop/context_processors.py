from .models import Category, Product,Favorite
from django.shortcuts import render, get_object_or_404

def categories(request):
    return {'categories': Category.objects.all()}

def products(request):
    return {'products': Product.objects.all()}

def is_fav(request):
    products = Product.objects.filter(available=True)
    is_favorited = {}

    if request.user.is_authenticated:
        for product in products:
            is_favorited[product.id] = Favorite.objects.filter(user=request.user, product=product).exists()
    else:
        for product in products:
            is_favorited[product.id] = False

    return {'is_favorited': is_favorited}

