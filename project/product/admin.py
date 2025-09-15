from django.contrib import admin
from .models import ProductCategory, RawMaterial, Product
from .forms import ProductAdminForm, ProductRawMaterialInlineForm

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active")
    search_fields = ("name",)
    list_filter = ("is_active",)

@admin.register(RawMaterial)
class RawMaterialAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active")
    search_fields = ("name",)
    list_filter = ("is_active",)

class RawMaterialThroughInline(admin.TabularInline):
    model = Product.raw_materials.through
    form = ProductRawMaterialInlineForm
    extra = 1
    fk_name = "product"  # ensure inline attaches to Product side

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ("name", "product_category", "is_active")
    search_fields = ("name", "product_category__name", "raw_materials__name")
    list_filter = ("product_category", "is_active")
    inlines = [RawMaterialThroughInline]
    exclude = ("raw_materials",)  # avoid duplicate M2M widget when using inline