from rest_framework import serializers
from products.models import Product,Category
from decimal import Decimal
class CategorySerializers(serializers.ModelSerializer):
    # id = serializers.IntegerField()
    # name = serializers.CharField()
    # description = serializers.CharField()
    class Meta:
        model = Category
        fields = '__all__'
class ProductSerializers(serializers.ModelSerializer):
    unit_price = serializers.DecimalField(max_digits=10, decimal_places=2, source = 'price')
    class Meta:
        model = Product
        fields = ["id", "name", "description", "unit_price", "stock", "image", "category", "created_at", "updated_at"]
# class ProductSerializers(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=255)
#     description = serializers.CharField()
#     unit_price = serializers.DecimalField(max_digits=10, decimal_places=2, source = 'price')
#     # price_with_tax = serializers.SerializerMethodField(method_name='tax_calculate')
#     stock = serializers.IntegerField()
#     image = serializers.ImageField(required=False, allow_null=True)
#     category = CategorySerializers()
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)

#     # def tax_calculate(self, product):
#     #     return round(product.price * Decimal(1.1), 2)


