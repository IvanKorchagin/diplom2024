from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Product, Favorite,Category

def index(request):
    return render(request, 'shop/product/index.html')


def contacts(request):
    return render(request,'shop/product/contacts.html')

def about(request):
    return render(request,'shop/product/about.html')

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    cart_product_form = CartAddProductForm()
    user = request.user
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        
    if user.is_authenticated:
        favorite_products = Favorite.objects.filter(user=user).values_list('product_id', flat=True)
        for product in products:
            product.is_favorited = product.id in favorite_products
    else:
        for product in products:
            product.is_favorited = False

    return render(request,
                  'shop/product/list.html',
                   {'cart_product_form': cart_product_form,
                    'category': category,
                    'categories': categories,
                    'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    is_favorited = False
    if request.user.is_authenticated:
        is_favorited = Favorite.objects.filter(user=request.user, product=product).exists()
    return render(request, 'shop/product/detail.html', {
        'product': product,
        'cart_product_form': cart_product_form,
        'is_favorited': is_favorited
    })

@login_required
def add_to_favorites(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, product=product)
    return JsonResponse({'status': 'added'})

@login_required
def remove_from_favorites(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Favorite.objects.filter(user=request.user, product=product).delete()
    return JsonResponse({'status': 'removed'})

@login_required
def view_favorites(request):
    favorites = Favorite.objects.filter(user=request.user).select_related('product')
    products = [favorite.product for favorite in favorites]
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/favorite_products.html', {'products': products,'cart_product_form': cart_product_form})



