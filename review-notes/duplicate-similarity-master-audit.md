# SAP-C02 674-question duplicate, similarity and answer-conflict audit

**Branch:** `answer-audit-2026-10-28`  
**Dataset:** `src/data/questions.json` (674 questions)  
**Audit date:** 2026-11-01  
**Scope:** Pairwise normalized question-stem and option-word similarity; preliminary screening, followed by focused technical review of high-risk pairs.

## Executive summary

- 674 questions scanned across all four domains.
- 26 candidate pairs passed preliminary similarity thresholds; these are **candidates**, not 26 confirmed duplicates. Screening can miss paraphrased duplicates.
- Eight pairs have identical normalized stems (Q69/113, Q82/412, Q99/557, Q124/397, Q133/632, Q139/243, Q389/637, Q446/565).
- Two source answer keys were corrected and committed: **Q333 D → A** and **Q565 A → B**.
- **Q510** has been flagged `needs-source-reconciliation`; its B,D,E answer has *not* been changed.
- A different option letter is not necessarily a different solution (Q40 B versus Q303 D).

## High-priority answer conflicts and corrections

| Questions | Original answers | Outcome | Why |
|---|---|---|---|
| Q446 / Q565 | B / A | **Corrected Q565 to B** | Identical environmental-data ingestion scenario; ALB cannot target SQS, but API Gateway HTTP API can integrate with SQS, and Lambda can consume from the queue |
| Q82 / Q333 / Q412 | A / D / A | **Corrected Q333 to A** | S3 buckets must be emptied before CloudFormation deletes them. `DeletionPolicy: Delete` does not empty a bucket; Lambda custom resource is appropriate |
| Q40 / Q303 | B / D | **Same selected solution**, no key change | Both select launch-template attribute-based instance-type selection; the letters differ because option order differs |
| Q9 / Q510 | A,D,E / B,D,E | **Q510 flagged; unresolved** | DRS private replication, staging subnet internet access, dedicated connectivity, and bandwidth constraints are different and must not be conflated |
| Q363 / Q492 | B / B | Likely wording/branding variant | Kinesis Data Firehose is now Amazon Data Firehose; Splunk delivery architecture is similar |

## Q9 vs Q510 — detailed comparison

| Requirement | Q9 | Q510 |
|---|---|---|
| AWS Elastic Disaster Recovery | Yes | Yes |
| Private/dedicated replication connection | Explicitly dedicated | Avoid public internet, but dedicated link not explicitly required |
| Public application access prohibited | Yes | Yes |
| Bandwidth constraint | Explicit 75% maximum | Must preserve bandwidth for other applications |
| Stored answer | A,D,E | B,D,E |
| Review | Compare source variants | **Flagged ambiguous; no speculative correction** |

Q9 option E explicitly combines private replication with bandwidth throttling. Q510 option E only selects private-IP replication and **does not explicitly throttle**. Q510 option B proposes public staging subnets; a public subnet does not *automatically* make the recovery application internet-accessible, but private recovery subnet design and replication routing require independent verification. Option A offers private staging subnets and NAT gateways and may be more defensible, but this has **not** been established as a definitive correction. The available options do not completely resolve the stated bandwidth requirement. Do not silently equate Q9 and Q510.

## High-confidence duplicates and wording variants

