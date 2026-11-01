# Domain 4 multi-answer study — verified question-by-question

Branch: `answer-audit-2026-10-28`. Total multi-answer questions identified in dataset: **33**. Review in ascending original question ID order. Retain full original question/options in `src/data/questions.json`; this file records conclusions and related scenarios.

## 1 of 33 — Q74 — Select THREE — Oracle RDS to PostgreSQL across accounts

**Verified key: A, C, E** (unchanged). Source: Oracle RDS private subnet, target PostgreSQL in another AWS account, existing records and ongoing changes, CNAME cutover.

- **A correct:** Create PostgreSQL target and use AWS Schema Conversion Tool for heterogeneous Oracle schema/code conversion. AWS DMS Schema Conversion is a newer supported alternative.
- **B incorrect:** SCT does not automatically provision a target DB and migrate all data.
- **C correct:** Cross-account VPC peering, routes, security groups, and DNS support private connectivity.
- **D incorrect:** Making Oracle publicly accessible is unnecessary and increases risk.
- **E correct:** AWS DMS full load plus CDC migrates existing and ongoing changes; cut over the Route 53 CNAME after synchronization and validation.
- **F incorrect:** CDC only does not backfill historical rows.

**Caveat:** 'No downtime' is overstated. Engine compatibility, DMS lag, write quiescence, DNS TTL, and existing database connections may require a coordinated cutover. DMS does not migrate all schema/code objects.

**External variants:** [CertsTopics](https://www.certstopics.com/questions/helping-hand-questions-for-sap-c02.html), [ExamsVCE](https://www.examsvce.com/sap-c02/a-company-is-planning-to-migrate-an-39448-question-answer.html) both show A,C,E; [FreeCram](https://www.freecram.net/question/Amazon.SAP-C02.v2026-02-11.q252/a-company-is-planning-to-migrate-an-amazon-rds-for-oracle-database-to-an-rds-for-postgresql-db-instance) uses reordered letters A,B,F for the same solution text.

**AWS sources:** https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2postgresql.html ; https://docs.aws.amazon.com/dms/latest/userguide/instance-profiles-network.html ; https://docs.aws.amazon.com/dms/latest/userguide/schema-conversion.html

**Duplicate assessment:** No confirmed exact same-stem duplicate within the 674-question set in this review. Compare future migration questions by **schema conversion vs data replication**, private connectivity, and **CDC-only vs full load + CDC**, not answer letters.

**Next:** Q106 (2 of 33) — Application Discovery Agent, Migration Hub and EC2 sizing recommendations.
