# Documentation

## 📌 Introduction
This project is a Django-based MVP web application designed to manage **product certification workflows**.  
It was developed as part of a coding exercise to demonstrate backend design, data modeling, and admin customization skills.

The system replicates a real-world certification workflow where customer service staff enter application data, and reviewers validate, approve, or reject products and supply chain companies. Approved applications can be exported as PDF reports.

---

## 🏗️ System Overview

### Core Models
- **Company** – Represents a customer company applying for certification.
- **SupplyChainCompany** – Represents suppliers or partners in the supply chain.
- **CertificationBody** – Represents the authority that issues certifications.
- **ProductCategory** – Categories for products (seeded from Excel).
- **RawMaterial** – Materials linked to products (seeded from Excel).
- **Product** – Belongs to a category and has multiple raw materials.
- **Application** – Links companies, products, and supply chain companies. Tracks status and review metadata.
- **ApplicationUpload (Optional Task 4)** – Stores uploaded Excel files for bulk importing applications.

### Workflows
1. Customer Service staff enter applications based on Excel forms.
2. Reviewers approve or reject products and supply chain companies.
3. Status is recomputed automatically (Pending / Approved / Rejected).
4. Reviewers can download a **PDF certification report** with approved products and suppliers.
5. (Optional) Applications can be bulk-imported by uploading Excel files.

---

## ⚙️ Setup Instructions

1. Clone repository and install dependencies (`requirements.txt`).  
2. Configure `.env` with `DJANGO_SECRET_KEY` and `DEBUG`.  
3. Run migrations and create a superuser (or use admin/admin).  
4. Import seed data using `python manage.py import_seed_data`.  
5. Start development server: `python manage.py runserver`.  
6. Log into Django Admin to manage applications.

*(Detailed setup steps are in README.md)*

---

## 👥 User Roles

- **Customer Service Staff**
  - Enter applications into the system (or upload Excel files if enabled).
  - Ensure company, products, and suppliers are correctly entered.

- **Reviewer**
  - Review each application, approve or reject linked products and suppliers.
  - Recompute status to update application state.
  - Generate and download PDF reports for approved applications.

---

## 🔄 Application Workflow

1. Customer submits filled Excel form.  
2. Customer Service enters data via admin (manual) or uploads the file (optional task).  
3. Reviewer inspects application:  
   - If products/suppliers invalid → Reject.  
   - If valid → Approve.  
4. Reviewer clicks **Recompute Status** → Application marked Approved/Rejected.  
5. Reviewer downloads **PDF Report** summarizing approved products and suppliers.

---

## 📑 Assumptions

- Excel files follow a fixed schema with headers:  
  `Company | Product | Category | RawMaterial | Supplier`
- Basic validation is implemented, but advanced error handling is out of scope.  
- PDF generation uses `xhtml2pdf` for simplicity (alternative: WeasyPrint).  
- SQLite is used for simplicity; production deployments should use PostgreSQL or MySQL.

---

## ✅ Completed Tasks

- **Task 1**: Core models, migrations, seed data import.  
- **Task 2**: Admin enhancements (filters, search, autocomplete, inline raw materials).  
- **Task 3**: Application workflow (status recompute, PDF export, admin buttons).  
- **Task 4 (Optional)**: Excel file upload + processing into applications. Bugfix in recompute redirect.

---

## 🔮 Future Work

- **Background Tasks**: Queue Excel processing for long-running jobs.  
- **REST API**: Expose endpoints for programmatic submissions.  
- **Customer Portal**: Allow customers to submit applications online.  
- **Process Verification**: Validate input → process → output product chains.  
- **Improved UI/UX**: Dedicated dashboard for reviewers and customer service.

---

## 🛠️ Tech Stack
- **Backend**: Django 5.2.4  
- **Database**: SQLite (default)  
- **Excel Parsing**: `openpyxl`, `pandas`  
- **PDF Export**: `xhtml2pdf`  
- **Autocomplete**: `django-autocomplete-light`
