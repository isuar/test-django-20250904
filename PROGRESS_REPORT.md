# Progress Report

## ✅ Task 1 – Core Models & Admin Setup
- Implemented core models: **Company, SupplyChainCompany, ProductCategory, RawMaterial, Product, Application**.
- Added migrations and seed data import (Excel).
- Set up Django Admin with filters, search, and inline editing.

---

## ✅ Task 2 – Admin Enhancements
- Added inline raw materials for products.
- Configured autocomplete for foreign keys using **django-autocomplete-light**.
- Improved admin usability (filters, search fields, horizontal selectors).

---

## ✅ Task 3 – Application Workflow
- Implemented **Application** model logic with recompute status method.
- Added **custom admin actions** to recompute status.
- Wired **Approve/Recompute** button in the change page.
- Added **PDF report generation** using **xhtml2pdf**, downloadable directly from admin.
- Polished:
  - Read-only review fields (`submitted_at`, `reviewed_at`, `reviewed_by`).
  - Filters for reviewed applications.
  - Clean PDF formatting (tables for products & suppliers).

---

## ✅ Task 4 (Optional) – Excel Upload
- Added `ApplicationUpload` model to store uploaded Excel files.
- Registered **ApplicationUpload** in admin with “Process Excel” action.
- Parsing logic:
  - Reads `Company`, `Product`, `Category`, `RawMaterial`, and `Supplier`.
  - Auto-creates missing records.
  - Links them into a new `Application`.
- Fixed **redirect bug** in recompute status (removed confusing “doesn’t exist” message).
- This feature enables bulk data entry from Excel forms.

---