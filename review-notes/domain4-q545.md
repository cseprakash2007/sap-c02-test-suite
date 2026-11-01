# Domain 4 Q545 — single-answer question 119/139

**Verified historical answer: C.** Original stem/options retained in `src/data/questions.json`.

## Option analysis
- **A incorrect:** Systems Manager Patch Manager is for patch management; installing a collector per guest VM is not the agentless approach; high utilization alone does not justify excluding workloads.
- **B incorrect:** Manual CSV review adds operational overhead, discards high-utilization servers without justification, and AWS SMS ended support April 1, 2023.
- **C intended correct:** Migration Evaluator's agentless collector collects VMware VM inventory and utilization; review inactive workloads as candidates for retirement and plan cost-effective migration. **Defect:** AWS FAQ says install collector on a **separate Windows Server VM** and use VMware vSphere interfaces, **not on the ESXi hypervisor**.
- **D incorrect:** Application Migration Service agent per VM plus Redshift/QuickSight is for migration and custom analytics, not lowest-overhead inventory discovery.

## Lifecycle and data-quality flags
AWS Migration Hub stopped accepting new customers November 7, 2025; AWS Transform is the modern replacement for new migration assessments. AWS SMS ended support April 1, 2023. AWS recommends 2–4 weeks of VMware collection for TCO and 2–6 weeks for migration planning. Inactive servers require owner validation before retirement. Stem typo `Knowledge` -> `knowledge`.

## External variants
FreeCram Q101/264, Exam-Tests Q343, CertEnsure and Scribd reproduce the exact single-answer question and answer C. No verified Choose TWO/THREE variant.

## Official sources
- https://aws.amazon.com/migration-evaluator/faqs/
- https://docs.aws.amazon.com/migrationhub/latest/ug/migrationhub-availability-change.html
- https://docs.aws.amazon.com/transform/latest/userguide/transform-app-assessments.html
- https://docs.aws.amazon.com/application-discovery/latest/userguide/agentless-collector-gs-vcenter-details.html
- https://docs.aws.amazon.com/general/latest/gr/full_shutdown_services.html

## External sources
- https://www.freecram.net/question/Amazon.SAP-C02.v2026-03-31.q264/a-company-wants-to-migrate-to-aws-the-company-is-running-thousands-of-vms-in-a-vmware-esxi-environment
- https://www.exam-tests.com/SAP-C02-exam/Amazon.SAP-C02.v2025-02-24.q513.html?p=70
- https://www.certensure.com/amazon-web-services/sap-c02-cert-practice-test.html

Reviewed 2026-11-01.