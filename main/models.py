from django.db import models

class ProductType(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Price(models.Model):
    currency = models.CharField(max_length=3)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.currency

class ProductPrice(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    price = models.ForeignKey('Price', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.title} - {self.price}"

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.ManyToManyField(Price, through=ProductPrice)
    amount = models.IntegerField()
    barcode = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    typeid = models.ForeignKey(ProductType, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    