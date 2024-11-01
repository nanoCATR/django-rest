from django.contrib import admin
from .models import Price, Product, ProductType, ProductPrice
# Register your models here.
class PriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'currency', 'price')


class PriceInline(admin.TabularInline):
    model = Product.price.through
    extra = 1

class ProductAcmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_prices', 'amount', 'barcode', 'date_added', 'typeid')
    search_fields = ('title', 'amount', 'barcode', 'date_added')
    filter_horizontal = ()
    list_filter = ()
    inlines = [PriceInline]

    def get_prices(self, obj):
            return ", ".join([f"{price.currency} {price.price}" for price in obj.price.all()])
    get_prices.short_description = 'price'

class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')

class ProductPriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'price')

admin.site.register(Price, PriceAdmin)
admin.site.register(Product, ProductAcmin)
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(ProductPrice, ProductPriceAdmin)




