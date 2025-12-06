from rest_framework import serializers
from orders.models import Cart, CartItem
from products.models import Product
class CartProductSerializers(serializers.ModelSerializer):
    unit_price = serializers.DecimalField(max_digits=10, decimal_places=2, source = 'price')
    class Meta:
        model = Product
        fields = ["id", "name", "unit_price", "image"]
class AddCartItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["id", "product", "quantity"]
class CartItemSerializer(serializers.ModelSerializer):
    product = CartProductSerializers()
    total_price = serializers.SerializerMethodField(method_name='get_net_price')
    class Meta:
        model = CartItem
        fields = ['id','product', 'quantity', 'total_price']
    def get_net_price(self, cart_item: CartItem):
        return cart_item.product.price*cart_item.quantity
class UpdateCartItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['quantity']
class Cartserializer(serializers.ModelSerializer):
    Items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField(method_name='get_total_price')
    class Meta:
        model = Cart
        fields = ['id', 'user', 'Items', 'total_price']
    def get_total_price(self, cart: Cart):
        list = sum([item.product.price * item.quantity for item in cart.Items.all()])
        return list


