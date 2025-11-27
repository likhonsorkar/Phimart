from django.urls import path, include

urlpatterns = [
    path('products/', include('products.products_urls')),
    path('categories/', include('products.categories_urls')),
]
