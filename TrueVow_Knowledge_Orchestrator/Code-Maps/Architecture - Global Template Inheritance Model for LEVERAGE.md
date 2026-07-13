---
category: architecture
title: "Global Template Inheritance Model for LEVERAGE"
importance: 9
tags: ["leverage", "templates", "inheritance", "saas-admin", "architecture"]
file_paths: []
created: 2026-06-25T02:17:55.747030+00:00
updated: 2026-06-25T02:17:55.747030+00:00
memory_id: 531a8312-6343-46f1-8e4d-6a203acc17fb
---

# Global Template Inheritance Model for LEVERAGE

SaaS Admin stores global rule templates in the centralized DB. Law firms inherit templates via tenancy_id. Firms can customize inherited templates without affecting the global version. Template versioning: SaaS Admin publishes v1.0, firms can lock to specific version or auto-update. Schema: leverage_global_templates (id, template_json, version, effective_date, practice_area, jurisdiction).

---
**Category:** `architecture` | **Importance:** 9/10
**Files:** N/A
