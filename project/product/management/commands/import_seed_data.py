from django.core.management.base import BaseCommand
from django.conf import settings
from pathlib import Path
import pandas as pd

from product.models import ProductCategory, RawMaterial

class Command(BaseCommand):
    help = "Import ProductCategory and RawMaterial from data_files/*.xlsx"

    def handle(self, *args, **kwargs):
        data_dir = Path(settings.BASE_DIR).parent / 'data_files'

        # Product Categories
        cat_file = data_dir / 'product_category.xlsx'
        if cat_file.exists():
            df = pd.read_excel(cat_file)
            for _, row in df.iterrows():
                name = str(row.get('name') or row.get('Name') or '').strip()
                if name:
                    ProductCategory.objects.get_or_create(name=name)
            self.stdout.write(self.style.SUCCESS("Product categories imported."))
        else:
            self.stdout.write(self.style.WARNING("No product_category.xlsx found."))

        # Raw Materials
        rm_file = data_dir / 'raw_material.xlsx'
        if rm_file.exists():
            df = pd.read_excel(rm_file)
            for _, row in df.iterrows():
                name = str(row.get('name') or row.get('Name') or '').strip()
                if name:
                    RawMaterial.objects.get_or_create(name=name)
            self.stdout.write(self.style.SUCCESS("Raw materials imported."))
        else:
            self.stdout.write(self.style.WARNING("No raw_material.xlsx found."))
