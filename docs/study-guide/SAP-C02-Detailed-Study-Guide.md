# SAP-C02 Deep Learning Notes — Concepts Behind the 674 Questions

> **Source:** [674-question dataset](../../src/data/questions.json), branch `answer-audit-2026-10-28`; [all-question index](./SAP-C02-All-674-Question-Index.md).
>
> **Audit caveat (31 October 2026):** The data contains 674 records: 150 domain 1, 55 domain 2, 297 domain 3 and 172 domain 4. Most stored answer keys have **not** been independently verified. This is a **conceptual study guide based on recurring question patterns**, not a certification that every recorded key is correct. Do not memorize disputed or outdated answers. The original SAP-C02 exam is administered through **16 November 2026**, followed by SAP-C03 from **17 November 2026**; confirm which exam you booked.
>
> This guide is organized by related concepts rather than source question order. Use the [question index](./SAP-C02-All-674-Question-Index.md) to connect every original QID to a primary topic. Read a lesson, attempt its related questions without looking at the key, and return to the lesson to explain **why the other options fail**.

## 1. How to solve SAP-C02 scenarios

The exam is not primarily a dictionary test. It gives a business requirement and four or more architectures. Identify **what must not change**, **what must improve**, and **what trade-off decides the answer**. Translate phrases: *lowest operational overhead* → managed service; *near-zero RPO* → synchronous or continuously replicated data; *existing code must not change* → compatible interface or rehost; *private connectivity* → endpoint, PrivateLink, VPN or Direct Connect depending on direction; *cross-account governance* → Organizations guardrail plus IAM/resource permission.

Use a five-pass method: (1) circle hard constraints, (2) name the AWS service capability required, (3) eliminate options that violate even one hard constraint, (4) compare remaining options by cost/operational burden, (5) check if answers are technically possible but not the **best** fit. A plausible service name is not enough. Always distinguish *what a service can do* from *what it is designed to do*.

**Worked thought process:** A company has a cross-account policy requirement for every current and future account. Adding IAM policies manually to each account is not a strong organization-wide guardrail. Consider SCPs/RCPs and automated account provisioning—but remember a guardrail alone does not grant access.

## 2. Organizations, SCPs, RCPs and IAM

Think of AWS Organizations as a company office building. Each **account** is a room, each **OU** groups rooms, **SCPs** impose maximum actions principals can perform, and **RCPs** apply resource-centric boundaries. An IAM identity policy is a person's permission slip; a resource policy is the permission posted on a resource. The effective permission is constrained by applicable boundaries and any explicit deny. **SCPs do not grant API permissions**. SCPs generally do not restrict principals in the organization's management account; plan stronger management-account protection separately.

Cross-account pattern: in Account B create a role whose **trust policy** allows a principal in Account A; the source principal must also be allowed to call `sts:AssumeRole`. The assumed role then uses its own identity permissions. Resource policies can instead grant direct access for supported services such as S3, subject to other policy evaluation rules. **IAM Identity Center** centralizes workforce access; **AWS RAM** shares supported resources, not arbitrary IAM rights; **Control Tower** sets up account governance and landing zones.

**Example:** A developer in Account A needs read-only access to S3 in Account B. An AssumeRole workflow requires the trust relationship in B, permission to assume in A, read permission on the role in B, and any bucket/KMS policy permissions needed.

**Trap:** An SCP that says `Allow s3:GetObject` does not itself make S3 objects readable. **Learn:** policy intersection, explicit deny, organizations root/OU inheritance, delegated administration.

AWS: https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html and https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html

## 3. Network foundation: VPC, subnets and routing

A VPC is a logically isolated network, a **subnet** is an IP range in one Availability Zone, and a **route table** chooses the next hop. An **internet gateway** enables public-internet routing for appropriately addressed public-subnet resources; it is not a NAT gateway. A **NAT gateway** allows privately addressed instances to initiate outbound IPv4 connectivity without unsolicited inbound internet connections. For resiliency, deploy NAT gateways in each active AZ and route each private subnet to a same-AZ NAT as appropriate.

