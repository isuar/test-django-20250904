# project/product/forms.py
from django import forms
from dal import autocomplete
from .models import Product

class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            # Single-select with autocomplete for category
            "product_category": autocomplete.ModelSelect2(
                url="product-category-autocomplete",
                attrs={"data-minimum-input-length": 1}
            ),
            # Multi-select with autocomplete for raw materials (if you want it on the main form)
            "raw_materials": autocomplete.ModelSelect2Multiple(
                url="raw-material-autocomplete",
                attrs={"data-minimum-input-length": 1}
            ),
        }

# Inline form for the M2M through table so inline rows use DAL too
class ProductRawMaterialInlineForm(forms.ModelForm):
    class Meta:
        model = Product.raw_materials.through  # auto-generated through model
        fields = "__all__"
        widgets = {
            # Default field name on the through model is "rawmaterial"
            "rawmaterial": autocomplete.ModelSelect2(
                url="raw-material-autocomplete",
                attrs={"data-minimum-input-length": 1}
            )
        }
