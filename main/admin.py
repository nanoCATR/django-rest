from django.contrib import admin
from .models import Price, Product, ProductType
# Register your models here.
class PriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'currency', 'price')

class ProductAcmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'amount', 'barcode', 'date_added', 'typeid')
    search_fields = ('title', 'amount', 'barcode', 'date_added')
    filter_horizontal = ()
    list_filter = ()

class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')

admin.site.register(Price, PriceAdmin)
admin.site.register(Product, ProductAcmin)
admin.site.register(ProductType, ProductTypeAdmin)




