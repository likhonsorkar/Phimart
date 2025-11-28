from django.urls import path, include
from products.views import ProductViewSet, CategoryViewSet, ReviewsViewSet
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)

product_router = routers.NestedDefaultRouter(router, 'products', lookup = "product")
product_router.register('review', ReviewsViewSet, basename='product-review')
urlpatterns = [
   path('', include(router.urls)),
   path('', include(product_router.urls))
]
