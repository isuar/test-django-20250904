from django.contrib import admin
from .models import ProductCategory, RawMaterial, Product
from .forms import ProductAdminForm, ProductRawMaterialInlineForm

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)

@admin.register(RawMaterial)
class RawMaterialAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)

class RawMaterialThroughInline(admin.TabularInline):
    model = Product.raw_materials.through
    form = ProductRawMaterialInlineForm
    extra = 1
    fk_name = "product"

@admin.action(description="Approve selected products")
def approve_products(modeladmin, request, queryset):
    updated = queryset.update(is_valid=True)
    modeladmin.message_user(request, f"Approved {updated} product(s).")

@admin.action(description="Reject selected products")
def reject_products(modeladmin, request, queryset):
    updated = queryset.update(is_valid=False)
    modeladmin.message_user(request, f"Rejected {updated} product(s).")

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ("name", "product_category", "is_active", "is_valid")
    list_filter = ("product_category", "is_active", "is_valid")
    search_fields = ("name", "product_category__name", "raw_materials__name")
    inlines = [RawMaterialThroughInline]
    exclude = ("raw_materials",)
    actions = [approve_products, reject_products]