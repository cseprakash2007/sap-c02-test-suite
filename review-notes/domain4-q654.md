# Domain 4 Q654 — question 137/139

**CORRECTED ANSWER: B (original source key C is technically invalid).** Reviewed 2026-11-01. Original stem and four option texts retained in questions.json.

## Full original question
A company has applications in an AWS account that is named Source. The account is in an organization in AWS Organizations. One of the applications uses AWS Lambda functions and store’s inventory data in an Amazon Aurora database. The application deploys the Lambda functions by using a deployment package. The company has configured automated backups for Aurora. The company wants to migrate the Lambda functions and the Aurora database to a new AWS account that is named Target. The application processes critical data, so the company must minimize downtime. Which solution will meet these requirements?

## All original options and review
- **A:** Download the Lambda function deployment package from the Source account. Use the deployment package and create new Lambda functions in the Target account. Share the automated Aurora DB cluster snapshot with the Target account.
  - **Incorrect:** Lambda redeploy is valid, but automated Aurora cluster snapshots cannot be shared directly. Copy automated snapshot to a manual snapshot first.
- **B:** Download the Lambda function deployment package from the Source account. Use the deployment package and create new Lambda functions in the Target account Share the Aurora DB cluster with the Target account by using AWS Resource Access Manager {AWS RAM). Grant the Target account permission to clone the Aurora DB cluster.
  - **CORRECT:** Lambda deployment package recreates functions in Target. AWS RAM shares Aurora cluster for quick cross-account copy-on-write cloning.
- **C:** Use AWS Resource Access Manager (AWS RAM) to share the Lambda functions and the Aurora DB cluster with the Target account. Grant the Target account permission to clone the Aurora DB cluster.
  - **Incorrect:** RAM supports Aurora cluster sharing but does **not** support sharing Lambda functions. Lambda resource-based policies grant invocation/access, not migration/ownership transfer.
- **D:** Use AWS Resource Access Manager (AWS RAM) to share the Lambda functions with the Target account. Share the automated Aurora DB cluster snapshot with the Target account.
  - **Incorrect:** Both RAM Lambda sharing and direct automated-snapshot sharing are unsupported.

## Operational caveats
- An Aurora clone is a point-in-time independent database, NOT ongoing replication. For minimal data loss, coordinate a write freeze/final sync and cutover; consider CDC if near-zero downtime and continued writes are required.
- Encrypted Aurora clusters require source KMS customer-managed key permissions; default AWS managed RDS key blocks cross-account cloning.
- Recreate Lambda triggers, event source mappings, IAM execution roles, environment variables, VPC config and aliases in Target; deployment package alone does not recreate all settings.

## Independent external exam comparison
- FreeCram SAP-C02 Q264: keys **C** but its explanation describes **B** — internally contradictory.
- P2PExams SAP-C02 Marquez PDF: keys **C** but its explanation describes **B** — internally contradictory.
- Pupuweb SAP-C02: keys **B**, consistent with AWS documentation.
- No confirmed Choose TWO/THREE variant.
- Source OCR/format errors: `store’s` for `stores`, option B missing sentence period and `{AWS RAM)`.

## AWS primary sources
- https://docs.aws.amazon.com/ram/latest/userguide/shareable.html
- https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Clone.Cross-Account.html
- https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-share-snapshot.html
- https://docs.aws.amazon.com/lambda/latest/dg/permissions-function-cross-account.html

## External exact-stem sources
- https://www.freecram.net/question/Amazon.SAP-C02.v2026-03-31.q264/a-company-has-applications-in-an-aws-account-that-is-named-source-the-account-is-in-an-organization
- https://www.p2pexams.com/free-questions/braindumpscollection-amazon-sap-c02-exam-dumps-by-marquez-18-01-2024-6qa.pdf
- https://pupuweb.com/aws-certified-solutions-architect-professional-sap-c02-actual-exam-question-answer-dumps-1/3/

## Additional independent verification (2026-11-01)
- SpotO 2026 compilation also keys **B** for this exact question: https://cciedump.spoto.net/exam-questions/free-aws-sap-c02-practice-questions-answers-2026-part1
- ExamTopics community-archived copy has **B** and records a large majority vote for B (secondary evidence, not AWS authority): https://ro.scribd.com/document/927890359/AWS-Certified-Solutions-Architect-Professional-SAP-C02-Exam-ExamTopics-51-75
- FreeCram continues to publish **C** despite describing the B workflow: https://www.freecram.net/question/Amazon.SAP-C02.v2026-03-31.q264/a-company-has-applications-in-an-aws-account-that-is-named-source-the-account-is-in-an-organization
- The competing answer keys do **not** establish a Choose TWO/THREE variant; the verified originals show one requested solution with A–D alternatives. A separately repaginated or reordered version may use a different option letter: compare option content rather than letters.
- AWS verifies that `rds:Cluster` can be shared via RAM for cross-account cloning; Lambda functions are absent from the RAM shareable-resource catalog: https://docs.aws.amazon.com/ram/latest/userguide/shareable.html
- Clone setup uses `restore-db-cluster-to-point-in-time` with `--restore-type copy-on-write`; create DB instances separately. Cross-account clone is not continuous data synchronization. Default AWS-managed RDS KMS key cannot support cross-account clones: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Clone.Cross-Account.html
- AWS explicitly requires copying an **automated** Aurora snapshot to a **manual** snapshot before sharing: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-share-snapshot.html
- **Review result:** Existing Q654 `answers:["B"]`, explanations, status and defect warnings are correct. No question-data edit required; original question and options intentionally preserved for fidelity.
