# Progress Report — Django Product Certification Web App

## ✅ Completed

### Task 1: Core Models & Data Setup

- **Models Implemented**

  - **Customer App**
    - `Company`
    - `SupplyChainCompany`
    - `CertificationBody`
  - **Product App**
    - `ProductCategory` (with `is_active`)
    - `RawMaterial` (with `is_active`)
    - `Product` (with FK to `ProductCategory` and M2M to `RawMaterial`)
  - **Application App**
    - `Application` (with `company`, `products`, `supply_chain_companies`, `status`, timestamps)

- **Database**

  - Ran `makemigrations` and `migrate` successfully.
  - Tables created in `db.sqlite3`.

- **Admin Registration**

  - Registered all models with sensible:
    - `list_display`
    - `list_filter`
    - `search_fields`
    - Inline editing for related models

- **Admin UI Check**

  - Verified in Django Admin:
    - **Customer** → Certification bodies, Companies, Supply chain companies
    - **Product** → Product categories, Products, Raw materials
    - **Application** → Applications
  - Admin user (`admin / admin`) created and functional.

- **Seed Data Command**
  - Custom command `import_seed_data` implemented:
    ```
    product/management/commands/import_seed_data.py
    ```
  - Reads `product_category.xlsx` and `raw_material.xlsx` from `/data_files` and populates DB.
  - ✅ Updated to use **openpyxl only** (dropped pandas due to Python 3.13 compatibility issue).
  - Successfully tested with:
    ```bash
    python manage.py import_seed_data
    ```

---

### Task 2: Admin Interfaces

- **Product Admin**

  - Inline raw material editing inside Product form.
  - Autocomplete (using `django-autocomplete-light`) for:
    - Product category
    - Raw materials
  - Inactive items (`is_active=False`) excluded from autocomplete.

- **Company & Supply Chain Admin**

  - Filters for `is_valid`, `country`, `city`.
  - Search fields enabled.

- **Status**
  - Verified in Admin: inline editing + autocomplete working as expected.

---

## 🔄 Dependency Adjustment

- Original scaffold included **pandas** for Excel import.
- On Python **3.13.5 (Windows)**, no prebuilt wheels for pandas exist yet, causing build failures.
- To ensure reproducibility, pandas was **removed** and replaced with an **openpyxl-only import** implementation.
- Functionality unchanged — categories and raw materials are still loaded correctly from Excel.

**Current dependencies (`requirements.in`):**

```
django==5.2.4
openpyxl==3.1.5
django-autocomplete-light==3.12.1
python-dotenv==1.0.1
xhtml2pdf==0.2.15
```

---

## 🔮 Upcoming Tasks

### Task 3: Application Workflow

- Allow Customer Service to create applications from Excel form.
- Reviewer approves/rejects products & supply chain companies.
- Add status tracking (`pending`, `approved`, `rejected`).
- Implement PDF report generation for approved products & companies.

### Optional Enhancements

- Excel upload via admin (auto-populate applications).
- Background job processing (Celery).
- REST API endpoints for programmatic submission.
- Customer-facing portal.
- Process verification (using `process.xlsx`).

---

✅ **Status:** Task 1 + Task 2 complete. Dependencies cleaned up. Ready to start Task 3 (Application Workflow).