**Security groups** are stateful allow rules attached to network interfaces; **network ACLs** are stateless subnet-level allow/deny rules. Remember return traffic needs explicit NACL allowances, whereas a security group's stateful behavior automatically accounts for return packets. A public subnet has a route toward the IGW, but an EC2 instance also needs a public IPv4 address or suitable IPv6 configuration to reach the internet directly.

**Example:** Three-AZ app: public ALB, app EC2 in private subnets, separate data subnets, and one NAT per AZ. The app can download updates through NAT; the database remains private. For private S3 access, add a **gateway VPC endpoint** instead of routing every S3 request through NAT.

**Trap:** Merely placing a NAT gateway in a VPC does not route traffic through it. Verify each subnet's route table. **Learn:** asymmetric routing, AZ failure domains, source/destination checks, IPv6 egress-only IGW.

AWS: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html

## 4. Transit Gateway, Direct Connect, VPN and Cloud WAN

A **transit gateway (TGW)** is a regional routing hub for many VPCs and on-premises networks. VPC peering is a direct VPC-to-VPC path and **is not transitive**. For hundreds of VPCs, a hub can be simpler, but examine data-processing charges and route domain separation. **AWS Cloud WAN** provides policy-driven global networking across Regions; it is not just a replacement spelling for TGW.

**Site-to-Site VPN** encrypts connectivity over IP networks and can be established relatively quickly, but internet conditions can affect consistency. **Direct Connect (DX)** provides a dedicated private physical connection and generally more consistent network experience; it does not automatically encrypt traffic. Use VPN over DX or another encryption layer if required. A private VIF targets VPC connectivity using a VGW or DX gateway; a transit VIF is for DX gateway-to-TGW connections. A public VIF is for supported public AWS endpoints, not for directly attaching a VPC private subnet.

**Example:** 100 VPCs across five accounts need on-premises connectivity. Central network account + TGW sharing via RAM reduces point-to-point complexity. If international sites need a global policy overlay, evaluate Cloud WAN.

**Trap:** A DX circuit is not itself a VPN and not necessarily encrypted. **Learn:** BGP, route propagation, overlapping CIDRs, TGW route tables, DX Gateway.

AWS: https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html and https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html

## 5. PrivateLink, VPC endpoints and DNS

A **gateway VPC endpoint** serves S3 and DynamoDB through route-table entries. An **interface VPC endpoint** uses one or more elastic network interfaces with private IPs and private DNS where supported. **AWS PrivateLink** commonly exposes a service privately through an interface endpoint; a service provider can publish an endpoint service backed by an NLB (or other supported configuration). PrivateLink is **not** full bidirectional VPC routing.

A **Route 53 Resolver inbound endpoint** allows authorized on-premises DNS resolvers to ask questions of VPC-aware DNS; an **outbound endpoint** forwards selected VPC DNS queries to on-premises DNS servers, using forwarding rules. Resolver rules can be shared across accounts through RAM. Private hosted zones alone do not magically resolve from on-premises networks.

**Example:** A SaaS provider wants clients to consume a private API without peering networks. Publish an endpoint service and grant endpoint access. If clients need all IP-level access to the provider's VPC, PrivateLink is not the right general routing solution.

**Trap:** PrivateLink endpoint connections are primarily consumer-initiated; check service/provider direction, DNS names, endpoint policies, and security groups.

AWS: https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html and https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html

## 6. S3: encryption, cost, access and replication

Amazon S3 stores **objects**, not mounted block volumes. Storage classes answer *how frequently do users retrieve an object?* Encryption choices answer *who manages keys and auditing?* **SSE-S3** is S3-managed encryption. **SSE-KMS** uses KMS keys for key control and audit integration; it can add KMS request costs. **S3 Bucket Keys** reduce requests to KMS for SSE-KMS and can reduce associated request costs by up to 99% under supported conditions. Bucket Keys are not supported for DSSE-KMS.

