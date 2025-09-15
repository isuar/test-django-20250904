from django.contrib import admin
from .models import Company, SupplyChainCompany, CertificationBody

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "city")
    search_fields = ("name", "country", "city")

@admin.action(description="Approve selected supply chain companies")
def approve_suppliers(modeladmin, request, queryset):
    updated = queryset.update(is_valid=True)
    modeladmin.message_user(request, f"Approved {updated} supplier(s).")

@admin.action(description="Reject selected supply chain companies")
def reject_suppliers(modeladmin, request, queryset):
    updated = queryset.update(is_valid=False)
    modeladmin.message_user(request, f"Rejected {updated} supplier(s).")

@admin.register(SupplyChainCompany)
class SupplyChainCompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "is_valid", "country", "city")
    list_filter = ("is_valid", "country")
    search_fields = ("name", "country", "city")
    actions = [approve_suppliers, reject_suppliers]

@admin.register(CertificationBody)
class CertificationBodyAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "city")
    search_fields = ("name", "country", "city")