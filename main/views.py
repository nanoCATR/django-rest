from django.shortcuts import render
from django.http import Http404
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, Price, ProductType, ProductPrice
from .serializers import ProductSerializer, PriceSerializer, ProductTypeSerializer

# GET всех товаров/POST нового товара
class ProductAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def create(self, request, *args, **kwargs):
        prices_data = request.data.pop('price')
        product_serializer = self.get_serializer(data=request.data)
        product_serializer.is_valid(raise_exception=True)
        product = product_serializer.save()
        
        for price_data in prices_data:
            price, created = Price.objects.get_or_create(**price_data)
            ProductPrice.objects.create(product=product, price=price)
        
        headers = self.get_success_headers(product_serializer.data)
        return Response(product_serializer.data, status=201, headers=headers)

# GET/PUT/DELETE товара с указанным id
class RetrieveUpdateDestroyProductAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        prices_data = request.data.pop('price', [])
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        product = serializer.save()

        # Обновление цен
        if prices_data:
            product.price.clear()
            for price_data in prices_data:
                price, created = Price.objects.get_or_create(**price_data)
                ProductPrice.objects.create(product=product, price=price)

        return Response(serializer.data)

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
    