**Worked Q1 (source answer B):** Millions of frequently accessed SSE-KMS objects create high KMS request costs. The existing option B switches to SSE-S3, removing KMS request fees if KMS-based key controls are not mandatory. In real life, if KMS control must remain, **enable S3 Bucket Keys**; check the question options and constraints. Neither Intelligent-Tiering nor Glacier directly solves a KMS API-request issue.

**S3 versioning** preserves versions; **replication** copies objects asynchronously (not a replacement for backups or every data-protection concern); **Object Lock** enforces retention; **Access Points** simplify access patterns and scoped network controls; **S3 Access Grants** helps manage access to S3 data identities and grants. Use lifecycle transitions and expiration according to access patterns and minimum storage-duration charges.

**Trap:** Cross-Region Replication is not an automatic instant failover mechanism, and using SSE-KMS can require source and destination KMS permissions.

AWS: https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-key.html and https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html

## 7. EBS vs EFS vs FSx and Storage Gateway

Choose storage by **access protocol** first. **EBS** is persistent block storage primarily attached to EC2, typically AZ-scoped. **EFS** is managed elastic NFS shared file storage for Linux-compatible workloads and can be mounted by multiple clients. **FSx for Windows File Server** provides managed Windows/SMB integration and Active Directory features. **FSx for Lustre** targets high-performance parallel file workloads. **FSx for NetApp ONTAP** supports advanced enterprise NFS/SMB storage capabilities; **FSx for OpenZFS** offers low-latency NFS-oriented file systems.

**Storage Gateway** bridges on-premises environments to AWS storage through gateway abstractions. File Gateway exposes file shares backed by S3; volume gateway and tape gateway address other storage/backup patterns. It is not the same service as DataSync (bulk/recurring transfers) or Transfer Family (managed FTP/FTPS/SFTP/AS2 endpoints).

**Example:** On-prem Windows users need a shared SMB file server with AD permissions and a move to AWS → evaluate FSx for Windows. A Linux fleet needs NFS shared storage → EFS. A compute-intensive HPC job needs fast parallel throughput → FSx for Lustre.

**Trap:** An EBS snapshot is stored by AWS using S3 infrastructure but is not a regular S3 object you can browse in a bucket. Don't infer direct S3 object operations on snapshots.

AWS: https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html and https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html

## 8. Databases: RDS, Aurora, DynamoDB and caching

**RDS** manages relational database operations for supported engines. A **Multi-AZ deployment** improves availability and failover; **read replicas** scale reads and have replication lag, and they are not interchangeable with synchronous standby mechanisms. **Aurora** is a cloud-designed relational engine with distributed storage and engine-specific replication/failover characteristics. **DynamoDB** is key-value/document NoSQL for highly scalable access patterns; design partition keys carefully and use GSIs/LSIs when query patterns need them. **ElastiCache** provides in-memory caching (Redis/Valkey or Memcached options), not a durable primary database substitute by default.

**Example:** Payment records with complex joins and ACID transactions → RDS/Aurora. User-session lookups keyed by user ID at enormous scale → DynamoDB or cache depending on durability. Heavy repeated queries and read pressure → caching can improve latency and lower database load.

**Cross-Region:** Aurora Global Database, DynamoDB global tables, cross-Region replicas and backup/restore all have different replication consistency, recovery properties and operational implications. Never equate **replica exists** with **zero data loss**.

**Trap:** RDS Multi-AZ standby is not automatically available for normal read traffic; distinguish deployment variants and instance-level versus cluster designs.

AWS: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html and https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html

## 9. EC2, Auto Scaling, load balancing and placement

**ALB** is Layer 7 HTTP/HTTPS routing with host/path rules and application-aware features. **NLB** is Layer 4 TCP/UDP/TLS-oriented load balancing, useful when connection characteristics or static addresses matter. **Gateway Load Balancer** assists with deployment of network appliances for traffic inspection. Use **Auto Scaling** to adjust compute based on demand, placing instances across AZs; it does not by itself make stateful session data shared.

