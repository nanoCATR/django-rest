"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import ProductAPIView, RetrieveUpdateDestroyProductAPIView, ProductAmountDecreaseAPIView, PriceAPIView, RetrieveUpdateDestroyPriceAPIView, ProductTypeAPIView, RetrieveUpdateDestroyProductTypeAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/product/', ProductAPIView.as_view()),
    path('api/v1/product/<int:pk>/', RetrieveUpdateDestroyProductAPIView.as_view()),
    path('api/v1/product_amount_descrease/<int:pk>/', ProductAmountDecreaseAPIView.as_view()),
    path('api/v1/price/', PriceAPIView.as_view()),
    path('api/v1/price/<int:pk>/', RetrieveUpdateDestroyPriceAPIView.as_view()),
    path('api/v1/producttype/', ProductTypeAPIView.as_view()),
    path('api/v1/producttype/<int:pk>/', RetrieveUpdateDestroyProductTypeAPIView.as_view()),
]
