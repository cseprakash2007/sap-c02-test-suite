# Domain 4 Q636 — question 133/139

**DISPUTED SOURCE KEY A.** Repository answer A retained for traceability; **B better fits TCO**, but automatic Migration Hub import is unverified. Reviewed 2026-11-01. Original stem and options remain unchanged in questions.json.

## Original scenario
On-premises virtual Microsoft workloads, existing Site-to-Site VPN, SNMP on VMs, no additional on-prem VMs or source software, require TCO report AND automatically imported Migration Hub discovery data.

## Option review
- **A (source key, disputed):** Application Migration Service agentless migration plus Strategy Recommendations does not document the specified SNMP-based TCO report or automatically importing source discovery into Migration Hub. Strategy Recommendations focuses on strategy.
- **B (best TCO match, incomplete):** Windows EC2 Migration Evaluator agentless collector can reach SNMP/WMI sources over VPN, avoids new on-prem VMs and agents, and Migration Evaluator produces TCO reports. However automatic import into Migration Hub is not demonstrated.
- **C wrong:** Misattributes TCO report generation to Migration Hub rather than Migration Evaluator.
- **D wrong:** Migration Readiness Assessment does not discover SNMP servers or produce the detailed TCO business case.

## Cross-site key disagreement
- CertEnsure SAP-C02 Q67: **A**, same as repository A.
- DumpsReview Q219: **D**, equivalent to repository A.
- FreeCram question 217/355: **A**, equivalent to repository **B**.
- No confirmed Choose TWO/THREE variant.
- Multiple missing punctuation marks; typo `VMs m`.

## AWS documentation
- https://aws.amazon.com/migration-evaluator/faqs/
- https://aws.amazon.com/migration-evaluator/features/
- https://aws.amazon.com/compare/migration-evaluator-and-migration-hub/
- https://docs.aws.amazon.com/migrationhub/latest/ug/gs-new-user-discovery.html
- https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-import.html
- https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/getting-started-deploy.html

## External exam sources
- https://www.certensure.com/amazon-web-services/sap-c02-cert-practice-test.html
- https://www.freecram.net/question/Amazon.SAP-C02.v2025-07-25.q355/a-company-wants-to-migrate-virtual-microsoft-workloads-from-an-on-premises-data-center-to-aws-the-company
- https://www.dumpsreview.com/articles/guide-new-2024-actual-amazon-sap-c02-exam-questions-q214-q233/

## Recommendation
Flag as defective/ambiguous in study UI, do not teach source A as confidently verified. Distinguish TCO (Migration Evaluator) from Migration Hub discovery/tracking. A complete answer would need documented automated data integration into Migration Hub in addition to TCO generation.
