from .models import Product
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .cart import Cart  
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('product_list')  # Перенаправление на главную страницу
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Сохраняем нового пользователя
            login(request, user)  # Логиним пользователя сразу после регистрации
            return redirect('product_list')  # Перенаправление на главную страницу
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})


@login_required  # Этот декоратор защищает страницу от неавторизованных пользователей
def index(request):
    # Логика для главной страницы
    return render(request, 'index.html')


def index(request):
    query = request.GET.get('query', '')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)  # Получение товара по ID (pk)
    return render(request, 'product_detail.html', {'product': product})



# views.py
def cart_view(request):
    cart = Cart(request)
    return render(request, 'cart_view.html', {'cart': cart})

def remove_from_cart(request, product_id):
    cart = Cart(request)  
    cart.remove(product_id)  # Удаление товара из корзины
    return redirect('cart_view')  # Перенаправление на страницу корзины

def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)  # Получение товара по ID
    cart = Cart(request)  
    cart.add(product)  # Добавляем товар в корзину
    return redirect('cart_view')  # Перенаправляем на страницу корзины

def checkout_view(request):
    
    return render(request, 'checkout.html')

