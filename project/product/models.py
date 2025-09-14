from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class RawMaterial(models.Model):
    name = models.CharField(max_length=200, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, related_name='products')
    raw_materials = models.ManyToManyField(RawMaterial, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
