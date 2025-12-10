from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from products.serializers import ProductSerializers, CategorySerializers, ReviewsSerializer
from products.models import Product, Category, Reviews
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from products.pagination import Default_Pagination
from products.filters import ProductFilter
from api.permissions import IsAdminOrReadOnly
from products.permissions import IsReviewAuthourOrReadOnly

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.select_related("category").all()
    serializer_class = ProductSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    pagination_class = Default_Pagination
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'name', 'updated_at']
    permission_classes = [IsAdminOrReadOnly]
    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        if product.stock >10:
            return Response({'message': 'product with stock more then 10 could not be deleted'})
        self.perform_destroy(product)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [IsAdminOrReadOnly]

class ReviewsViewSet(ModelViewSet):
    serializer_class = ReviewsSerializer
    permission_classes = [IsReviewAuthourOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,)
    def get_queryset(self):
        return Reviews.objects.filter(product_id = self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}