EC2 purchase options: On-Demand for flexible short-term usage, Savings Plans/Reserved Instances for steady commitments, Spot for interruption-tolerant workloads, and dedicated options for isolation/licensing requirements. **Placement groups**: cluster for low-latency nodes in close placement; spread for distinct hardware separation (with limits); partition for partition-aware distributed systems.

**Example:** A stateless API with variable demand → ALB + Auto Scaling across AZs; keep application state in a shared store such as DynamoDB, Aurora or ElastiCache. An HPC tightly coupled workload → cluster placement, subject to availability/capacity caveats.

**Trap:** Scaling EC2 horizontally requires statelessness or session strategy, not just adding instances. AZ and placement constraints matter.

AWS: https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html

## 10. ECS, EKS, Fargate and container modernization

**ECS** is AWS's container orchestrator. **EKS** provides managed Kubernetes control-plane services. **Fargate** is serverless compute capacity for supported ECS/EKS workloads, so you can avoid managing the EC2 worker fleet. **ECR** stores container images. An image repository is not a deployment runtime, and Kubernetes clusters don't remove the need to plan networking, authentication and cost.

**Example:** A team wants to containerize a background worker with minimal Kubernetes expertise → ECS on Fargate can be simpler. An existing organization has Kubernetes operators, controllers, custom resources and cluster portability requirements → EKS may fit.

**Cost/operations trade-off:** Fargate simplifies host management but can be more expensive for some sustained workloads. EC2 node fleets allow more control but require AMI patching, node scaling and lifecycle management. Use serverless when operational simplicity outweighs raw unit-cost differences.

**Trap:** EKS is not automatically the best answer just because the application uses Docker; examine whether Kubernetes features are truly necessary.

AWS: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html and https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html

## 11. Lambda, queues, events and orchestration

**Lambda** executes short-lived event-driven code without managing servers. **SQS** decouples producers and consumers with durable queues; **SNS** fans messages out to subscribers; **EventBridge** routes events using rules and event buses; **Step Functions** coordinates multi-step workflows with state and retries. **Kinesis Data Streams** addresses ordered streaming ingestion for applicable analytics/processing needs. **Amazon MQ** supports broker protocols for legacy message systems.

**SQS Standard** prioritizes scale with at-least-once delivery and best-effort ordering. **SQS FIFO** supports ordered message groups and deduplication semantics, with documented throughput constraints. Consumer code must generally be idempotent. Visibility timeout temporarily hides a received message; it does not delete it. Configure retry and DLQ policies appropriately.

**Example:** Incoming orders must trigger billing, notifications and shipping independently → SNS fan-out to distinct SQS queues. A workflow needs approval, retries and wait states → Step Functions. A high-volume event integration across AWS accounts → EventBridge bus with appropriate policy controls.

**Trap:** SNS does not store work for later polling the way SQS does. EventBridge rules select/route events, not necessarily guarantee exactly-once processing.

AWS: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html and https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html

## 12. Disaster recovery: RTO, RPO and failover

**RPO** = how much historical data you can tolerate losing (measured backward from the outage). **RTO** = how long the service may remain unavailable. They are different axes. Common strategies from typically less costly/slower to more costly/faster are **backup and restore**, **pilot light**, **warm standby**, and **active-active**. Those are design patterns, not contractual guaranteed numbers.

**Example:** RPO 15 minutes and RTO one hour → a continuously replicated warm standby or suitable database replication + tested automation may fit; daily snapshots probably violate RPO. RPO 24 hours and RTO two days → backup and restore may be sufficient. Check whether replication is synchronous or asynchronous before claiming zero data loss.

**AWS Elastic Disaster Recovery (DRS)** continuously replicates servers into a staging area and can help with recovery of supported workloads. **AWS Backup** centralizes protection policies for supported resources, but a backup plan alone does not build end-to-end application failover. Route 53 failover/health checks or Global Accelerator can route requests, but only if your alternative stack/data is genuinely ready.

