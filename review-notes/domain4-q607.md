# Domain 4 Q607 — question 127 of 139

**Answer B independently verified.** Original stem and all four source options preserved in `src/data/questions.json`; reviewed 2026-11-01.

## Exam scenario and interpretation
Three-tier on-premises application: Java frontend in VMs, TensorFlow recommendation model on a physical server, and on-premises SQL Server storing profiles. Migrate to AWS with the **least operational overhead**.

## Verified answer — B
- Export the model to **Amazon S3**, deploy a compatible TensorFlow inference container and trained artifacts to a **SageMaker AI endpoint**. Set IAM permissions and network integration.
- Deploy Java app to **AWS Elastic Beanstalk** (Java SE/Tomcat).
- Use **AWS DMS** to migrate data from on-prem SQL Server to **Amazon RDS for SQL Server**.
- Integrate user-profile access and model invocation securely. The stem does not define the detailed request/DB integration.

## Each original answer choice
- **A — Incorrect:** AWS SMS is a **legacy/outdated migration offering**, and rehosting physical ML/application servers does not provide managed model inference or the least ongoing operations.
- **B — Correct:** Managed ML serving, managed Java deployment, managed relational DB and migration minimize operations.
- **C — Incorrect:** AWS Application Migration Service (MGN) is a lift-and-shift tool. Self-managed EC2 application/model servers and SQL Server on EC2 require more patching, backups, monitoring, database and operating system management.
- **D — Incorrect:** EKS managed node groups still entail Kubernetes, container, workload and node lifecycle management; no Kubernetes-specific need stated. RDS in this option is a good managed choice, but B is lower-overhead overall.

## Source and variant audit
Same scenario appears as FreeCram SAP-C02 **Topic 3 Q889** and in the ITDumpsKR SAP-C02 practice test. Question numbering differs, but both present this as a single-answer architecture-choice scenario; **no verified Choose TWO/THREE variant**. Original answer B corroborated by AWS documentation. Do not treat third-party answer keys as AWS authority.

## Defects and caveats
- Stem typo `onpremises` should read `on-premises`.
- Option B punctuation typo `{AWS DMS)` should be `(AWS DMS)`.
- Option D omits punctuation before `Host the node groups`.
- **AWS Server Migration Service (AWS SMS)** is legacy nomenclature; AWS Application Migration Service is the modern lift-and-shift option.
- SageMaker hosting requires model packaging, compatible TensorFlow inference image/code, IAM role and secure VPC/database integration. Its endpoint does not automatically understand how to read SQL Server profiles. 
- Original question and options kept byte-for-byte for audit traceability.

## AWS official documentation
- https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model-get-started.html
- https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-inference-code.html
- https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_Java.html
- https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SQLServer.html
- https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.SQLServer.html

## External exam question references
- https://www.freecram.com/discussions/Amazon/exam-sap-c02-topic-3-question-889-discussion-p1333148.html
- https://www.itdumpskr.com/AWS-Solutions-Architect-Professional-practice-test.html
