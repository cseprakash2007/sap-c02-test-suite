# Domain 4 Q646 — question 135/139

**Answer D verified as intended, with substantial wording and migration caveats.** Original full stem and all options preserved in questions.json. Reviewed 2026-11-01.

## Original question
A company is migrating a large on-prem Oracle database (withstored procedures) to AWS. The solution must usemanaged services, behighly available, and enable afast migrationwithminimal downtime.

- A. Use AWS DMS to replicate data to RDS for Oracle. Store database files in S3.
- B. Use backup and restore into EC2-hosted Oracle cluster.
- C. Use DMS to move data to DynamoDB. Recreate stored procedures in Lambda.
- D. Use DMS to migrate toAmazon Aurora PostgreSQL. UseAWS SCTto convert stored procedures.

## Every option
- **A incorrect as written:** RDS for Oracle is managed, and DMS can replicate Oracle data, but RDS Oracle database files are not stored in customer S3 buckets. A correctly specified Oracle-to-RDS Oracle migration may minimize code changes.
- **B incorrect:** EC2 Oracle cluster requires self-management; backup/restore can cause extended downtime for large DB.
- **C incorrect:** DynamoDB is not a drop-in relational Oracle replacement; PL/SQL-to-Lambda rewrite is significant rearchitecture.
- **D intended correct:** AWS SCT converts Oracle schema and many stored procedures to PostgreSQL-compatible code; DMS full-load and CDC minimize cutover downtime; Aurora PostgreSQL is managed and highly available.

## Technical caveats and defects
- SCT cannot automatically translate every Oracle PL/SQL feature; assess and manually remediate unsupported procedures/packages. Update/test application SQL, drivers and behavior.
- DMS transfers data and ongoing changes; it does not automatically convert all procedural code.
- The question does not explicitly require changing engines; Oracle-to-PostgreSQL may take more work than a well-designed homogeneous Oracle-to-RDS Oracle migration. D is best of offered choices, not universally the fastest migration.
- AWS DMS Schema Conversion is a newer managed alternative to downloadable SCT; neither is obsolete.
- Original stem has no question sentence and severe spacing defects: withstored, usemanaged, behighly, afast, migrationwithminimal; option D has toAmazon, UseAWS, SCTto.

## Source comparison
- ExamCollection SAP-C02 Q22 reproduces exact abbreviated stem/options, answer **D**.
- A second independent exact-stem exam-site match was not established.
- No confirmed Choose TWO/THREE variant.

## Official AWS sources
- https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-oracle-database-to-aurora-postgresql-using-aws-dms-and-aws-sct.html
- https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/heterogeneous-migration.html
- https://docs.aws.amazon.com/dms/latest/userguide/CHAP_SchemaConversion.html
- https://aws.amazon.com/dms/faqs/

## External exam source
- https://www.examcollection.us/exam/SAP-C02-question-answer-2.html
