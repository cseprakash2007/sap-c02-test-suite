# Domain 4 Q528 — question 116/139

**Verified answer: A (single-answer).** Original stem/options preserved in `src/data/questions.json`.

## Reason
AWS DocumentDB's documented cross-version migration procedure creates a new target cluster, exports/imports indexes using DocumentDB Index Tool, uses AWS DMS **Migrate and replicate** for initial full load and ongoing CDC via change streams, verifies data and cuts over the DNS endpoint.

## Options
- **A correct:** isolated target permits validation while writes continue and CDC tracks changes.
- **B incorrect:** binary dump/import alone lacks continuous replication.
- **C incorrect for scenario:** in-place MVU is supported, but causes production downtime and cannot validate the new version in isolation before applications use it.
- **D incorrect:** DataSync is not a DocumentDB database CDC migration tool.

## Defects / caveats
- 24-hour change-stream retention must be long enough to cover full load.
- Monitor DMS errors and CDC latency; quiesce writes, let replication catch up, validate before Route 53 cutover; account for TTL and existing client connections.
- Configure DMS target preparation to **Do nothing** to preserve imported indexes.
- Amazon DocumentDB 8.0 and in-place major upgrades exist; option C is not inherently an unsupported service, just fails this scenario.
- Exact-option practice copies found on ExamCollection and Certstopics. No independently confirmed Choose TWO/THREE variant.

## References
- https://docs.aws.amazon.com/documentdb/latest/devguide/docdb-migration.versions.html
- https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.DocumentDB.html
- https://docs.aws.amazon.com/documentdb/latest/devguide/docdb-mvu.html
- https://docs.aws.amazon.com/documentdb/latest/devguide/migration-quick-start.html
- https://www.examcollection.us/exam/SAP-C02-question-answer-3.html
- https://www.certstopics.com/questions/sap-c02-vce-exam-download.html

Reviewed 2026-11-01.