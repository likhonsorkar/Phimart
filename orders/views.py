from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from orders.models import Cart, CartItem
from orders.serializers import Cartserializer, CartItemSerializer, AddCartItemSerializers, UpdateCartItemSerializers
# Create your views here.
class Cartviewset(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = Cartserializer

class CartItemsViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    def get_serializer_class(self):  
        if self.request.method == "POST":
            return AddCartItemSerializers
        if self.request.method == "PATCH":
            return UpdateCartItemSerializers
        return CartItemSerializer
    def get_queryset(self):
        return CartItem.objects.filter(cart_id = self.kwargs['cart_pk'])
    def perform_create(self, serializer):
        cart_id = self.kwargs['cart_pk']
        product_id = serializer.validated_data['product']
        quantity = serializer.validated_data['quantity']
        try:
            item = CartItem.objects.get(cart_id=cart_id, product_id=product_id)
            item.quantity += quantity
            item.save()
        except CartItem.DoesNotExist:
            serializer.save(cart_id=cart_id)