**Trap:** Multi-AZ protects against an AZ outage but isn't equivalent to a full Regional-disaster architecture. Test restoration regularly and include DNS TTL, dependencies and application startup in RTO.

AWS: https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/disaster-recovery-dr-objectives.html

## 13. Monitoring, incident response and governance

**CloudWatch** covers operational metrics, logs, alarms and application monitoring. **CloudTrail** records AWS API and account activity; don't substitute one for the other. **AWS Config** tracks supported resource configuration and evaluates compliance against rules. **Systems Manager** helps manage fleet operations, patching and sessions; **Session Manager** can enable shell access without traditional inbound SSH when its prerequisites are met.

For security posture, combine detection services according to threat class: **GuardDuty** detects threats, **Security Hub** aggregates security findings/posture, **Macie** discovers sensitive data in S3, **WAF** filters supported application-layer web attacks, and **Shield** addresses DDoS-related protections. **Control Tower** supports governed account setup; it is not a logging product.

**Example:** Unauthorized IAM changes? Use CloudTrail to establish the API event; EventBridge to route a matching event; Lambda/SSM automation to respond; Config to evaluate drift and baseline controls. These tools complement rather than replace each other.

**Trap:** CloudTrail cannot by itself prevent an API call; an IAM/SCP/resource policy or network guardrail does that. Monitoring and enforcement are distinct architectural layers.

AWS: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html and https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html

## 14. Cost optimization and performance

Identify the main cost driver *before* choosing a service: compute hours, provisioned capacity, I/O requests, data transfer, NAT processing, cross-AZ transfers, KMS requests, storage class, idle resources or software licensing. Pricing options do not solve an unrelated cost driver. Check if the scenario asks for lowest absolute cost or lowest **total cost of ownership including people and operational effort**.

**Savings Plans** can benefit predictable compute spend; **Spot** helps flexible fault-tolerant workloads; **Compute Optimizer** recommends resource-sizing opportunities using workload signals; **Cost Explorer** helps analyze spending; **Trusted Advisor** provides checks based on entitlement and account conditions; **Budgets** can alert/enforce limited budget actions. Each solves a different problem.

**Example:** Millions of S3 SSE-KMS operations result in a large KMS bill. Switching EC2 purchase models doesn't fix it. Bucket Keys or a different encryption scheme may. Another case: a high-traffic private subnet downloads S3 data via NAT; a gateway endpoint can lower unnecessary NAT processing while keeping traffic private.

**Trap:** Always examine data-transfer and cross-AZ costs before claiming a centralized shared NAT, TGW, or cross-Region design is cheapest.

AWS: https://docs.aws.amazon.com/cost-management/latest/userguide/what-is-costmanagement.html

## 15. Migration planning and the 7 Rs

A migration starts with discovery and business constraints, not with an agent installation. The common **7 Rs** are **rehost** (lift-and-shift), **relocate** (platform move without changing app architecture), **replatform** (limited optimization without redesign), **repurchase** (replace with SaaS), **refactor/re-architect** (substantial redesign), **retain** (leave for now), and **retire** (decommission). Choose per application dependency and business value.

**Discovery** collects servers, dependency information and utilization. **Migration Hub** can give portfolio or migration tracking integration depending on available capabilities. Assess TCO, on-prem licenses, interconnects, dependencies, data sovereignty, testing and rollback. Do not assume a migration service automatically understands business dependencies.

**Example:** A legacy Java application on EC2 where code change is prohibited → rehost. A self-managed SQL Server on EC2 to RDS with minimal schema/application changes → replatform when engine and feature compatibility allow. A monolithic app broken into independently deployed event-driven services → refactor.

**Trap:** 'Most cost-effective' can change with time horizon and licensing. A correct network migration plan must handle identity, DNS, route changes, data synchronization and cutover—not just provision target instances.

AWS: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-retiring-applications/7-rs.html

## 16. AWS DMS, schema conversion and CDC