| Pair | Domain(s) | Classification / observation |
|---|---|---|
| Q69 / Q113 | 1 | Exact duplicate; same answers C,D |
| Q82 / Q412 | 3 | Same question, OCR defects (`S3` rendered `53`); A |
| Q99 / Q557 | 1 | Same stem; minor option OCR differences; B |
| Q124 / Q397 | 3 | Same SageMaker scenario; product naming updated; A |
| Q133 / Q632 | 3 | Same Lambda deployment scenario; minor text differences; A |
| Q139 / Q243 | 1 | Same CloudWatch Logs aggregation scenario; A,C,E |
| Q389 / Q637 | 1 | Exact duplicate; EC2 Instance Connect; C |
| Q446 / Q565 | 3 / 1 | Same stem and options; conflicting original keys corrected to B |
| Q73 / Q383 | 2 / 3 | Elasticsearch Service vs OpenSearch Service naming; A |
| Q363 / Q492 | 4 | Kinesis Data Firehose vs Amazon Data Firehose naming; B |
| Q440 / Q651 | 2 | Ticket-sale scaling scenario; D |
| Q404 / Q611 | 1 | Organizations/CloudFormation StackSets scenario; C |
| Q216 / Q265 | 3 | Similar EC2 cost-anomaly alert scenarios; B |
| Q68 / Q277 | 3 | CloudFormation Retain policy variants; A |
| Q399 / Q660 | 3 | Market-data processing with Firehose, AWS Batch Spot; B |
| Q140 / Q225 | 3 | SSM Agent and IAM role troubleshooting; A,B |
| Q32 / Q83 | 3 | S3 multipart upload expiration and lifecycle; C,E |
| Q16 / Q342 | 3 | Aurora Serverless v2 and Compute Savings Plans; D |
| Q306 / Q445 | 4 | Transfer Family, Glue, S3 and SQS scenario; C |
| Q143 / Q504 | 4 | Storage Gateway Volume Gateway cache mode; C |

## Related scenarios that must NOT automatically be merged

- **Q124/Q397 vs Q271:** SageMaker Git repository authentication versus CodeArtifact/PyPI dependency access; different tasks and solutions.
- **Q82/Q412 vs Q333:** same nonempty-bucket deletion problem; Q333 was miskeyed, not a genuinely different solution.
- **Q9 vs Q510:** DRS private connectivity and bandwidth constraints differ.
- **Q40 vs Q303:** same solution with differently ordered answer choices.
- **Q446 vs Q565:** same question with genuinely conflicting original solutions; resolved by AWS technical constraints.

## AWS rules for exam study

1. **ALB target groups** support instance, IP, and Lambda target types; SQS is not an ALB target. Use API Gateway → SQS to buffer bursty ingestion.
2. **CloudFormation and S3:** a bucket must be empty before stack deletion. `DeletionPolicy: Delete` alone cannot delete a nonempty bucket.
3. **AWS DRS:** separate replication network path (VPN/Direct Connect/private IP), staging subnet design, recovery instance exposure, and bandwidth throttling. They solve different requirements.
4. **Answer letters are not identities:** compare selected *option text* after normalizing option order.
5. **Service rebrands and OCR:** Amazon Elasticsearch Service → OpenSearch Service, Kinesis Data Firehose → Amazon Data Firehose, `S3` ↔ OCR `53`; do not mistake naming changes for architecture changes.

## AWS documentation

