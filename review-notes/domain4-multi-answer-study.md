# Domain 4 multi-answer study — verified question-by-question

Branch: `answer-audit-2026-10-28`. Total multi-answer questions identified in dataset: **33**. Review in ascending original question ID order. Retain full original question/options in `src/data/questions.json`; this file records conclusions and related scenarios.

## 1 of 33 — Q74 — Select THREE — Oracle RDS to PostgreSQL across accounts

**Verified key: A, C, E** (unchanged). Source: Oracle RDS private subnet, target PostgreSQL in another AWS account, existing records and ongoing changes, CNAME cutover.

- **A correct:** Create PostgreSQL target and use AWS Schema Conversion Tool for heterogeneous Oracle schema/code conversion. AWS DMS Schema Conversion is a newer supported alternative.
- **B incorrect:** SCT does not automatically provision a target DB and migrate all data.
- **C correct:** Cross-account VPC peering, routes, security groups, and DNS support private connectivity.
- **D incorrect:** Making Oracle publicly accessible is unnecessary and increases risk.
- **E correct:** AWS DMS full load plus CDC migrates existing and ongoing changes; cut over the Route 53 CNAME after synchronization and validation.
- **F incorrect:** CDC only does not backfill historical rows.

**Caveat:** 'No downtime' is overstated. Engine compatibility, DMS lag, write quiescence, DNS TTL, and existing database connections may require a coordinated cutover. DMS does not migrate all schema/code objects.