**AWS DMS** moves supported database data between sources and targets. **Full load** copies existing rows; **CDC (change data capture)** applies ongoing changes after/beside initial transfer, allowing a smaller cutover window. **Schema Conversion** handles supported structural conversion requirements, particularly for heterogeneous engine migrations. Data migration and schema conversion are related but distinct tasks.

**Example:** An on-prem Oracle database migrates to Amazon Aurora PostgreSQL. Assess incompatible schema, stored procedures, types and application SQL; perform schema conversion where appropriate; run DMS full load + CDC; validate row counts/business queries; freeze writes or coordinate a brief cutover; switch connection endpoints after validation.

**Homogeneous** means same or compatible database engine; **heterogeneous** means different engines and usually greater schema/application conversion risk. A DMS replication task does not by itself guarantee that every schema object or stored procedure was converted. Confirm DMS endpoints, engine features, LOB handling, task modes and CDC prerequisites.

**Trap:** 'Minimal downtime' points to CDC but it is not necessarily zero downtime; target catching-up and application cutover still matter.

AWS: https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html

## 17. Application Migration Service and AWS Elastic Disaster Recovery

**AWS Application Migration Service (MGN)** is designed for lift-and-shift server migration with replication and test/cutover. **AWS Elastic Disaster Recovery (DRS)** is geared toward disaster recovery: recovering operational applications after failures via continuous replication and launch of recovery instances. Both involve replication concepts but different primary purposes and process expectations.

**Example:** 200 on-prem servers must be moved to AWS with minimal code change and controlled test/cutover → evaluate MGN. Existing production servers must have a recoverable counterpart in AWS for an unexpected outage → DRS may fit.

Do not confuse **machine migration** with **managed database migration**. Moving a database-hosting EC2/server with MGN is not the same as transforming the database to Aurora with DMS. Select service by outcome: server replication, application redesign, or DB data/engine transformation.

**Trap:** The newest AWS migration offerings can change feature coverage. Audit historical exam options for retired services, renamed tooling and region/OS limitations before memorization.

AWS: https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html and https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html

## 18. DataSync vs Transfer Family vs Storage Gateway vs Snow Family

**AWS DataSync** efficiently transfers file/object data between supported locations, including on-premises storage and AWS destinations, often with scheduling, metadata handling and verification. **AWS Transfer Family** provides managed file-transfer endpoints and workflows for protocols such as SFTP/FTPS/FTP/AS2 depending on configuration and service support. **Storage Gateway** presents hybrid file, volume or tape interfaces to existing systems. **Snow Family** addresses offline/edge data movement when networks are constrained and device capabilities fit.

**Example:** Nightly bulk NFS files need to arrive in S3 while preserving metadata where supported → DataSync. Thousands of external partners must continue sending SFTP uploads → Transfer Family. Local SMB users want familiar shares backed by S3 → File Gateway. Massive datasets at remote sites with inadequate bandwidth → consider Snow device capabilities and availability.

**Trap:** DataSync is not a managed public SFTP server; Transfer Family isn't the general-purpose solution for replicating an existing NFS tree with preserved ownership and POSIX metadata. Be precise about supported source/target/protocol combinations.

AWS: https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html and https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-family.html

## 19. Migration modernization: event-driven, managed databases and analytics

Modernization changes architecture to improve business outcomes, not merely server location. Typical paths: EC2 hosted monolith → containerized service (ECS/EKS) → smaller APIs; nightly batch → event ingestion + queue + workers; self-managed relational databases → RDS/Aurora where feature compatibility allows; scheduled analytics → S3 data lake + Glue/EMR/Athena/Redshift depending on query style.

**Example:** A file ingestion application originally exposes custom SFTP servers with OS maintenance. A managed SFTP endpoint can remove server ownership, and EventBridge/Lambda/Step Functions can coordinate post-upload steps. This is more of a modernization than simply lifting the SFTP server VM.

