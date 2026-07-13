---
source: TrueVow_Platform_Analytics_Service/.opencode/skills/reporting/SKILL.md
service: TrueVow_Platform_Analytics_Service
type: analytics
stack: ["python", "fastapi"]
imported: 2026-06-30T22:32:05.310006+00:00
skill_name: reporting
---
---
name: reporting
description: Report generation and export for analytics data.
---

# Reporting

## Overview
This skill covers report generation and data export capabilities for the Platform Analytics Service.

## When to Use
- Adding new report types
- Implementing data export functionality
- Creating scheduled reports
- Adding report templates

## Implementation Steps
1. Define report schema and output format
2. Create report generation function
3. Add export endpoint (CSV, JSON, PDF)
4. Implement caching for expensive queries
5. Add report scheduling if needed
6. Test report output matches expected format

## Validation Checklist
- [ ] Report schema is defined
- [ ] Export format is supported (CSV/JSON)
- [ ] Query is optimized for large datasets
- [ ] Pagination is implemented for large reports
- [ ] Error handling for failed exports
- [ ] Response headers set correctly for downloads

## Files to Modify
- `app/api/v1/endpoints/` — New report endpoints
- `app/aggregations/workers/` — Report generation workers
- `app/services/` — Report service layer
