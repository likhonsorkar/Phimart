from rest_framework import serializers
from products.models import Product,Category, Reviews
from decimal import Decimal
class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
class ProductSerializers(serializers.ModelSerializer):
    unit_price = serializers.DecimalField(max_digits=10, decimal_places=2, source = 'price')
    class Meta:
        model = Product
        fields = ["id", "name", "description", "unit_price", "stock", "image", "category", "created_at", "updated_at"]
class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ["id", "name", "description"]
    def create(self, validated_data):
        product_id = self.context['product_id']
        return Reviews.objects.create(product_id = product_id, **validated_data)

