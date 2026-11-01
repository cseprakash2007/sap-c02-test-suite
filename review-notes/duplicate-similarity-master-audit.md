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