**External variants:** [CertsTopics](https://www.certstopics.com/questions/helping-hand-questions-for-sap-c02.html), [ExamsVCE](https://www.examsvce.com/sap-c02/a-company-is-planning-to-migrate-an-39448-question-answer.html) both show A,C,E; [FreeCram](https://www.freecram.net/question/Amazon.SAP-C02.v2026-02-11.q252/a-company-is-planning-to-migrate-an-amazon-rds-for-oracle-database-to-an-rds-for-postgresql-db-instance) uses reordered letters A,B,F for the same solution text.

**AWS sources:** https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2postgresql.html ; https://docs.aws.amazon.com/dms/latest/userguide/instance-profiles-network.html ; https://docs.aws.amazon.com/dms/latest/userguide/schema-conversion.html

**Duplicate assessment:** No confirmed exact same-stem duplicate within the 674-question set in this review. Compare future migration questions by **schema conversion vs data replication**, private connectivity, and **CDC-only vs full load + CDC**, not answer letters.

**Next:** Q106 (2 of 33) — Application Discovery Agent, Migration Hub and EC2 sizing recommendations.

## 2 of 33 — Q106 — Select THREE — On-premises discovery and EC2 right-sizing

**Verified original key A, D, E; no answer-key change.** Original OCR-damaged stem repaired in JSON.

**Scenario:** Windows/Linux physical machines and VMs; collect system config, performance, processes, and network connections; group applications; recommend cost-effective EC2 types.

- **A correct:** AWS Application Discovery Agent runs on supported physical and virtual Linux/Windows servers; collects process/network dependency and utilization data.
- **B incorrect:** Systems Manager Agent manages systems; not the migration-specific discovery agent for all required details.
- **C incorrect:** Systems Manager Application Manager is not the Migration Hub grouping workflow.
- **D correct:** AWS Migration Hub groups discovered servers into applications.
- **E correct:** Migration Hub EC2 instance recommendations match server profile/utilization and estimated cost.
- **F incorrect:** Trusted Advisor does not import on-prem server inventory for EC2 migration recommendations.

**CRITICAL 2026 UPDATE:** AWS Application Discovery Service and AWS Migration Hub stopped accepting **new customers November 7, 2025**. Existing customers can continue existing migration projects. AWS Transform is AWS's recommended successor for new discovery, dependency mapping, assessment, and migration planning. Keep A,D,E for this historical question, but mark it outdated and teach AWS Transform.

**Source variant audit:** CertsTopics, FreeCram, DumpsTech and ExamTopics variants show A,D,E; SPOTO has a B,D,E answer variant that conflicts with AWS documentation on agent responsibilities. Some external versions reorder options; compare solution texts rather than letters.

**Duplicate/similar across all 674:** Q212 is a **strong near-duplicate** (single-answer combined Discovery Agent + Migration Hub); Q56 and Q168 closely related with Strategy Recommendations; Q142/Q264/Q395 test discovery processes/network details; Q266 tests CSV import + EC2 recommendations; Q478/Q537/Q545 focus on migration business cases and Migration Evaluator. No confirmed exact normalized-stem duplicate identified for Q106.

**AWS:** https://docs.aws.amazon.com/application-discovery/latest/userguide/what-is-appdiscovery.html ; https://docs.aws.amazon.com/migrationhub/latest/ug/how-ec2-recommendations-work.html ; https://docs.aws.amazon.com/migrationhub/latest/ug/generating-ec2-recommendations.html ; https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html ; https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/migrationhub-availability-change.html

**External:** https://www.certstopics.com/questions/sap-c02-amazon-web-services-exam-lab-questions.html ; https://www.freecram.net/question/Amazon.SAP-C02.v2025-04-03.q227/a-company-wants-to-migrate-its-workloads-from-on-premises-to-aws-the-workloads-run-on-linux-and-windows ; https://www.dumpstech.com/free-amazon-web-services/sap-c02-practice-6.html ; https://cciedump.spoto.net/exam-questions/prepare-for-sap-c02-exams-questions--study-materials

**Next:** Q116 (3 of 33) — IoT Core, DocumentDB, and Step Functions reporting architecture.

## 3 of 33 — Q116 — Select THREE — MQTT IoT migration, reporting and MongoDB

**Verified key A, D, E (unchanged).** Scenario: MQTT IoT devices every 5 minutes, on-prem MongoDB, periodic 120–600-second report generation, public report access; minimize operational overhead.

- **A correct:** Step Functions coordinates Lambda report-generation tasks; 120–600 seconds fits Lambda's 15-minute per-invocation maximum. Reports in S3 are served by CloudFront.
- **B incorrect:** Lambda polling devices is not a substitute for managed MQTT broker; Lambda layers package dependencies, not message storage.
- **C incorrect:** EKS with EC2 worker nodes and ingress requires more operations than serverless reporting.
- **D correct:** AWS IoT Core accepts device MQTT publish; rules can invoke Lambda to parse, transform, and persist telemetry.
- **E correct:** Amazon DocumentDB offers managed MongoDB compatibility; validate unsupported MongoDB features, driver behavior and indexes.
- **F incorrect:** MongoDB on EC2 leaves OS/DB patching, replication, backups and failover management.

**External variants:** Exact2Pass question #119 matches Q116 with A,D,E. Exact2Pass question #118 and SalesforceXamDumps #31 show same underlying architecture with B,D,E because of option ordering. Compare service content, not letters.

**Duplicate:** **Q438 is a strong near-duplicate**: same MQTT/DocumentDB/Step Functions-S3-CloudFront architecture, answer B,D,E due to reordered options. Similar but distinct: Q228 (IoT Core → Firehose → S3), Q255 (IoT certificates), Q258/Q453 (MongoDB), Q467 (custom MQTT broker overload), Q509 (IoT Core → Kinesis buffering → Fargate), Q583 (vehicle telemetry). **Separate defect candidate:** Q467 stored A uses ALB for raw MQTT; ALB does not directly support raw TCP/MQTT, so re-audit Q467.

**Current-service check:** No confirmed retirement for core correct services. AWS IoT rules can retry and discard on exhausted retries; configure error action/monitoring for production. Ensure IoT rule can invoke Lambda and DocumentDB is compatible with source MongoDB.

**AWS sources:** https://docs.aws.amazon.com/iot/latest/developerguide/iot-create-rule.html ; https://docs.aws.amazon.com/iot/latest/developerguide/lambda-rule-action.html ; https://docs.aws.amazon.com/iot/latest/developerguide/iot-rule-actions.html ; https://aws.amazon.com/lambda/faqs/

**External sources:** https://www.exact2pass.com/sap-c02-aws-certified-solutions-architect-professional-question-8.html ; https://www.salesforcexamdumps.com/sap-c02-practice-questions/3

**Next:** Q119 (4 of 33) — Multi-Region disaster recovery for three-tier applications, Route 53 failover, DynamoDB global tables.

## 4 of 33 — Q119 — Select THREE — Multi-Region three-tier DR with 1-minute RTO

**Verified original answer B, C, E (unchanged).** Original has a minor OCR punctuation defect ("web. application"), corrected to "web, application" in JSON without changing options. The requirement is high availability within each Region, a second-Region hot standby and user-impact-minimizing rapid failover of web, app, and NoSQL tiers.

**Answer-by-answer AWS validation:**

- **A incorrect:** Weighted Route 53 100/0 with 1-hour TTL is not the best primary/secondary automatic failover arrangement; a long TTL can keep stale DNS responses for up to an hour or longer in noncompliant caches.
- **B correct (with caveat):** Route 53 PRIMARY/SECONDARY failover records plus health checking and 30-second TTL are the best offered traffic-switching mechanism. A 30-second TTL alone does **not** guarantee completed failover in <=60 seconds: endpoint health check detection, retry thresholds, recursive/client DNS caching, existing connections and standby readiness contribute to RTO. Consider ARC routing control and rehearse RTO for production.
- **C correct:** DynamoDB global tables continuously maintain Regional replicas for local app access and post-Region-failure service. Default multi-Region eventual consistency (MREC) is async, typically replicating within seconds, but nonzero RPO / conflicts remain possible. AWS introduced multi-Region strong consistency (MRSC) in 2025; evaluate its availability and constraints if zero-RPO/global consistency is required.
- **D incorrect:** 60-minute exports/backups + S3 Cross-Region replication + ad hoc restore suffer stale data and long recovery; unlike global tables, they do not serve as near-live DR replica.
- **E correct:** Keep baseline application/web servers running in Auto Scaling groups across multiple AZs in both Regions. Zonal Reserved Instances cover reliably running minimum and give the matching-AZ capacity reservation; On-Demand instances handle the nonsteady additional load. Note more flexible Savings Plans/On-Demand Capacity Reservations may be better in other modern architectures, but not choices here.
- **F incorrect:** Spot Instances alone are interruptible and cannot guarantee reliable hot-standby capacity for critical 1-minute RTO. Use as optional interruptible overflow only.

**Duplicate audit (entire 674-question JSON checked):** No exact normalized-stem duplicate. Strong **conceptual overlap** with Q182 (multi-Region DynamoDB global tables + Route 53, but its active-active/latency routing is preferred for performance and growth), Q187 and Q79 (active/passive EC2+ALB+Auto Scaling+Route 53 failover), and Q639 (multi-Region DynamoDB and Aurora data-tier DR). Distinct scenario variations: Q27 (DynamoDB global tables + Route 53 with Lambda concurrency), Q242 (looser RPO 2h/RTO 4h favors cheap backups vs global tables), Q341 (ASG at zero + cross-Region RDS replica, <15m RTO), Q464 (CloudFront origin failover beats DNS-origin TTL for fastest origin recovery), Q58 (EC2/RDS DR with 30-sec RPO / 10-min RTO) and Q650 (ECS Fargate + RDS warm standby). Beware superficial cross-question answer conflicts: required objectives, stateful database, and traffic-routing needs differ.

**External variant:** Matching stem and the exact A–F option wording confirmed at [CertEnsure](https://www.certensure.com/amazon-web-services/sap-c02-cert-practice-test.html). A second independently verified exact exam variant was **not located**, so do not claim multi-site consensus. The recommendation rests primarily on AWS official documentation, not answer dumps.

**AWS documentation:** [Route 53 failover record values](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values-failover.html) · [Health check detection](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html) · [DynamoDB global tables design](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-global-table-design.html) · [DynamoDB + Route 53 RTO considerations](https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-global-tables/route-53-request-routing.html) · [EC2 zonal RI capacity](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ri-limits.html) · [ARC routing control](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.html).

**2026 audit verdict:** Original B,C,E is the best available combination, but "fail over in 1 minute" is a technically overconfident claim if based only on DNS TTL; retain exam key and flag caveat. No service in the selected options is obsolete.

**Next:** Continue the next multi-answer Domain 4 question in ascending ID order (5 of 33); confirm its ID directly from the 674-question dataset.

## 5 of 33 — Q169 — Select TWO — EKS multi-node, Inspector scanning and multiprotocol shared storage

**Verified B,E (unchanged).** B: multi-node EKS with managed Prometheus/Grafana and ECR enhanced scanning; E: FSx for NetApp ONTAP supporting NFS and SMB persistent volumes through Trident CSI. A fails HA due to one worker node; C self-hosts monitoring on EC2; D requires two separate storage platforms (EFS + FSx Windows), adding overhead. No core selected service is retired.

**2026 implementation warnings:** Distribute EKS nodes across AZs and deploy FSx ONTAP Multi-AZ. ECR enhanced scanning examines stored images, not all runtime vulnerabilities. Managed Prometheus/Grafana do not automatically satisfy application logging: configure a log pipeline. NetApp Trident SMB PV support requires Windows nodes and ontap-nas; SMB is not supported through the Trident EKS add-on. EKS integration requires appropriate CSI driver setup.

**674-bank duplicate check:** No exact normalized-stem duplicate found. Related Q320 (FSx for NetApp ONTAP multiprotocol storage) and Q482 (Grafana availability/operations), but they test different architectures.

**External exam:** [Solution2Pass exact Q169 wording and B,E](https://www.solution2pass.com/Amazon-Web-Services/SAP-C02-question-answers.html). No independently confirmed second exact variant; do not claim consensus.

**AWS/NetApp:** https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/supported-fsx-clients.html ; https://docs.aws.amazon.com/eks/latest/userguide/fsx-ontap.html ; https://docs.netapp.com/us-en/trident-2602/trident-use/trident-fsx.html ; https://aws.amazon.com/blogs/containers/optimize-log-management-for-amazon-eks-with-amazon-fsx-for-netapp-ontap/

**Next:** Q189 — 6 of 33.

## 6 of 33 — Q189 — Select THREE — 540 accounts moving between AWS Organizations

**Historical key B,E,F retained; CRITICAL OUTDATED SELECT THREE.** B = source management account calls RemoveAccountFromOrganization; E = new management account invites with InviteAccountToOrganization; F = invited member accepts (AcceptHandshake). Current AWS Organizations supports **direct member-account transfer** via E and F without B; no three mandatory options exist. A is not a valid cross-organization MoveAccount API; C wrongly calls management-only RemoveAccountFromOrganization from member account (member-initiated departure uses LeaveOrganization); D placeholder account is unnecessary.

**Migration safeguards:** Destination organization at least 7 days old, newly created source member accounts at least 4 days old, compatible Seller of Record, quotas and permissions; review SCP/RCP/IAM organization ID conditions, delegated admin, root access, historical billing reports, and stale management-account IAM roles. A direct transfer can avoid temporary standalone billing/policy exposure.

**674-question comparison:** No exact stem duplicate. Related Q25, Q33, Q192, Q213, Q282 and Q325 address organization/account migration or account management but have distinct requirements. External exact stem/answers: https://www.examsvce.com/sap-c02/a-company-uses-aws-organizations-to-manage-75551-question-answer.html (B,E,F). Independent second exact exam variant not confirmed. Official: https://docs.aws.amazon.com/organizations/latest/userguide/orgs_account_migration.html ; https://docs.aws.amazon.com/organizations/latest/APIReference/API_RemoveAccountFromOrganization.html ; https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_invites.html

**Next:** Q190 — 7 of 33.

## 7 of 33 — Q190 — Select THREE — Enterprise migration discovery and readiness

**Historical answer A,D,F verified. OUTDATED FOR NEW CUSTOMERS.** A Application Discovery Service inventories servers, configurations, performance and dependencies; D CART assesses organizational adoption readiness; F Migration Hub groups applications and tracks migration progress. B SMS is a legacy migration execution tool; C X-Ray traces instrumented requests; E Inspector finds vulnerabilities.

**2026 critical change:** AWS Application Discovery Service and AWS Migration Hub stopped accepting new customers **November 7, 2025**. AWS Transform is the recommended successor for new discovery, dependency mapping, assessment, cost estimation and wave planning. Existing projects may continue. CART is a readiness assessment, not a precise AWS cost estimator. Source question's cloud resource cost estimation requirement is only partly served by A,D,F; use AWS Transform assessments / AWS Pricing Calculator for detailed costs.

**Independent exam variants:** [Cloud Study Exams Q10](https://cloudstudyexams.com/aws-certified-solutions-architect-professional-1-10/) A,D,F; [SAP-C02 collection Q208](https://www.dumpscollection.net/downloadfile.html?id=14113) A,D,F. **AWS:** https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html ; https://docs.aws.amazon.com/migrationhub/latest/ug/migrationhub-availability-change.html ; https://docs.aws.amazon.com/prescriptive-guidance/latest/evaluating-migration-readiness/introduction.html

**674 question duplicate/similarity audit:** No exact normalized-stem duplicate. Strong conceptual overlaps Q56, Q106, Q168, Q212, Q142, Q264, Q266, Q395 (discovery, utilization, dependencies and migration planning). Q478/Q537/Q545 address business case, cost, Migration Evaluator and broader VMware inventory. Compare each question's discovery versus assessment versus actual execution requirement; don't equate different answer letters.

**Next:** Determine Q191+ multi-answer sequence from dataset (8 of 33).

## 8 of 33 — Q241 — Select TWO — Direct Connect transit VIF bidirectional BGP

**Verified B,C (unchanged).** B advertises on-premises CIDRs via BGP over the transit VIF toward AWS. C advertises AWS-side allowed prefixes from the Direct Connect gateway toward on-premises. A is false because a 1 Gbps transit VIF is supported; D/E configure MACsec link encryption, not reachability. Direct Connect gateway allowed-prefix lists control the AWS advertisements on transit gateway associations. Configure the transit VIF, DX gateway-TGW association, TGW/VPC routes and BGP session; AWS re:Post states 100 on-prem routes per transit VIF BGP session is a hard quota.

**Source defect:** Corrected original C typo 'Adverse' -> 'Advertise'; original stem/options/answers preserved in originalQuestionSnapshot. Singular 'account VPC' awkward but not answer-changing. No obsolete service.

**External matching exam variants:** https://www.freepdfdumps.com/Amazon.SAP-C02.v2025-06-02.q210.html?p=22 (Q102, B,C); https://www.dumpstech.com/free-amazon-web-services/sap-c02-practice-4.html (B,C). **AWS official:** https://docs.aws.amazon.com/directconnect/latest/UserGuide/WorkingWithVirtualInterfaces.html ; https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-transit-gateways.html ; https://docs.aws.amazon.com/vpc/latest/tgw/tgw-dcg-attachments.html ; https://repost.aws/knowledge-center/direct-connect-fix-connectivity-to-vpc

**674-question duplicate audit:** No exact normalized stem duplicate. Related Q96 (DX/TGW connectivity), Q185 (hybrid network), Q268 (hybrid), Q301 (multi-region), Q308 (single DX resiliency), Q427 (hybrid DX), Q625 (DX networking). Their objectives differ; do not transfer B,C without checking routing-vs-redundancy-vs-encryption requirements.

**Next:** Q248 — 9 of 33.

## 9 of 33 — Q248 — Select TWO — Legacy inline security inspection using Gateway Load Balancer

**Historical exam answer A,D (unchanged), with serious wording caveats.** A: deploy compatible legacy security virtual appliances on EC2 Auto Scaling instances across AZs. D: Gateway Load Balancer is correct technology for transparent inline L3/L4 packet inspection. **DEFECT:** D says provision a separate GWLB *for each AZ*, whereas AWS normally uses **one multi-AZ GWLB plus a zonal Gateway Load Balancer endpoint (GWLBe) per AZ**. Set symmetric ingress/egress routing through endpoints, GWLB targets and appliance ASG. Appliance must support GENEVE UDP 6081 encapsulation; 15-year-old tool with no vendor cloud product might not work on EC2. The claim of no application performance impact is unrealistic because inspection introduces latency.

**Distractors:** B NLB distributes app traffic, not all-IP inline inspection; C ALB is HTTP(S) application routing, not inline packet inspection; E TGW is relevant for centralized *multi-VPC* inspection but unnecessary for this single-VPC architecture.

**External exact variants:** [FreeCram Q88/183](https://www.freecram.net/question/Amazon.SAP-C02.v2023-11-04.q183/a-financial-company-is-planning-to-migrate-its-web-application-from-on-premises-to-aws-the-company-uses) A,D; [FreePDFDumps](https://www.freepdfdumps.com/Amazon.SAP-C02.v2023-09-29.q103.html?p=13) A,D; AWS re:Post discusses ambiguity: https://www.repost.aws/questions/QUC5JQ72irRHSpIpDoAr0HYw/third-party-security-tool-integration . **AWS official:** https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/introduction.html ; https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/getting-started.html ; https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-load-balancer-endpoints.html ; https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/inspecting-inbound-traffic-fa.html

**674-question comparison:** No exact duplicate. Q360 is centralized multi-VPC inspection where TGW may be necessary; Q375 is shared-services AWS Marketplace firewall with appliances + GWLB + GWLBe, different topology and answer A,C,F. Related Q521 (web app deployment) and Q625 (DX) are not the same inspection scenario. Similar framework can lead to different answers because the number of VPCs and need for centralized routing differ.

**Next:** Q249 — 10 of 33.

## 10 of 33 — Q249 — Select TWO — VMware application and SQL Server VM low-downtime rehost

**Historical answer A,D; RETIRED SERVICE WARNING.** A and D both select AWS SMS incremental VMware VM replication (SQL Server VM and application VM). SMS was discontinued March 31, 2022; historical SMS snapshot replication ran no more frequently than hourly, so its RPO was not near-zero. **Current 2026:** AWS Transform MGN (formerly AWS Application Migration Service, renamed June 2026) continuously replicates blocks and orchestrates testing and cutover of both VMs. Use Direct Connect private replication networking and validate supported OS, per-disk/per-server limits, SQL crash/application consistency, licensing, EBS target design and synchronized application/database cutover.

**Distractors:** B VM Import/Export is a one-time app VM image import; C Snowball Edge device shipment/offline transfer is not continuous and 10 Gbps DX is available; E DMS replication to RDS can provide low database downtime but changes target architecture and does not itself rehost SQL Server VM. 500 TB at 10 Gbps theoretical minimum ~4.63 days to seed, not 4.63 days application downtime; verify actual sustained bandwidth and per-disk limitations.

**Multiple external exam variants:** [PassTest Q153 reordered](https://www.passtest.jp/articles/2025%E5%B9%B404%E6%9C%88%E5%AE%9F%E9%9A%9B%E3%81%AB%E5%87%BA%E3%82%8Bsap-c02%E8%A9%A6%E9%A8%93%E5%95%8F%E9%A1%8C%E9%9B%86%E3%81%AB%E3%81%AF%E6%AD%A3%E7%A2%BA%E3%81%A7%E6%9B%B4%E6%96%B0%E3%81%95%E3%82%8C%E3%81%9F%E5%95%8F%E9%A1%8C-q152-q170/); [FreePDFDumps Q99 reordered](https://www.freepdfdumps.com/Amazon.SAP-C02.v2024-09-24.q208.html?p=21); [Scribd Q311 original A,D](https://www.scribd.com/document/1030319491/SAP-C02-Dg-Re-Vh8uyt); [Examlex Q297 original A,D](https://theexamlex.work/exams/181452-exams-10-aws-certified-solutions-architect-prof/28). Verify answer by option content, not letters across sites.

**Official AWS:** https://aws.amazon.com/blogs/mt/accelerate-your-migration-with-aws-application-migration-service/ ; https://aws.amazon.com/application-migration-service/ ; https://docs.aws.amazon.com/transform/latest/userguide/transform-vmware-migrate-servers.html ; https://docs.aws.amazon.com/mgn/latest/ug/MGN-service-limits.html ; https://aws.amazon.com/blogs/architecture/field-notes-choosing-a-rehost-migration-tool-cloudendure-or-aws-sms/

**674-question duplicates:** No exact duplicate. Similar Q44/Q324 VMware server rehost; Q92/Q217/Q560 database-only migration and DMS/RDS; Q259 massive bulk data transfer with Snowball; Q190 discovery and planning, not execution; Q536 replication scenario. Different requirements can justify different services/answers.

**Next:** Q268 — 11 of 33.
