# Domain 4 Q616 — question 129/139

**Verified answer D (equivalent to C in external longer variant).** Reviewed 2026-11-01. Original shortened question and all options preserved in questions.json.

## Requirements
Migrate selected Oracle databases, retain other Oracle databases on-premises for compliance, support spatial data and cron maintenance, and query retained Oracle tables as foreign tables from AWS.

## All options
- **A incorrect:** DynamoDB/S3/Athena/Lambda do not meet foreign-table Oracle access or relational spatial/cron requirements.
- **B incorrect:** SQL Server and Glue crawlers do not expose live Oracle foreign tables.
- **C incorrect:** EC2-hosted Oracle lift-and-shift adds server operations; MGN does not provide database CDC or Oracle FDW.
- **D correct:** SCT converts Oracle schema; DMS migrates data; RDS PostgreSQL supports PostGIS spatial features, pg_cron database scheduling, oracle_fdw foreign Oracle tables; Direct Connect supplies hybrid network connectivity.

## Technical caveats
- Direct Connect is network transport only; oracle_fdw performs Oracle foreign-table queries. Configure route tables, security, Oracle listener, permissions and user mapping.
- Check exact RDS PostgreSQL engine version for PostGIS, pg_cron and oracle_fdw extension compatibility.
- SCT/DMS do not automatically convert every Oracle PL/SQL routine or scheduled job.

## External variant and defects
- SAP-C02 PDF question 73 has the full-length stem and four longer choices. The PostgreSQL architecture is **option C there**, equivalent to **D here**. Its answer line says C, while its explanation mistakenly calls it D.
- Repository Q616 has severe missing spaces and abridged wording, including omission of explicit PostGIS and pg_cron. Preserve original for traceability, flag for source reconstruction.
- No verified Choose TWO/THREE variant.

## References
- https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/postgresql-oracle-fdw.html
- https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.Extensions.foreign-data-wrappers.html
- https://docs.aws.amazon.com/AmazonRDS/latest/PostgreSQLReleaseNotes/postgresql-extensions.html
- https://myportal.utt.edu.tt/ICS/icsfs/d97df75f-867e-411a-ac5f-e13435c2eedc.pdf?target=c53e5228-7ce9-4ef5-a5ec-d932dc3abaad
