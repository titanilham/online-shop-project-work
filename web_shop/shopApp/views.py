from django.shortcuts import render
from .models import Product
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .cart import Cart  # Импортируем класс корзины

def login(request):
    return render(request, "login.html")

def index(request):
    query = request.GET.get('query', '')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)  # Получаем товар по ID (pk)
    return render(request, 'product_detail.html', {'product': product})



# views.py
def cart_view(request):
    cart = Cart(request)
    return render(request, 'cart_view.html', {'cart': cart})

def remove_from_cart(request, product_id):
    cart = Cart(request)  # Получаем корзину
    cart.remove(product_id)  # Удаляем товар из корзины
    return redirect('cart_view')  # Перенаправляем на страницу корзины

def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)  # Получаем товар по ID
    cart = Cart(request)  # Инициализируем корзину с использованием сессии
    cart.add(product)  # Добавляем товар в корзину
    return redirect('cart_view')  # Перенаправляем на страницу корзины

def checkout_view(request):
    # Ваша логика оформления заказа
    return render(request, 'checkout.html')