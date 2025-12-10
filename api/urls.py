from django.urls import path, include
from products.views import ProductViewSet, CategoryViewSet, ReviewsViewSet
from orders.views import Cartviewset, CartItemsViewSet
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)
router.register('carts', Cartviewset, basename="cart")

product_router = routers.NestedDefaultRouter(router, 'products', lookup = "product")
product_router.register('review', ReviewsViewSet, basename='product-review')

carts_router = routers.NestedDefaultRouter(router, 'carts', lookup = 'cart')
carts_router.register('items', CartItemsViewSet, basename='cart-item' )


urlpatterns = [
   path('', include(router.urls)),
   path('', include(product_router.urls)),
   path('', include(carts_router.urls))
]
