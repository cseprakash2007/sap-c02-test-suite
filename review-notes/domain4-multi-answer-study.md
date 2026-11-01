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

## 11 of 33 — Q268 — Select TWO — Multi-Region Direct Connect hybrid access and public services

**SOURCE CORRUPTION REPAIRED:** Original JSON incorrectly split external option A into two options A and B, leaving 6 choices and key A,E. Reconstructed original **five-option** source from [FreeCram Q12/355](https://www.freecram.net/question/Amazon.SAP-C02.v2025-07-25.q355/a-company-is-building-a-hybrid-environment-that-includes-servers-in-an-on-premises-data-center-and-in); historical answer now **A,D**. Stored old question/options/answers in originalQuestionSnapshot.

**Historical A,D, but defective architecture.** A Direct Connect gateway connects multiple VPCs in different Regions using **private VIF -> DX gateway -> VGW associations**. D includes a public VIF, which is needed to access public AWS services, but it also requires **Site-to-Site VPN over public VIF to the remote VPCs**, which is unnecessary because the private VIF/DX gateway already provides private routing. Technically clean implementation is one physical DX circuit with private VIF to global DX gateway and each VPC's VGW, plus public VIF for AWS public service IPs. AWS Direct Connect gateway is globally available; not intrinsically located in nearest Region. The private VIF (not the physical DX circuit) associates with the gateway.

**All options:** A best available cross-Region DX gateway; B unnecessary extra circuits/port charges; C VPN over private VIF is not the normal supported AWS-managed Site-to-Site VPN pattern; D public VIF useful but bundled VPN redundant; E inter-Region peering is non-transitive and cannot carry DX-to-peered-VPC traffic. Historical answer A,D should be marked flawed rather than unconditionally correct.

**AWS docs:** https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways-intro.html ; https://docs.aws.amazon.com/directconnect/latest/UserGuide/ ; https://repost.aws/knowledge-center/public-private-interface-dx ; https://repost.aws/knowledge-center/set-up-direct-connect-gateway ; https://repost.aws/knowledge-center/connect-private-network-dx-vif . External original matching variant: https://www.freecram.net/question/Amazon.SAP-C02.v2025-07-25.q355/a-company-is-building-a-hybrid-environment-that-includes-servers-in-an-on-premises-data-center-and-in . A second independent exact external variant was not confirmed.

**674 duplicate audit:** No exact stem duplicate. Related Q96, Q185, Q241, Q301, Q308, Q427 and Q625 use Direct Connect, multi-Region hybrid routing, resilience or transit VIF. Q241 specifically requires transit VIF/BGP for a TGW, unlike this Q268 private VIF/VGW model. Q308 focuses resilience rather than cost and public service access.

**Next:** Q276 — 12 of 33.

### Q268 follow-up independent recheck (2026-11-01)

Multiple independent external mirrors confirmed: [FreeCram 2025 five-option A,D](https://www.freecram.net/question/Amazon.SAP-C02.v2025-07-25.q355/a-company-is-building-a-hybrid-environment-that-includes-servers-in-an-on-premises-data-center-and-in); [FreeCram 2023 malformed six-option A,E](https://www.freecram.net/question/Amazon.SAP-C02.v2023-12-13.q142/a-company-is-building-a-hybrid-environment-that-includes-servers-in-an-on-premises-data-center-and-in); [JPNTest reordered](https://www.jpntest.com/shiken/SAP-C02-mondaishu); [dumps-files split options](https://www.dumps-files.com/downloadfile.html?id=8265). These are mirrors and not independent AWS authority. [AWS remote Region guidance](https://docs.aws.amazon.com/directconnect/latest/UserGuide/remote_regions.html) explicitly describes both DX gateway+private VIF and public VIF+VPN as alternative ways to access remote VPCs; combining them for the same VPCs is redundant. [AWS virtual private gateway associations](https://docs.aws.amazon.com/directconnect/latest/UserGuide/virtualgateways.html) and [VIF types](https://docs.aws.amazon.com/directconnect/latest/UserGuide/WorkingWithVirtualInterfaces.html) validate clean solution. No answer change; historical five-option A,D remains flagged defective, original malformed snapshot preserved.

## 12 of 33 — Q276 — Select THREE — AWS Transit Gateway shared hybrid segmentation

**Original six-option historical key A,B,C retained; DEFECTIVE/AMBIGUOUS SELECT THREE.** A central Transit Gateway shared via AWS RAM (A) + VPC/VPN attachments (B or E) + separate Transit Gateway route tables, associations AND selective propagation (C) is the architectural pattern. B and E redundantly describe the same kind of attachments. B insists on *all* VPCs, which is unnecessary if the company wants selective communication; E is not materially distinguishable as wrong. D VPC peering is operationally poor at this scale and non-transitive. F is mixed: VPC subnet route tables really must point to TGW for applicable CIDRs, but VPNs do not have separate VPC-style route tables; static/BGP VPN routes live in TGW/on-prem network routing. A,B,C is the source key, **not** uniquely valid as a three-choice set.

**Important operational qualification:** The TGW owner must create its Site-to-Site VPN attachment; a VPN already terminating to a virtual private gateway or existing VPC/account is not automatically movable to TGW. Create a suitable TGW VPN connection and plan cutover. Share TGW with organization member accounts by RAM, create participating VPC attachments (at least one subnet/AZ needed for TGW routing), configure TGW isolation tables, association, propagation/static routes, VPC subnet and return routes, BGP customer routes, and security groups/NACLs as appropriate. Disable undesired default association/propagation for strict isolation. TGW is Regional; multiple Regions need further design. Use route tables to allow prod/dev/on-prem reachability without accidental east-west paths. TGW routing is not a firewall.

**External variant verification:** [ExamTopics discussion exact six-option Q340](https://www.examtopics.com/discussions/amazon/view/126768-exam-aws-certified-solutions-architect-professional-sap-c02-topic-1-question-340-discussion/) reports ABC but comments dispute with ACE; [AWS re:Post user discussion six options](https://www.repost.aws/questions/QUvX0QyO3pRQWkBQspwcgVKg/transit-gateway-attachment-configuration) has same duplicated B/E; [Scribd exam mirror six-option source](https://www.scribd.com/document/931431704/AWS-Certified-Solutions-Architect-Professional-SAP-C02-Exam-ExamTopics-301-350) reports ABC (vote 72% ABC, 28% ACE); [FreeCram 2025 five-option PDF](https://www.freecram.net/Amazon.SAP-C02.v2025-04-03.q227.pdf) omits six-option B, and remaps E to generic attachments. Do not transplant answer letters between variants. Exam mirrors and community votes are not AWS technical authority.

**AWS authority:** [Documentation](https://docs.aws.amazon.com/vpc/latest/tgw/working-with-transit-gateways.html); [Documentation](https://docs.aws.amazon.com/vpc/latest/tgw/how-transit-gateways-work.html); [Documentation](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-transit-gateways.html); [Documentation](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpc-attachments.html); [Documentation](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpn-attachments.html). Relevant confirmed facts: RAM cross-account sharing; only TGW owner creates VPN attachments / manages TGW route tables; each attachment associates to one table, can propagate into several; subnet routes are required; TGW table segmentation isolates VPCs.

**674-bank comparison:** Exact normalized stem duplicates: **none**. Closest conceptual matches: **Q136** (new organization-account TGW onboarding), **Q191** (shared-services account TGW attachment), **Q263** (transit-account centralized VPN and shared TGW), **Q354** (remote access to multi-account applications), **Q369** (routing/security within Control Tower multi-account TGW), **Q415** (central networking VPC and on-prem VPN connectivity), **Q540** (default VPC subnet route + central egress TGW). Other related: Q108 centralized outbound governance, Q241 TGW+DX transit VIF BGP, Q301 multi-Region hybrid connectivity, Q360 centralized inspection. Difference is whether the stem tests route-table segmentation, propagation, account onboarding, hybrid VPN, egress/inspection, or DX; do not borrow answer letters.

**Next:** determine 13 of 33 from the source question ordering.

## 13 of 33 — Q321 — Select THREE — PHP/Java/PostgreSQL three-tier replatform

**Historical A,D,F retained; AWS architecture verified with source wording caveat.** A = existing server-side PHP/Apache frontend on EC2 Auto Scaling behind ALB, EFS shared static assets; D = monolithic Java SE on Elastic Beanstalk (less development than Docker/Fargate); F = migrate PostgreSQL data via DMS to Aurora PostgreSQL and autoscale read replicas. B falsely treats dynamic PHP as static SPA, C adds containerization work, E merely vertically scales self-managed PostgreSQL on EC2.

**Critical distinctions:** A 60 TB database is within current Aurora PostgreSQL cluster-volume capacity for supported versions, but per-table limits, source version compatibility, DMS full-load/CDC duration, schema objects and cutover need separate checks. Aurora reader Auto Scaling changes number of replicas, NOT storage size. Application must send reads to reader endpoint. The stem says the database 'reached capacity because of read operations' (ambiguous storage vs read-throughput); replicas address read saturation but not necessarily storage exhaustion. DMS is a migration/replication service, not automatic conversion of every database object. Original wording retained in snapshot.

**External variants:** [SAP-C02 PDF collection, Question 10, matching stem and options](https://cdnc.heyzine.com/files/uploaded/v3/0e2ddf4c8489bd5762075a3d0f0a9ee2193fc36d.pdf). No independently verified second exact exam variant; avoid claiming consensus. **AWS:** https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/java-se-platform.html ; https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Managing.html ; https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_Limits.html ; https://docs.aws.amazon.com/rds/latest/auroraextendedcontent/aurora-features-scalability.html

**674-bank comparison:** No exact normalized-stem duplicate. Closely related Q176 (Java/Tomcat and PostgreSQL migration), Q188 (Elastic Beanstalk with Aurora), Q230 (Aurora PostgreSQL capacity), Q328 (three-tier Java), Q487 (server-side JS three-tier migration), Q525 (RDS PostgreSQL peak demand), Q530 (PostgreSQL ingestion scaling), Q607 and Q667 (three-tier migration). Distinguish frontend language, development-effort constraint, database read vs write vs storage bottlenecks, and whether existing containers are present.

**Next:** Q326 — 14 of 33.

## 14 of 33 — Q326 — Select THREE — RDS MySQL Multi-AZ fast failover

**Historical C,D,E retained; strict <20-second SLO NOT GUARANTEED.** C RDS Proxy minimizes DNS/client reconnection delays; D migrate RDS MySQL to Aurora MySQL; E create cross-AZ Aurora Replica for automatic promotion. A Memcached and B Redis cache reads but do not shorten writer failover; F ordinary RDS MySQL read replica is not an automatic Aurora cluster failover target. In-flight transactions can fail even with proxy; clients need retry/backoff and validation.

**AWS docs:** https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.Failover.html (standard Multi-AZ typically 60–120s); https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraHighAvailability.html (Aurora replicas and proxy); https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy.howitworks.html (connection continuity); https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Replication.html (replica promotion). Aurora typically ~30 seconds, and RDS Proxy can improve failover delays by *up to* 66%; neither is a guaranteed maximum. Measure app-level recovery and test under load.

**Multiple external exact variants:** [Certstopics Q188 C,D,E](https://www.certstopics.com/questions/all-sap-c02-test-inside-amazon-web-services-questions.html); [ExamPractice Q10 C,D,E](https://exampractice.org/examtopics/amazon-exams/aws-certified-solutions-architect-professional-sap-c02); [ExamPal reordered technical C,D,E](https://exampal.app/questions/aws-sap-c02-a-company-is-running-a-critical-application-that-uses-an-amazon-rds-for-mysql-database-to-store-data/); **[DumpsCollection conflicting A,B,F](https://www.dumpscollection.net/downloadfile.html?id=15448)**. External keys are not AWS authority; A,B,F is not a credible fast-failover architecture.

**674-bank comparison:** No exact normalized stem duplicate. Strong match **Q431** (RDS MySQL Multi-AZ failover) — compare its precise goal and answer; related Q287 (RDS app resilience), Q230 (Aurora PostgreSQL scaling), Q525 (RDS PostgreSQL high load). Distinguish standby failover, reader scale-out, proxy connection management and caches; don't transfer answer letters.

**Next:** Q337 — 15 of 33.

## 15 of 33 — Q337 — Select THREE — EKS M6i to Graviton cost optimization

**Verified historical key A,C,E unchanged.** A ensure ARM64-compatible container images; C migrate x86 M6i EKS EC2 nodes to suitable Graviton instances; E purchase EC2 Instance Savings Plan for selected Graviton instance family and Region, sized to stable demand. B nonsensical because EKS already runs containers; D newer x86 not the intended ARM cost path; F x86 family Savings Plan cannot cover Graviton usage. Test multi-arch manifests, native libs, add-ons/DaemonSets, and rolling migration before removing old nodes. AWS docs: https://docs.aws.amazon.com/eks/latest/eksctl/arm-support.html ; https://docs.aws.amazon.com/eks/latest/best-practices/cost-opt-compute.html ; https://docs.aws.amazon.com/savingsplans/latest/userguide/plan-types.html . Savings Plans cover underlying EC2 nodes, not EKS control-plane fee; family+Region lock-in differs from flexible Compute Savings Plans.

**External exact exam variants:** [CertEnsure Q156 A,C,E](https://www.certensure.com/amazon-web-services/sap-c02-cert-practice-test.html); [P2PExams PDF Q4 A,C,E](https://www.p2pexams.com/free-questions/amazon-sap-c02-cheat-sheet-exam-by-deleon.pdf); [JPNTest Q1 reordered options](https://www.jpntest.com/free/SAP-C02-mondaishu-aws-certified-solutions-architect-professional-sap-c02). These exam mirrors may share source material, not independent AWS evidence.

**674-bank duplicate audit:** **Q45 is a near-verbatim shortened duplicate of Q337** with same EKS M6i expiring Savings Plan, Graviton/ARM64 approach, and A,C,E answer. No exact normalized full-stem duplicate due to rewording. Avoid counting Q45 and Q337 as independent knowledge topics. No other direct Graviton/Savings Plan stem matches found by keyword scan.

**Wording caveat:** A pre-existing multi-architecture image need not be rebuilt; 'most recent generation' and new EC2 Instance Savings Plan are not automatically the mathematically cheapest solution without benchmarking, utilization forecast and commitment sizing. Historical A,C,E is the best intended exam answer.

**Next:** Q346 — 16 of 33 (source metadata Select THREE but only four options and two keyed answers; investigate corruption before treating as genuine multi-answer).

## 16 of 33 — Q346 — Select THREE — UDP matchmaking service, NLB, NACL, Shield Advanced

**CORRUPTED SOURCE RESTORED.** Original GitHub had four truncated options A-D, two keyed answers A,D and a Select THREE stem. Preserved original in originalQuestionSnapshot. Restored original six-option version with E = CloudFront+ELB origin and F = Shield Advanced on all public-facing resources. Corrected intended historical key **A,D,F** in original GitHub ordering. External [FreeCram old SAP Professional Q103/147](https://www.freecram.net/question/Amazon.AWS-Solutions-Architect-Professional.v2021-07-21.q147/a-company-hosts-a-game-player-matching-service-on-a-public-facing-physical-on-premises-instance-that) uses reordered letters A=NACL, B=NLB, E=Shield and reports A,B,E. [QuizPlus SAP-C01 Q662](https://quizplus.com/ar-SA/quiz/181452-exam-10-aws-certified-solutions-architect-professional-sap-c01/questions/13536645-a-company-hosts-a-game-playermatching-service-on-a-p) shows the six choices in GitHub A-F ordering. Historical variants share the same stem; do not treat them as independent AWS authority.

**Options:** A NLB correct for UDP but use Route 53 alias to NLB DNS rather than one zonal EIP. B ALB HTTP(S) cannot serve raw UDP. C AWS WAF protects HTTP(S), not NLB UDP. D NACL can restrict protocols but 'block all non-UDP' can break TCP health checks; allow necessary return/health-check traffic, and consider modern NLB security groups. E CloudFront not raw UDP proxy. F Shield Advanced protects supported public NLBs against DDoS. Additional caveat: old on-premises UDP instance must be migrated to suitable AWS targets; AWS 2026 guidance warns direct NLB UDP on-prem IP targets can have return-path problems.

**AWS docs:** https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancers.html ; https://docs.aws.amazon.com/waf/latest/developerguide/web-acl.html ; https://docs.aws.amazon.com/shield/ ; https://aws.amazon.com/blogs/networking-and-content-delivery/routing-udp-to-on-premises-network-load-balancer-targets/ .

**674-bank duplicate audit:** No exact normalized stem duplicate. Closest **Q642** also UDP gaming with NLB, but asks multi-Region global availability and static client IPs, favoring Global Accelerator, not subnet filtering. Q351, Q454 and Q599 use NLB/PrivateLink for different TCP/application connectivity patterns; Q523 uses NLB for EC2 target workload, not game UDP security. Do not borrow option letters.

**Next:** Q350 — 17 of 33.

## 17 of 33 — Q350 — Choose TWO — ECS awsvpc networking and least-privilege task roles

**Verified historical key B,E unchanged.** B use awsvpc mode for per-task ENI/IP and task-specific security groups. E assign SG to tasks and use IAM task roles for least-privilege AWS resource access. A bridge mode can run Linux ECS tasks on EC2 but does not offer direct per-task SG. C instance SG/instance profile scopes privileges to EC2 host, not individual microservice. D passing IAM credentials into containers is an unsafe anti-pattern; ECS task role provides temporary credentials. Separate *task role* (application permissions), *execution role* (ECS agent ECR/logs), and *instance profile* (EC2 host/agent). For EC2-backed tasks, prevent exposure of host IMDS with ECS_AWSVPC_BLOCK_IMDS where applicable. awsvpc task definitions and service SG configuration require a new deployment rather than in-place switching after launch.

**Official AWS docs:** https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-network.html ; https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-iam-roles.html ; https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html ; https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking-awsvpc.html . awsvpc is required for ECS Fargate, recommended for EC2 launch type, and task target groups must use ip target type.

**External exact exam variants:** [ExamsVCE B,E](https://www.examsvce.com/sap-c02/a-company-wants-to-migrate-its-website-question-answer.html); [Pupuweb Question 144](https://pupuweb.com/aws-certified-solutions-architect-professional-sap-c02-actual-exam-question-answer-dumps-2/5/); [Exam-Tests Question 36](https://www.exam-tests.com/SAP-C02-exam/Amazon.SAP-C02.v2025-02-24.q513.html?p=9). Mirrors may copy a shared source; AWS documentation is primary evidence.

**674-bank comparison:** No exact full-stem duplicate; keyword scan identifies Q43 (AWS networking/security around CloudFront and ECS-adjacent design) and Q655 (ECS app networking), but different problem constraints. Compare question intent rather than answer letters. No materially outdated ECS service names; stem chronology 'after deployment' is imprecise because task network mode is selected before task launch.

**Next:** Identify 18 of 33 after Q350 from ordered Domain 4 multi-answer dataset.
