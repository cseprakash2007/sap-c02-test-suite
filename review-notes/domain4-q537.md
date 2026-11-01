# Domain 4 Q537 — question 117 of 139

**Original historical answer: C. Single-answer. 2026 status: verified, but outdated services.** Full original question and options preserved in `src/data/questions.json`.

## Explanation
- **A wrong:** AWS SMS ended support April 1, 2023; DMS handles database migration, Service Catalog provisions governed products rather than discovering dependencies.
- **B wrong:** AWS Application Migration Service migrates servers, Storage Gateway supports hybrid storage rather than discovering app/database dependencies.
- **C historically correct:** Migration Evaluator inventories and measures workloads and generates a business case; Migration Hub visualizes portfolio; Application Discovery Service identifies dependencies. Sample at least one month to capture month-end batch jobs.
- **D wrong:** Control Tower sets up AWS landing zones, not on-premises discovery. SMS is retired.

## 2026 defects and update
AWS Application Discovery Service and AWS Migration Hub stopped accepting new customers November 7, 2025. AWS Transform is recommended for new discovery and dependency mapping. The original C is the only historical best answer but is not fully viable for a new customer in 2026. Option C typo: `anunderstanding` -> `an understanding`. SMS in A and D retired 2023.

## External variants
- Scribd SAP-C02 Q164: exact stem, C.
- scalar.usc.edu SAP-C02 Q208: exact stem, shuffled options, D refers to the same Migration Evaluator solution.
- No confirmed Choose TWO/THREE version.

## References
- https://aws.amazon.com/migration-evaluator/features/
- https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-tools/discovery-migration-evaluator.html
- https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html
- https://aws.amazon.com/about-aws/whats-new/2025/10/aws-service-availability/
- https://docs.aws.amazon.com/general/latest/gr/full_shutdown_services.html
- https://www.scribd.com/document/1030319491/SAP-C02-Dg-Re-Vh8uyt
- https://scalar.usc.edu/works/race-and-migration-in-the-united-states-/pass-guaranteed-quiz-useful-amazon---exam-sap-c02-overviews

Reviewed 2026-11-01.