# Domain 4 Q560 — question 121/139

**Corrected answer: C. Original source key: B (defective).** Original stem/options remain unchanged in questions.json.

## Verification
AWS Prescriptive Guidance explicitly recommends native SQL Server **transactional replication** with Amazon RDS for SQL Server as a **push subscriber** for minimal-downtime migrations. Initial snapshot then ongoing source changes are replicated; validate, pause writes briefly, wait for replication catch-up, cut over applications. See https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/trans-rep.html .

## Options
- **A wrong:** MGN is server rehosting, SCT schema conversion; post-cutover export to Aurora does not ensure continuous sync.
- **B wrong despite original key:** DMS full load/CDC to **S3** creates data and change files; a subsequent load to RDS is not an automatically continuously synchronized RDS target. Direct DMS full-load+CDC to RDS would work but is absent.
- **C best:** native SQL Server transactional replication to RDS SQL Server subscriber, followed by validated low-downtime cutover. Distinguish transactional replication from generic Always On HA.
- **D wrong:** MGN can rehost to EC2, but RDS SQL Server cannot attach manually detached MDF/LDF files from EC2 as proposed.

## Defects / exam context
Stem OCR `SOL Server` -> `SQL Server`. 'Modern data architecture' is ambiguous: RDS SQL Server is managed replatforming, not heterogeneous engine modernization; Aurora PostgreSQL with schema conversion and direct DMS CDC would better meet engine modernization. External exact-stem CertifHub Q7 keys native replication (its option C, same as dataset C despite other options reordered). No confirmed Choose TWO/THREE variant.

## References
- https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/trans-rep.html
- https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/methods.html
- https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html
- https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.Targets.html
- https://blog.certifhub.com/aws/aws-certified-solutions-architect-professional-english/q7/

Reviewed 2026-11-01.