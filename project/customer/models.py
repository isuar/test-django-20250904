from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Company(models.Model):
    users = models.ManyToManyField(User, blank=True, related_name='companies')
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class SupplyChainCompany(models.Model):
    name = models.CharField(max_length=255)
    is_valid = models.BooleanField(default=False)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class CertificationBody(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
