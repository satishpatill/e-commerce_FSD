from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_products(request):
    return redirect('/products/')

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('products/', include('products.urls')),  
    path('', redirect_to_products),  # Redirect homepage to products
]