- [CloudFormation S3 bucket deletion](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3-bucket.html)
- [ALB target groups](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html)
- [API Gateway HTTP API service integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations.html)
- [DRS data routing](https://docs.aws.amazon.com/drs/latest/userguide/data-routing.html)
- [DRS network requirements](https://docs.aws.amazon.com/drs/latest/userguide/Network-Requirements.html)
- [DRS network preparations](https://docs.aws.amazon.com/drs/latest/userguide/Network-Settings-Preparations.html)

## GitHub change history

- [Q333/Q565 answer-key corrections](https://github.com/cseprakash2007/sap-c02-test-suite/commit/0c394cf45ebda67c6108590fad7f7cb241806cdc)
- [Initial duplicate/conflict audit notes](https://github.com/cseprakash2007/sap-c02-test-suite/commit/023467ccbf5f3b3529e8b1334364e3491d29973e)
- [Q510 review flag](https://github.com/cseprakash2007/sap-c02-test-suite/commit/5e1d1dcae38d1c3559c41b7a5e24dd2ef9c2fa9d)
- [Q9/Q510 focused comparison](https://github.com/cseprakash2007/sap-c02-test-suite/commit/59e375581522cab92c102f8bd0cea74e598229e3)

## Follow-up checklist

- [ ] Independently reconcile Q510 against AWS DRS documentation and exact external question variants.
- [ ] Inspect all 26 candidate pairs manually; classify exact duplicate, equivalent wording, related but different, or false positive.
- [ ] Compare full answer text, not only letters, for every pair.
- [ ] Audit additional paraphrased duplicates that lexical similarity screening can miss.
- [ ] Add React practice-site filters for `duplicate`, `related-but-different`, and `conflicting-answer`; preserve original IDs.
- [ ] Do not remove questions or alter uncertain answer keys without independent technical verification.

**Status:** Reference audit only. Corrected keys Q333 and Q565 are already committed; Q510 remains intentionally unresolved.

## Follow-up audit: similar problems with different AWS frameworks and integration patterns (2026-11-01)

| Questions | Shared business problem | Architecture / framework distinction | Classification |
|---|---|---|---|
| Q40 / Q303 | Spot instance launch failures | Attribute-based instance type selection via launch template, selected B versus D because option order differs | Equivalent solution; duplicate-like |
| Q363 / Q492 | Near-real-time network telemetry to Splunk | CloudWatch Logs subscriptions → Kinesis Data Firehose (renamed Amazon Data Firehose) → Splunk | Service rebrand; equivalent |
| Q306 / Q445 | Managed SFTP ingestion and file transformation | Transfer Family + S3 event + Glue transformation + SQS completion message | Equivalent architecture; Q306 is abbreviated |
| Q124 / Q397 | Private Git repository access from isolated SageMaker notebook | SageMaker Git repository settings and Secrets Manager credentials | Same scenario, renamed SageMaker AI; **network reachability still needs independent validation** |
| Q271 vs Q124/Q397 | Package or source access from isolated SageMaker | PyPI dependencies → CodeArtifact with public:pypi upstream and interface endpoint; Git source → repository credentials and network route | Similar setting, different dependency type; **not duplicates** |
| Q16 / Q342 | Highly variable Lambda/Fargate workload with write-heavy Aurora MySQL | Aurora Serverless v2 + Compute Savings Plans | Equivalent solution; check savings plan applies to Lambda/Fargate compute, not Aurora Serverless capacity |
| Q143 / Q504 | iSCSI block volumes with local low-latency cache and backup | Storage Gateway **cached volume gateway**, not file/tape gateway | Equivalent solution |

### Framework and integration lessons

- **Git source vs package repository:** Git credentials (Secrets Manager) do not by themselves provide private network connectivity. CodeArtifact can proxy PyPI packages and be accessed via VPC endpoints; it does not replace arbitrary Git source connectivity.
- **Firehose rebranding:** `Amazon Kinesis Data Firehose` and `Amazon Data Firehose` describe the same managed delivery service; check whether the question also changes transformation, routing or destinations.
- **Event-driven transfer:** S3 event notifications triggering processing plus Glue and SQS is different from an EFS cron job or EMR cluster, even if the outcome is file transformation.
- **EC2 scaling:** Attribute-based instance type selection diversifies available Spot capacity; changing answer letter does not change the solution.
- **Savings Plans:** Compute Savings Plans cover eligible Lambda and Fargate usage; Aurora Serverless v2 charges separately. Avoid reading the selected answer as if Compute Savings Plans discount Aurora.
- **Storage Gateway:** Cached Volume Gateway supports iSCSI block volumes with local caching; File Gateway and Tape Gateway serve different interfaces and use cases.

### Follow-up items

- [ ] Verify whether Q124/Q397 private Git host is reachable without internet and whether Secrets Manager-only answer is technically sufficient.
- [ ] Investigate additional *cross-framework* lookalikes beyond lexical matches: ALB vs API Gateway, SQS vs Kinesis, Step Functions vs EventBridge, Glue vs EMR, RDS vs DynamoDB, and ECS/Fargate vs Lambda.
- [ ] Preserve distinct question IDs and record why a change in requirement changes the recommended service.

## Cross-framework candidate scan — second pass (2026-11-01)

A keyword co-occurrence scan of all 674 question stems and options found the following *study candidates* (not validated duplicate counts): SQS/Kinesis 9; Step Functions/EventBridge 17; Glue/EMR 5; RDS/DynamoDB 29; Fargate/Lambda 29. API Gateway/ALB produced zero in this literal-token scan because the query required the exact hyphenated `api-gateway` string; **this is a search limitation, not evidence that there are no such questions**.

### Cross-framework study groups to inspect

| Questions | Topic | Key decision criteria | Status |
|---|---|---|---|
| Q194, Q222, Q661 | Long-running or custom data processing | Lambda 15-minute execution limit; Fargate container support; Step Functions orchestration vs EventBridge triggering | Candidate grouping; inspect full stems before judging equivalence |
| Q306, Q445, Q524 | Glue versus EMR | Managed ETL and event-driven transformations vs Hadoop/EMR processing | Q306/Q445 equivalent; Q524 distinct scenario |
| Q22, Q347, Q671 | RDS, DynamoDB and migration | Relational features, licensing, schema compatibility, read/write patterns | Related topics only; not duplicates |
| Q23, Q42, Q446, Q565 | Queuing and streaming | SQS buffering for asynchronous work vs Kinesis for ordered streaming/replay | Q446/Q565 confirmed duplicate and corrected |
| Q61, Q183, Q194, Q196 | Event orchestration | EventBridge event routing/schedules vs Step Functions workflow state, retries and callbacks | Requires case-by-case validation |

### Audit safeguards

1. Co-occurrence of two service names in answer options is **not** proof of equivalent questions.
2. Compare business requirements, latency, runtime, data consistency, operational overhead, and exact correct option text.
3. A service mentioned only as a distractor does not define the question's architecture.
4. Do not auto-correct answer keys based on similarity alone.
5. Continue investigating Q510, Q124/Q397 Git reachability, and further cross-framework variants.

## Focused cross-framework review: long-running jobs and SQS vs Kinesis (2026-11-01)

### Q194 / Q222 / Q661

| ID | Workload | Stored key | Finding |
|---|---|---|---|
| Q194 | Abbreviated question: infrequent S3 uploads, processing up to 25 minutes | A | **Abbreviated duplicate of Q222**; EventBridge → ECS Fargate task |
| Q222 | Full S3 survey upload scenario, existing EC2 polling, 25-minute processing | A | Same solution as Q194; S3 events → EventBridge → ECS Fargate task |
| Q661 | Proprietary unmodifiable Linux binary, CPU-intensive, runs up to 20 minutes every four hours | C | **Related but different**: EventBridge schedule → Fargate task; not S3-event triggered |

**Exam rule:** Lambda's maximum invocation duration is 15 minutes. A Step Functions Task state's timeout of 30 minutes does **not** allow a Lambda function to run for 30 minutes. Fargate can run containerized work longer than 15 minutes. For Q661, a container image can package the binary without modifying its source. AWS Batch is another viable batch framework but the proposed Step Functions schedule is not itself a scheduling mechanism.

### Q23 / Q42 / Q446 / Q565

| ID | Requirement | Stored key | Classification |
|---|---|---|---|
| Q23 | Bursty, loosely coupled order jobs to DynamoDB | B | SQS + Lambda worker; distinct scenario |
| Q42 | Continuous genomic records, parallel near-real-time analytics, Redshift destination | B | Kinesis Data Streams; distinct streaming scenario |
| Q446 | Bursty REST API with no lost messages | B | HTTP API → SQS → Lambda; duplicate of Q565 |
| Q565 | Same environmental-data ingestion scenario as Q446 | B (corrected from A) | Confirmed duplicate; same architecture |

**Exam rule:** SQS durably buffers independent asynchronous jobs; Kinesis Data Streams is optimized for continuous ordered-within-shard records, multiple consumers, and replay. API Gateway can integrate with SQS; an ALB cannot target an SQS queue. Reliability also requires retries, DLQ/redrive strategy, and idempotent processing where applicable.

### Reference documentation

- [Lambda timeout limits](https://docs.aws.amazon.com/lambda/latest/dg/configuration-timeout.html)
- [EventBridge targets and ECS tasks](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html)
- [S3 to EventBridge events](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ev-events.html)
- [API Gateway HTTP API integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations.html)
- [SQS and Lambda](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html)
- [Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/introduction.html)

**Dataset status:** No answer-key changes in this focused review; Q194 and Q222 identified as abbreviated/full duplicates, Q661 as related-but-different.
