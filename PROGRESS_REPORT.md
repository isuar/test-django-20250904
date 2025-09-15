# Progress Report — Django Product Certification Web App

## ✅ Completed

### Task 1: Core Models & Data Setup
- Implemented models:
  - **Customer App**: `Company`, `SupplyChainCompany`, `CertificationBody`
  - **Product App**: `ProductCategory` (with `is_active`), `RawMaterial` (with `is_active`), `Product` (with FK to `ProductCategory` and M2M to `RawMaterial`)
  - **Application App**: `Application` (with `company`, `products`, `supply_chain_companies`, `status`, timestamps, reviewer info)
- Database migrations run successfully.
- Admin registered with list filters, search, and inline editing.
- Admin verified for Customer, Product, and Application models.
- Seed data import command (`import_seed_data`) implemented with **openpyxl only** (removed pandas for Python 3.13 compatibility).

---

### Task 2: Admin Interfaces
- Product Admin: inline raw material editing inside Product form.
- Autocomplete with `django-autocomplete-light` for Product Category and Raw Materials.
- Inactive items excluded from autocomplete.
- Company & SupplyChainCompany Admin: filters and search enabled.
- Verified in admin: inline editing + autocomplete working.

---

### Task 3: Application Workflow
- **Reviewer workflow implemented**:
  - Create applications in admin linking Company, Products, and Supply Chain Companies.
  - Bulk action to recompute status.
  - Per-application **Recompute Status** and **Download PDF Report** buttons added to the change form.
- **Status logic**:
  - Pending if no products/suppliers attached.
  - Rejected if any linked product/supplier is invalid.
  - Approved if all linked items are valid.
- **PDF Export**:
  - Generates certification report listing approved Products and Supply Chain Companies.
  - Includes Product raw materials with proper comma formatting.
  - Dynamically hides Country column if no supplier has country data.
  - Basic table styling for clean, professional look.
- **Admin UX**:
  - Filters, search, date hierarchy, read-only audit fields added for Applications.
- **Performance**:
  - Query optimization in PDF view (`select_related` + `prefetch_related`) to avoid N+1 queries.

---

## 🔄 Dependency Adjustment
- Originally scaffolded with pandas.  
- Removed pandas (no wheels yet for Python 3.13 on Windows).  
- Replaced with openpyxl-only import logic.  
- Dependencies now:
```
django==5.2.4
openpyxl==3.1.5
django-autocomplete-light==3.12.1
python-dotenv==1.0.1
xhtml2pdf==0.2.15
```

---

## 🔮 Upcoming (Optional) Tasks
- Excel upload via admin (auto-populate applications).
- Background job processing (Celery).
- REST API endpoints (programmatic submissions + docs).
- Customer-facing application pages (Django templates or Vue/React).
- Process verification (`process.xlsx`).

---

✅ **Status:** Task 1 + Task 2 + Task 3 complete. Core workflow polished, reproducible, and working with PDF export. Ready to proceed to optional tasks.
