from django.contrib import admin
from .models import Company, SupplyChainCompany, CertificationBody

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "city")
    search_fields = ("name", "country", "city")

@admin.register(SupplyChainCompany)
class SupplyChainCompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "is_valid", "country", "city")
    list_filter = ("is_valid",)
    search_fields = ("name",)

@admin.register(CertificationBody)
class CertificationBodyAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "city")
    search_fields = ("name",)
