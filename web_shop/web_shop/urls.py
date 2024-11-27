"""
URL configuration for web_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shopApp import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('main/', views.index, name='product_list'),  # Главная страница
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),  # маршрут для добавления товара в корзину
    path('cart/', views.cart_view, name='cart_view'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    
    
]

if settings.DEBUG:  # Только в режиме разработки
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)