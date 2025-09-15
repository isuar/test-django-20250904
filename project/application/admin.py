# project/application/admin.py
from django.contrib import admin, messages
from django.urls import path, reverse
from django.shortcuts import get_object_or_404, redirect
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.utils import timezone
from xhtml2pdf import pisa

from .models import Application, ApplicationUpload
from customer.models import Company, SupplyChainCompany
from product.models import Product, ProductCategory, RawMaterial


@admin.action(description="Recompute status for selected applications")
def recompute_status_action(modeladmin, request, queryset):
    count = 0
    for app in queryset:
        app.recompute_status()
        app.reviewed_at = timezone.now()
        app.reviewed_by = request.user
        app.save(update_fields=["status", "reviewed_at", "reviewed_by"])
        count += 1
    messages.success(request, f"Recomputed status for {count} application(s).")


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("id", "company", "status", "submitted_at", "reviewed_at")
    list_filter = ("status", "submitted_at", "reviewed_at")
    date_hierarchy = "submitted_at"
    search_fields = ("company__name",)
    filter_horizontal = ("products", "supply_chain_companies")
    readonly_fields = ("submitted_at", "reviewed_at", "reviewed_by")
    actions = [recompute_status_action]
    change_form_template = "admin/application_change_form.html"

    def get_urls(self):
        urls = super().get_urls()
        custom = [
            path(
                "<int:pk>/report/",
                self.admin_site.admin_view(self.pdf_report_view),
                name="application-report",
            ),
            path(
                "<int:pk>/approve-recompute/",
                self.admin_site.admin_view(self.approve_and_recompute_view),
                name="application-approve-recompute",
            ),
        ]
        return custom + urls

    def approve_and_recompute_view(self, request, pk):
        app = get_object_or_404(Application, pk=pk)
        app.recompute_status()
        app.reviewed_at = timezone.now()
        app.reviewed_by = request.user
        app.save(update_fields=["status", "reviewed_at", "reviewed_by"])

        self.message_user(
            request,
            f"Application #{app.pk} recomputed to status '{app.status}'.",
            level=messages.SUCCESS,
        )

        # ✅ Redirect to the correct object change page (no more "2/2" bug)
        url = reverse("admin:application_application_change", args=[app.pk])
        return redirect(url)

    def pdf_report_view(self, request, pk):
        app = get_object_or_404(Application, pk=pk)
        approved_products = (
            app.products.filter(is_valid=True)
            .select_related("product_category")
            .prefetch_related("raw_materials")
        )
        approved_suppliers = app.supply_chain_companies.filter(is_valid=True)
        has_country = (
            approved_suppliers.exclude(country__isnull=True)
            .exclude(country__exact="")
            .exists()
        )

        html = render_to_string(
            "application_report.html",
            {
                "app": app,
                "approved_products": approved_products,
                "approved_suppliers": approved_suppliers,
                "has_country": has_country,
            },
        )

        response = HttpResponse(content_type="application/pdf")
        filename = f"application_{app.pk}_report.pdf"
        response["Content-Disposition"] = f'attachment; filename="{filename}"'

        pisa.CreatePDF(html, dest=response)
        return response
