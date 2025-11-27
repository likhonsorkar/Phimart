from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from products.serializers import ProductSerializers, CategorySerializers
from products.models import Product, Category

class View_products(APIView):
    def get(self, request):
        product = Product.objects.select_related("category").all()
        serializer = ProductSerializers(product, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ProductSerializers(data = request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class View_specific_products(APIView):
    def get(self, request, id):
        product = get_object_or_404(Product, pk=id)
        seralizer = ProductSerializers(product)
        return Response(seralizer.data)
    def put(self, request, id):
        product = get_object_or_404(Product, pk=id)
        seralizer = ProductSerializers(product, data = request.data)
        seralizer.is_valid(raise_exception=True)
        seralizer.save()
        return Response(seralizer.data)
    def delete(self, request, id):
        product = get_object_or_404(Product, pk=id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class View_categories(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializers(category, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = CategorySerializers(data = request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class View_specific_categories(APIView):
    def get(self,request, id):
        category = get_object_or_404(Category, pk = id)
        serializer = CategorySerializers(category)
        return Response(serializer.data)
    def put(self, request, id):
        category = get_object_or_404(Category, pk = id)
        serializer = CategorySerializers(category, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self, request, id):
        category = get_object_or_404(Category, pk=id)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
