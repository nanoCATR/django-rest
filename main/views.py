from django.shortcuts import render
from django.http import Http404
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, Price, ProductType
from .serializers import ProductSerializer, PriceSerializer, ProductTypeSerializer

# GET всех товаров/POST нового товара
class ProductAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

# GET/PUT/DELETE товара с указанным id
class RetrieveUpdateDestroyProductAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

# PATCH уменьшение остатка на складе
class ProductAmountDecreaseAPIView(generics.UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.amount > 0:
            instance.amount -= 1
            instance.save()
            serializer = self.get_serializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Товар уже отсутствует на складе"}, status=status.HTTP_400_BAD_REQUEST)

# GET всех цен/POST новой цены
class PriceAPIView(generics.ListCreateAPIView):
    serializer_class = PriceSerializer
    queryset = Price.objects.all()

# GET/PUT/DELETE цены с указанным id
class RetrieveUpdateDestroyPriceAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PriceSerializer
    queryset = Price.objects.all()

# GET всех типов товара/POST нового типа
class ProductTypeAPIView(generics.ListCreateAPIView):
    serializer_class = ProductTypeSerializer
    queryset = ProductType.objects.all()

# GET/PUT/DELETE типа товара с указанным id
class RetrieveUpdateDestroyProductTypeAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductTypeSerializer
    queryset = ProductType.objects.all()
    