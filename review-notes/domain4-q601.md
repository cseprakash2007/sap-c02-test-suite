# Domain 4 Q601 — question 126/139

**Answer C verified.** Original stem and options preserved in `src/data/questions.json`.

## AWS verification
Amazon MemoryDB is a fully managed durable Redis OSS/Valkey-compatible in-memory primary database with microsecond reads, single-digit-ms writes, Multi-AZ transaction log and automatic failover. AWS MemoryDB FAQs state unplanned failover typically completes in under 20 seconds; replica promotion generally resumes writes in seconds. It supports large datasets with sharding. Successful primary writes are durably logged across AZs before acknowledgment; primary reads are strongly consistent, replica reads eventually consistent. Snapshots can be exported to S3 for downstream analytics, but the question does not explicitly define a live analytics pipeline.

## All options
- **A not best:** ElastiCache Redis OSS with cluster mode is cache-oriented; no configured durable primary storage or Multi-AZ automatic failover. New June 2026 durability applies to **ElastiCache for Valkey**, not this stated Redis OSS option.
- **B incorrect:** Standard RDS + read replica does not offer microsecond leaderboard reads, and read replica alone is not automatic writer failover.
- **C correct:** MemoryDB Multi-AZ meets low-latency reads/writes, durable TB-scale data, fast primary failover and low operational overhead.
- **D incorrect:** Self-managed Redis on EC2 requires management of patching, replication, failover, monitoring and backups. S3 backups do not provide sub-minute writer failover.

## External / variant verification
Exact-stem single-choice copies: FreeCram SAP-C02 Topic 2 Q739 and PracticeCF No.1490. No confirmed Choose TWO/THREE variant. No retired services. **2026 nuance:** AWS added optional Multi-AZ durability for ElastiCache **Valkey** in June 2026 and now recommends considering it for new single-Region durable workloads; it does not change this original question's C answer.

## Official references
- https://aws.amazon.com/memorydb/faqs/
- https://docs.aws.amazon.com/memorydb/latest/devguide/what-is-memorydb.html
- https://docs.aws.amazon.com/memorydb/latest/devguide/autofailover.html
- https://docs.aws.amazon.com/memorydb/latest/devguide/consistency.html
- https://docs.aws.amazon.com/memorydb/latest/devguide/related-services-choose-between-memorydb-and-redis.html
- https://aws.amazon.com/blogs/database/announcing-durability-for-amazon-elasticache/

## External references
- https://www.freecram.com/discussions/Amazon/exam-sap-c02-topic-2-question-739-discussion-p1330600.html
- https://www.examtopics.cn/exam-aws-certified-solutions-architect-professional-2

Reviewed 2026-11-01.