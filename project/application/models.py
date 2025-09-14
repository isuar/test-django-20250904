from django.db import models
from customer.models import Company, SupplyChainCompany
from product.models import Product

class Application(models.Model):
    STATUS = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='applications')
    products = models.ManyToManyField(Product, blank=True, related_name='applications')
    supply_chain_companies = models.ManyToManyField(SupplyChainCompany, blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f'Application #{self.id} - {self.company.name}'
