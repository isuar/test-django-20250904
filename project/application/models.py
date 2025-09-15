# project/application/models.py
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from customer.models import Company, SupplyChainCompany
from product.models import Product

User = get_user_model()

class Application(models.Model):
    # ---- Status choices ----
    STATUS_PENDING = "pending"
    STATUS_APPROVED = "approved"
    STATUS_REJECTED = "rejected"
    STATUS_CHOICES = [
        (STATUS_PENDING, "Pending"),
        (STATUS_APPROVED, "Approved"),
        (STATUS_REJECTED, "Rejected"),
    ]

    # ---- Core fields ----
    company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name="applications")
    products = models.ManyToManyField(Product, related_name="applications", blank=True)
    supply_chain_companies = models.ManyToManyField(SupplyChainCompany, related_name="applications", blank=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
    submitted_at = models.DateTimeField(default=timezone.now)  # explicit default keeps record even if created via shell
    reviewed_at = models.DateTimeField(null=True, blank=True)
    reviewed_by = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL, related_name="reviewed_applications"
    )

    notes = models.TextField(blank=True, default="")

    class Meta:
        ordering = ("-submitted_at",)
        indexes = [
            models.Index(fields=["status"]),
            models.Index(fields=["submitted_at"]),
        ]
        verbose_name = "Application"
        verbose_name_plural = "Applications"

    def __str__(self):
        return f"Application #{self.pk} - {self.company.name}"

    # ---- Status helpers ----
    @property
    def is_pending(self) -> bool:
        return self.status == self.STATUS_PENDING

    @property
    def is_approved(self) -> bool:
        return self.status == self.STATUS_APPROVED

    @property
    def is_rejected(self) -> bool:
        return self.status == self.STATUS_REJECTED

    # ---- Core logic ----
    def recompute_status(self) -> str:
        """
        Recompute application status based on linked products and suppliers.

        Rules:
        - If there are no products OR no suppliers → PENDING
        - If any linked product or supplier is invalid → REJECTED
        - Otherwise (both exist and all valid) → APPROVED
        """
        prods = self.products.all()
        supps = self.supply_chain_companies.all()

        if not prods.exists() or not supps.exists():
            self.status = self.STATUS_PENDING
            return self.status

        if prods.filter(is_valid=False).exists() or supps.filter(is_valid=False).exists():
            self.status = self.STATUS_REJECTED
        else:
            self.status = self.STATUS_APPROVED

        return self.status

# ---- Optional Task 4: Excel Upload model ----
class ApplicationUpload(models.Model):
    file = models.FileField(upload_to="uploads/applications/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Upload #{self.pk} ({self.file.name})"