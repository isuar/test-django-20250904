# project/product/autocomplete.py
from dal import autocomplete
from django.db.models import Q

from .models import ProductCategory, RawMaterial

class ProductCategoryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Only allow authenticated staff to query
        if not self.request.user.is_authenticated:
            return ProductCategory.objects.none()

        qs = ProductCategory.objects.filter(is_active=True)

        if self.q:
            qs = qs.filter(Q(name__icontains=self.q))

        return qs.order_by("name")


class RawMaterialAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return RawMaterial.objects.none()

        qs = RawMaterial.objects.filter(is_active=True)

        if self.q:
            qs = qs.filter(Q(name__icontains=self.q))

        return qs.order_by("name")