**Trade-off:** More managed services can reduce undifferentiated operations but increase integration points, distributed tracing needs and eventual-consistency complexity. An architecture diagram must show retries, DLQs, idempotency, security roles, data ownership and monitoring—not only service icons.

**Trap:** Serverless is not synonymous with free, fastest or infinitely unconstrained; concurrency and quotas must be designed explicitly.

AWS: https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html

## 20. Architecture decision matrix to memorize

| Requirement | Usually investigate first | Common wrong shortcut |
|---|---|---|
| Organization-wide permission boundary | SCP/RCP + IAM/resource policies | SCP grants access by itself |
| Private S3 from VPC | S3 gateway endpoint | All traffic through NAT |
| Private SaaS service | PrivateLink endpoint service | Full-mesh peering for every client |
| Hundreds of VPCs to on-prem | TGW / Cloud WAN + DX/VPN | Hundreds of independent VPNs |
| Relational DB high availability | Multi-AZ / Aurora cluster design | Read replica as synchronous HA standby |
| Read scalability | Read replicas and cache | Vertical scaling only |
| Shared Linux file system | EFS or relevant FSx offering | General-purpose EBS attached everywhere |
| Windows SMB / AD file sharing | FSx for Windows File Server | EFS without protocol analysis |
| RPO / RTO demanding recovery | Replication and tested DR architecture | Daily backup for minute-level RPO |
| Rehost operating system and server | Application Migration Service | DMS for the entire machine |
| Ongoing DB changes during migration | DMS CDC | One-time export alone |
| Bulk on-prem NFS to S3 | DataSync | Transfer Family if no file-transfer endpoint required |
| External SFTP partners | Transfer Family | DataSync as public SFTP endpoint |
| Fan-out to independent consumers | SNS → SQS per consumer | One queue with competing consumer semantics |
| Stateful multistep workflow | Step Functions | Lambda alone with sleeps and manual retries |
| Investigate who changed IAM | CloudTrail | CloudWatch metrics alone |
| SSE-KMS KMS request cost | S3 Bucket Keys or assess SSE-S3 | Archive frequently read objects |

This matrix gives a **starting point**, not an always-correct answer. Hard constraints, service quotas, protocols, encryption rules, failure modes and exact option wording override shortcuts.

## 21. Six-step active recall routine

1. **Cover the answer** in the question bank and restate requirements in one sentence.
2. **Draw the data flow**: who initiates, what network path, where the data is stored, where it fails.
3. **Predict the service** before reading answer choices.
4. **Eliminate choices** by hard constraint and note one factual reason for each elimination.
5. **Name the deciding trade-off**: RTO, RPO, cost, license, scalability, encryption, operational overhead or compatibility.
6. **Return in 2 and 7 days** to questions missed or still unverified. Read the linked AWS docs for disputed questions rather than memorizing the key.

## 22. Question-bank quality warnings and exam readiness

The dataset currently contains **674 items**; **539 single-answer** and **135 multi-answer** questions. **481** lack a main explanation, **478** lack separate wrong-option explanations, **551** are tagged `source-key-unverified`, and **109** have nonempty source warnings. These are *file content statistics*, not a count of actually wrong answers. Some reviewed questions explicitly flag outdated products, option truncation, answer-key defects or cardinality conflicts. Review the exact `answerStatus` and `sourceWarning` before trusting them.

A suggested study order is: (1) IAM and account boundaries, (2) networks and hybrid DNS, (3) storage/database trade-offs, (4) availability, security and cost, (5) migration/modernization, (6) timed mixed-domain practice. Allocate more time to topics that require you to reason through several service layers rather than simply recognizing a service name.

## 23. Official references

- [SAP-C02 exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-professional-02/solutions-architect-professional-02.html)
- [SAP-C03 comparison](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-professional-03/sap-03-comparison.html)
- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)
- [AWS Prescriptive Guidance](https://docs.aws.amazon.com/prescriptive-guidance/)

*Study notes are training material, not an official AWS answer key. Review service feature changes and exact question wording against current AWS documentation.*
