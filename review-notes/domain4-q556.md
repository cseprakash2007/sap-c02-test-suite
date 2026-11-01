# Domain 4 Q556 — single-answer question 120/139

**Source answer A invalid as written. B is best literal option, but question is ambiguous and C also meets explicit requirements.** Full original question and options preserved in questions.json.

## Options
- **A incorrect:** Amazon DocumentDB is MongoDB-compatible but uses collections and managed cluster storage, not 'tables with Provisioned IOPS volumes'; instance endpoint ties client to a specific instance and is poor failover default.
- **B best conditional choice:** DynamoDB on-demand scales automatically; gateway endpoint allows same-VPC private EC2 to connect without internet/NAT and has no extra endpoint charge; TLS encrypts DynamoDB API traffic. **But** MongoDB app must be rewritten/remodeled for DynamoDB.
- **C technically valid alternative:** DynamoDB interface endpoints are fully supported and also enable private encrypted access and on-demand scaling, but add endpoint charges and client configuration. No explicit cost criterion makes B uniquely correct.
- **D incorrect as written:** DocumentDB cluster endpoint is the recommended endpoint and preserves MongoDB compatibility, but 'tables with Provisioned IOPS volumes' is not valid DocumentDB storage terminology. A corrected D with managed storage, TLS and appropriate scaling would be plausible if MongoDB API compatibility is mandatory.

## Defects and variants
Source keys **A**; Certsmania PDF repeats A with false claims about DocumentDB Provisioned IOPS and cluster endpoint replica load balancing. FreeCram Q19/171, Exam-Tests Q318, ExamTopics Q890 and Scribd Q252 have exact or near-exact stems. No verified Choose TWO/THREE version. Missing punctuation after 'database'. Recommend flagging this item as defective/underspecified, not a clean single-answer question.

## AWS documentation
- https://docs.aws.amazon.com/documentdb/latest/devguide/endpoints.html
- https://docs.aws.amazon.com/documentdb/latest/devguide/how-it-works.html
- https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-ddb.html
- https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/privatelink-interface-endpoints.html
- https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/on-demand-capacity-mode.html
- https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/network-isolation.html

## External practice copies
- https://www.freecram.net/question/Amazon.SAP-C02.v2024-03-21.q171/a-company-is-migrating-a-legacy-application-from-an-on-premises-data-center-to-aws-the-application-uses
- https://www.exam-tests.com/SAP-C02-exam/Amazon.SAP-C02.v2025-02-24.q513.html?p=65
- https://www.examtopics.com/discussions/amazon/view/80192-exam-aws-certified-solutions-architect-professional-topic-1-question-890-discussion/
- https://www.certsmania.com/pdf/amazon-web-servicesquestion-answer-preparation-changed-sap-c02-questions-by-frederic.pdf

Reviewed 2026-11-01.