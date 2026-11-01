# SAP-C02 question-by-topic learning index

**Dataset:** [questions.json](../../src/data/questions.json) on `answer-audit-2026-10-28` (674 questions). This index was generated from ALL 674 records. Questions are assigned to ONE primary topic using keyword matching; mixed-topic questions may fit several topics. The mapping is a **study-navigation aid**, not a technical correctness verdict.

**Important:** 481 questions lack a main explanation; 551 are explicitly tagged `source-key-unverified`; 109 include a nonempty source warning. The answer letters listed here repeat the dataset and MUST NOT be treated as independently verified.

**Legend:** 🟢 = has an existing explanation and lacks an explicit source warning (still not guaranteed correct); 🟡 = incomplete explanation or source warning; 🔴 = status explicitly suggests outdated/disputed/defective or conflicting options. Every ID from 1 to 674 appears exactly once below.

See [the detailed study guide](./SAP-C02-Detailed-Study-Guide.md) for lessons, decisions, diagrams and exam traps.


## 1. Organizations, SCPs, IAM & cross-account access — 185 questions

| Q | Domain | Existing key* | Status | Scenario cue |
|---|---:|---|---|---|
| Q6 | 2 | B | 🟢 source-key-unverified | A multi-tenant software as a service (SaaS) customer support platform serves thousands of enterprise clients. T… |
| Q12 | 1 | B, C, E | 🔴 disputed-ambiguous-third-choice | A company is using AWS Organizations with a multi-account architecture. The company's current security configur… |
| Q13 | 1 | A | 🟢 aws-docs-verified-study-wording | A company plans to consume a third-party software-as-a-service (SaaS) application through APIs. The SaaS provid… |
| Q25 | 1 | B, D | 🟢 source-key-unverified | A large company is migrating ils entire IT portfolio to AWS. Each business unit in the company has a standalone… |
| Q28 | 1 | C | 🟢 source-key-unverified | A company has multiple business units that each have separate accounts on AWS. Each business unit manages its o… |
| Q29 | 1 | D | 🟢 source-key-unverified | A solutions architect must provide a secure way for a team of cloud engineers to use the AWS CLI to upload obje… |
| Q33 | 1 | D | 🟢 source-key-unverified | A company is migrating its development and production workloads to a new organization in AWS Organizations. The… |
| Q44 | 4 | B | 🟢 domain4-key-corrected-best-offered-external-pending | A company wants to migrate an application to Amazon EC2 from VMware Infrastructure that runs in an on-premises … |
| Q50 | 1 | B | 🟢 source-key-unverified | A company is subject to regulatory audits of its financial information. External auditors who use a single AWS … |
| Q51 | 1 | A, C, F | 🟢 source-key-unverified | A company's factory and automaton applications are running in a single VPC More than 23 applications run on a c… |
| Q65 | 1 | C | 🟢 source-key-unverified | A financial services company has an asset management product that thousands of customers use around the world. … |
| Q67 | 3 | D | 🟢 source-key-unverified | A company has set up its entire infrastructure on AWS. The company uses Amazon EC2 instances to host its ecomme… |
| Q69 | 1 | C, D | 🟢 source-key-unverified | A company has multiple AWS accounts and manages these accounts with AWS Organizations. A developer was given IA… |
| Q71 | 1 | C, E | 🟢 source-key-unverified | A company manages multiple AWS accounts by using AWS Organizations. Under the root OU. the company has two OUs:… |
| Q75 | 3 | B | 🟢 source-key-unverified | A company needs to audit the security posture of a newly acquired AWS account. The company’s data security team… |
| Q76 | 2 | B | 🟢 source-key-unverified | A software company needs to create short-lived test environments to test pull requests as part of its developme… |
| Q80 | 1 | D | 🟢 source-key-unverified | A company has 10 accounts that are part of an organization in AWS Organizations AWS Config is configured in eac… |
| Q81 | 1 | A | 🟢 source-key-unverified | A company has an online learning platform that teaches data science. The platform uses the AWS Cloud to provisi… |
| Q87 | 1 | D | 🟡 source-key-unverified | A financial company needs to create a separate AWS account for a new digital wallet application. The company us… |
| Q89 | 1 | B | 🟢 source-key-unverified | A company uses a single organization in AWS Organizations with all features enabled to manage 300 AWS accounts… |
| Q99 | 1 | B | 🟢 source-key-unverified | A company manages hundreds of AWS accounts centrally in an organization in AWS Organizations. The company recen… |
| Q101 | 3 | B | 🟡 source-key-unverified | A company runs many workloads on AWS and uses AWS Organizations to manage its accounts. The workloads are hoste… |
| Q104 | 1 | B, D, E | 🟡 source-key-unverified | An enterprise company is building an infrastructure services platform for its users. The company has the follow… |
| Q108 | 1 | B | 🟡 source-key-unverified | A solutions architect at a large company needs to set up network security tor outbound traffic to the internet … |
| Q111 | 3 | D | 🟡 source-key-unverified | During an audit, a security team discovered that a development team was putting IAM user secret access keys in … |
| Q113 | 1 | C, D | 🟡 source-key-unverified | A company has multiple AWS accounts and manages these accounts with AWS Organizations. A developer was given IA… |
| Q117 | 1 | D | 🟡 source-key-unverified | A company has deployed applications to thousands of Amazon EC2 instances in an AWS account. A security audit di… |
| Q118 | 1 | B | 🟡 source-key-unverified | A company wants to use AWS IAM Identity Center (AWS Single Sign-On) to manage employee access to AWS services. … |
| Q120 | 1 | B | 🟡 source-key-unverified | A company uses AWS Organizations with all features enabled to manage its accounts. The company has configured A… |
| Q125 | 1 | C | 🟡 source-key-unverified | A research company is running daily simul-ations in the AWS Cloud to meet high demand. The simu-lations run on … |
| Q126 | 1 | C | 🟡 source-key-unverified | A company has 20 accounts in an organization in AWS Organizations. The accounts are in two OUs: development and… |
| Q136 | 1 | A, C | 🟡 source-key-unverified | A company has 50 AWS accounts that are members of an organization in AWS Organizations Each account contains mu… |
| Q139 | 1 | A, C, E | 🟡 source-key-unverified | A company needs to aggregate Amazon CloudWatch logs from its AWS accounts into one central logging account. The… |
| Q140 | 3 | A, B | 🟡 source-key-unverified | A solutions architect is importing a VM from an on-premises environment by using the Amazon EC2 VM Import featu… |
| Q150 | 1 | A | 🟡 source-key-unverified | A company has a new requirement to store all database backups in an isolated AWS account. The company is using … |
| Q153 | 4 | A | 🔴 verified-aws-doc-external-exact-match-minor-iam-terminology | A company is planning to migrate an application to AWS. The application runs as a Docker container and uses an … |
| Q154 | 1 | B | 🟡 source-key-unverified | A company is in the process of implementing AWS Organizations to constrain its developers to use only Amazon EC… |
| Q155 | 3 | A, D, E | 🟡 source-key-unverified | A company runs an ecommerce website on Amazon ECS behind an Application Load Balancer (ALB). The container imag… |
| Q156 | 3 | A | 🟡 source-key-unverified | A company consists of two separate business units. Each business unit has its own AWS account within a single o… |
| Q157 | 3 | A, D, E | 🟡 source-key-unverified | A company is running an application in the AWS Cloud. The company's security team must approve the creation of … |
| Q164 | 2 | D | 🟡 source-key-unverified | A company is implementing a serverless architecture by using AWS Lambda functions that need to access a Microso… |
| Q170 | 3 | C | 🟡 source-key-unverified | A company has a web application that securely uploads pictures and videos to an Amazon S3 bucket. The company r… |
| Q172 | 3 | A, D, F | 🟡 source-key-unverified | A company has many AWS accounts in an organization in AWS Organizations. The accounts contain many Amazon EC2 i… |
| Q173 | 1 | A | 🟡 source-key-unverified | A company uses AWS Organizations to manage a multi-account structure. The company has hundreds of AWS accounts … |
| Q174 | 3 | A, C | 🟡 source-key-unverified | A company uses IAM Identity Center for data scientist access. Each user should be able to accessonly their own … |
| Q180 | 1 | A | 🟡 source-key-unverified | A company is deploying an AI agent on Amazon Bedrock AgentCore Runtime. The agent automates business processes … |
| Q186 | 4 | B | 🔴 defective-nonunique-a-and-b-source-key-b | A company wants to modernize a monolithic application in the company's data center and deploy the application o… |
| Q189 | 4 | B, E, F | 🟡 source-key-unverified | A company uses AWS Organizations to manage more than 1.000 AWS accounts. The company has created a new develope… |
| Q191 | 1 | B | 🟡 source-key-unverified | A company use an organization in AWS Organizations to manage multiple AWS accounts. The company hosts some appl… |
| Q192 | 1 | B, C, F | 🟡 source-key-unverified | A company that uses AWS Organizations allows developers to experiment on AWS. As part of the landing zone that … |
| Q201 | 1 | D | 🟡 source-key-unverified | A company creates an AWS Control Tower landing zone to manage and govern a multi- account AWS environment. The … |
| Q209 | 1 | D | 🟡 source-key-unverified | A company hosts a metadata API on Amazon EC2 instances behind an internet-facing Application Load Balancer (ALB… |
| Q213 | 1 | B | 🟡 source-key-unverified | A company has created an OU in AWS Organizations for each of its engineering teams Each OU owns multiple AWS ac… |
| Q214 | 3 | B | 🟡 source-key-unverified | A company runs an application across three AWS accounts. The company uses an organization in AWS Organizations … |
| Q216 | 3 | B | 🟡 source-key-unverified | A company has AWS accounts that are in an organization in AWS Organizations. The company wants to track Amazon … |
| Q221 | 4 | B | 🔴 verified-b-technical-question-cardinality-conflict | A company wants to migrate an Amazon Aurora MySQL DB cluster from an existing AWS account to a new AWS account … |
| Q224 | 4 | B | 🔴 verified-b-aws-external-wording-defects | A company is planning a migration from an on-premises data center to the AWS cloud. The company plans to use mu… |
| Q225 | 3 | A, B | 🟡 source-key-unverified | A solutions architect is importing a VM from an on-premises environment by using the Amazon EC2 VM Import featu… |
| Q226 | 3 | B | 🟡 source-key-unverified | A company is using GitHub Actions to run a CI/CD pipeline that accesses resources on AWS. The company has an IA… |
| Q227 | 4 | C | 🔴 verified-c-aws-external-source-defects | A large mobile gaming company has successfully migrated all of its on-premises infrastructure tothe AWS Cloud. … |
| Q229 | 1 | C | 🟡 source-key-unverified | A company has dozens of AWS accounts for different teams, applications, and environments. The company has defin… |
| Q237 | 3 | A | 🟡 source-key-unverified | A solutions architect is creating an AWS CloudFormation template from an existing manually created non-producti… |
| Q243 | 1 | A, C, E | 🟡 source-key-unverified | A company needs to aggregate Amazon CloudWatch logs from its AWS accounts into one central logging account. The… |
| Q244 | 4 | B | 🟡 verified-b-aws-external-full-load-cdc-caveat | A company needs to migrate a 2 TB MySQL database from an on-premises data center to an Amazon Aurora cluster. T… |
| Q251 | 1 | C | 🟡 source-key-unverified | A solutions architect is designing a solution to automatically provision new AWS accounts in an organization in… |
| Q252 | 1 | C | 🟡 source-key-unverified | A company with several AWS accounts is using AWS Organizations and service control policies (SCPs). An Administ… |
| Q254 | 1 | A | 🟡 source-key-unverified | A company uses an organization in AWS Organizations that has multiple AWS accounts. The accounts host multiple … |
| Q256 | 1 | C | 🟡 source-key-unverified | A company has its cloud infrastructure on AWS A solutions architect needs to define the infrastructure as code… |
| Q262 | 3 | B | 🟡 source-key-unverified | A company uses Amazon S3 to store files and images in a variety of storage classes. The company's S3 costs have… |
| Q263 | 1 | C | 🟡 source-key-unverified | A company has an organization in AWS Organizations that has a large number of AWS accounts. One of the AWS acco… |
| Q267 | 1 | A | 🟡 source-key-unverified | A solutions architect is auditing the security setup of an AWS Lambda function for a company. The Lambda functi… |
| Q276 | 4 | A, B, C | 🟡 source-key-unverified | A company operates a fleet of servers on premises and operates a fleet of Amazon EC2 instances in its organizat… |
| Q282 | 1 | D | 🟡 source-key-unverified | Company A recently acquired Company B. Company A requires that Company B use Amazon WorkSpaces in a separate me… |
| Q283 | 3 | C, D, E | 🟡 source-key-unverified | A company is using an organization in AWS Organizations to manage hundreds of AWS accounts. A solutions archite… |
| Q289 | 1 | A | 🟡 source-key-unverified | A company uses AWS Organizations and tags every resource with a BusinessUnit tag. They want to allocate cloud c… |
| Q291 | 4 | B | 🔴 reviewed-with-caveats | A company recently completed the migration from an on-premises data center to the AWS Cloud by using a replatfo… |
| Q296 | 1 | C | 🟡 source-key-unverified | A retail company is mounting IoT sensors in all of its stores worldwide. During the manufacturing of each senso… |
| Q299 | 1 | A, E | 🟡 source-key-unverified | A company has many AWS accounts and uses AWS Organizations to manage all of them. A solutions architect must im… |
| Q302 | 3 | A, E | 🟡 source-key-unverified | A company has an IoT data lake that is stored in Amazon S3. Data scientists in a separate AWS account need to a… |
| Q304 | 1 | A, C | 🟡 source-key-unverified | A company needs to apply consistent custom security audit rules across its organization in AWS Organizations. A… |
| Q310 | 1 | A, C | 🟡 source-key-unverified | A company has multiple AWS accounts. The company recently had a security audit that revealed many unencrypted A… |
| Q315 | 1 | B | 🟡 source-key-unverified | A company is migrating its infrastructure to the AWS Cloud. The company must comply with a variety of regulator… |
| Q316 | 3 | D | 🟡 source-key-unverified | A startup company hosts a fleet of Amazon EC2 instances in private subnets using the latest Amazon Linux 2 AMI… |
| Q319 | 1 | A | 🟡 source-key-unverified | A company needs to copy backups of 40 RDS for MySQL databases from a production account to a central backup acc… |
| Q322 | 3 | A | 🟡 source-key-unverified | A company has an application that uses AWS Key Management Service (AWS KMS) to encrypt and decrypt data. The ap… |
| Q325 | 1 | A | 🟡 source-key-unverified | A company recently acquired several other companies. Each company has a separate AWS account with a different b… |
| Q327 | 4 | A | 🔴 verified | A company runs a Java application that has complex dependencies on VMs that are in the company's data center. T… |
| Q332 | 3 | B | 🟡 source-key-unverified | A company has an application that uses Amazon EC2 instances in an Auto Scaling group. The quality assurance (QA… |
| Q335 | 1 | B | 🟡 source-key-unverified | A company has multiple AWS accounts that are in an organization in AWS Organizations. The company needs to stor… |
| Q336 | 3 | A | 🟡 source-key-unverified | A company has a legacy monolithic application that is critical to the company's business. The company hosts the… |
| Q339 | 1 | C | 🟡 source-key-unverified | A company is expanding. The company plans to separate its resources into hundreds of different AWS accounts in … |
| Q340 | 3 | B | 🟡 source-key-unverified | A multinational insurance company is deploying an internal claims processing AI assistant that is powered by Am… |
| Q350 | 4 | B, E | 🟡 source-key-unverified | A company wants to migrate its website from an on-premises data center onto AWS. At the same time, it wants to … |
| Q351 | 3 | B | 🟡 source-key-unverified | A software as a service (SaaS) company uses AWS to host a service that is powered by AWS PrivateLink. The servi… |
| Q359 | 1 | C | 🟡 source-key-unverified | A financial services company sells its software-as-a-service (SaaS) platform for application compliance to larg… |
| Q361 | 3 | C | 🟡 source-key-unverified | A company has an organization that has many AWS accounts in AWS Organizations. A solutions architect must impro… |
| Q362 | 1 | C | 🟡 source-key-unverified | An AWS partner company is building a service in AWS Organizations using Its organization named org. This servic… |
| Q369 | 1 | B | 🟡 source-key-unverified | A company uses AWS Organizations for a multi-account setup in the AWS Cloud. The company uses AWS Control Tower… |
| Q370 | 1 | A, C, D | 🟡 source-key-unverified | A company wants to migrate to AWS. The company wants to use a multi-account structure with centrally managed ac… |
| Q373 | 1 | A | 🟡 source-key-unverified | A company is designing an AWS Organizations structure. The company wants to standardize a process to apply tags… |
| Q378 | 1 | C | 🟡 source-key-unverified | A company wants to optimize AWS data-transfer costs and compute costs across developer accounts within the comp… |
| Q379 | 1 | A, B, C | 🟡 source-key-unverified | A company runs applications in hundreds of production AWS accounts. The company uses AWS Organizations with all… |
| Q381 | 4 | B, D, F | 🟡 source-key-unverified | A solutions architect has implemented a SAML 2 0 federated identity solution with their company's on-premises i… |
| Q382 | 1 | A, C, E | 🟡 source-key-unverified | A company has many separate AWS accounts and uses no central billing or management. Each AWS account hosts serv… |
| Q384 | 1 | D | 🟡 source-key-unverified | A large payroll company recently merged with a small staffing company. The unified company now has multiple bus… |
| Q389 | 1 | C | 🟡 source-key-unverified | SIMULATION A research company conducts mathematical simulations in the AWS Cloud. The simulations run on severa… |
| Q395 | 4 | A | 🔴 verified-historical-outdated-service | A company is planning to migrate an on-premises data center to AWS. The company currently hosts the data center… |
| Q400 | 3 | A | 🟡 source-key-unverified | A company in the United States (US) has acquired a company in Europe. Both companies use the AWS Cloud. The US … |
| Q404 | 1 | C | 🟡 source-key-unverified | A company is using AWS Organizations to manage multiple AWS accounts. For security purposes, the company requir… |
| Q406 | 1 | D | 🟡 source-key-unverified | A company is using AWS Organizations to manage multiple accounts Due to regulatory requirements, the company wa… |
| Q407 | 1 | A, B, E | 🟡 source-key-unverified | A company is developing and hosting several projects in the AWS Cloud. The projects are developed across multip… |
| Q408 | 3 | A | 🔴 source-truncated | A solutions architect needs to implement a client-side encryption mechanism for objects that will be stored in … |
| Q414 | 4 | D | 🟡 verified-aws-and-external | A company runs an application in an on-premises data center. The application gives users the ability to upload … |
| Q415 | 3 | D | 🟡 source-key-unverified | A company uses AWS Organizations. The company creates a central VPC in an AWS account that is designated for ne… |
| Q423 | 1 | A, D | 🟡 source-key-unverified | A company has hundreds of AWS accounts. The company recently implemented a centralized internal process for pur… |
| Q432 | 1 | A, E | 🟡 source-key-unverified | A software company hosts an application on AWS with resources in multiple AWS accounts and Regions. The applica… |
| Q439 | 1 | D | 🟡 source-key-unverified | A company is using an on-premises Active Directory service for user authentication. The company wants to use th… |
| Q442 | 3 | A, C, F | 🟡 source-key-unverified | The company needs to determine which costs on the monthly AWS bill are attributable to each application or team… |
| Q444 | 1 | A, C | 🟡 source-key-unverified | A company wants to use an Amazon S3 bucket for its data scientists to store documents. The company uses AWS IAM… |
| Q451 | 1 | A, C, F | 🟡 source-key-unverified | A digital marketing company has multiple AWS accounts that belong to various teams. The creative team uses an A… |
| Q452 | 1 | C | 🟡 source-key-unverified | An enterprise company wants to allow its developers to purchase third-party software through AWS Marketplace. T… |
| Q455 | 1 | A | 🟡 source-key-unverified | A company is running several applications in the AWS Cloud. The applications are specific to separate business … |
| Q456 | 1 | B, D, F | 🟡 source-key-unverified | A solutions architect needs to copy data from an Amazon S3 bucket m an AWS account to a new S3 bucket in a new … |
| Q458 | 3 | D | 🟡 source-key-unverified | A company has an application that generates reports and stores them in an Amazon S3 bucket When a user accesses… |
| Q459 | 1 | D | 🟡 source-key-unverified | A company uses AWS Organizations with a single OU named Production to manage multiple accounts All accounts are… |
| Q463 | 1 | A, C | 🟡 source-key-unverified | A company has a data lake in Amazon S3 that needs to be accessed by hundreds of applications across many AWS ac… |
| Q465 | 1 | A | 🟡 source-key-unverified | A company wants to deploy an AWS WAF solution to manage AWS WAF rules across multiple AWS accounts. The account… |
| Q466 | 1 | C | 🟡 source-key-unverified | A company is using AWS Control Tower to manage AWS accounts in an organization in AWS Organizations. The compan… |
| Q468 | 1 | B | 🟡 source-key-unverified | A company uses AWS Organizations to manage its development environment. Each development team at the company ha… |
| Q471 | 1 | C | 🟡 source-key-unverified | A large company recently experienced an unexpected increase in Amazon RDS and Amazon DynamoDB costs. The compan… |
| Q472 | 1 | A | 🟡 source-key-unverified | A Solutions Architect wants to make sure that only AWS users or roles with suitable permissions can access a ne… |
| Q473 | 3 | B | 🟡 source-key-unverified | A company uses AWS Organizations to manage its AWS accounts. The company needs a list of all its Amazon EC2 ins… |
| Q476 | 1 | B, E | 🟡 source-key-unverified | A company has multiple lines of business (LOBs) that toll up to the parent company. The company has asked its s… |
| Q480 | 1 | A | 🟡 source-key-unverified | A company that has multiple AWS accounts is using AWS Organizations. The company’s AWS accounts host VPCs, Amaz… |
| Q483 | 1 | A | 🟡 source-key-unverified | A company uses an organization in AWS Organizations to manage the company's AWS accounts. The company uses AWS … |
| Q484 | 2 | A | 🟡 source-key-unverified | A company is building an application on Amazon EMR to analyze data. The following user groups need to perform d… |
| Q486 | 3 | A, B | 🟡 source-key-unverified | A company has several AWS accounts. A development team is building an automation framework for cloud governance… |
| Q500 | 1 | D | 🟡 source-key-unverified | A global healthcare analytics company runs a regulated workload on AWS across dozens of AWS accounts. The compa… |
| Q503 | 1 | C | 🟡 source-key-unverified | A company is designing its network configuration in the AWS Cloud. The company uses AWS Organizations to manage… |
| Q505 | 3 | A | 🟡 source-key-unverified | A solutions architect is preparing to deploy a new security tool into several previously unused AWS Regions. Th… |
| Q508 | 1 | C | 🟡 source-key-unverified | A company established a data-sharing agreement with a supplier. A solutions architect must establish bidirectio… |
| Q512 | 1 | D | 🟡 source-key-unverified | A company has a project that is launching Amazon EC2 instances that are larger than required. The project's acc… |
| Q518 | 1 | A | 🟡 source-key-unverified | A company uses AWS Organizations AWS account. A solutions architect must design a solution in which only admini… |
| Q522 | 1 | A | 🟡 source-key-unverified | A company has an organization in AWS Organizations. In a linked AWS account, the company has Amazon EC2 instanc… |
| Q526 | 4 | A, B | 🟡 source-key-unverified | A research center is migrating to the AWS Cloud and has moved its on-premises 1 PB object storage to an Amazon … |
| Q531 | 3 | B | 🟡 source-key-unverified | A company's solutions architect is reviewing a new internally developed application in a sandbox AWS account Th… |
| Q533 | 3 | C, D | 🟡 source-key-unverified | A retail company needs to provide a series of data files to another company, which is its business partner Thes… |
| Q541 | 1 | C, D, F | 🟡 source-key-unverified | A company has a few AWS accounts for development and wants to move its production application to AWS. The compa… |
| Q547 | 3 | C | 🟡 source-key-unverified | A company has an organization in AWS Organizations that includes a separate AWS account for each of the company… |
| Q549 | 1 | C | 🟡 source-key-unverified | A company uses AWS Organizations for a multi-account setup in the AWS Cloud. The company's finance team has a d… |
| Q553 | 1 | A | 🟡 source-key-unverified | A financial company uses AWS Control Tower to govern multiple AWS accounts. The company must comply with data r… |
| Q554 | 1 | A | 🟡 source-key-unverified | A company is using AWS to develop and manage its production web application. The application includes an Amazon… |
| Q557 | 1 | B | 🟡 source-key-unverified | A company manages hundreds of AWS accounts centrally in an organization in AWS Organizations. The company recen… |
| Q558 | 1 | B | 🟡 source-key-unverified | A company has an organization in AWS Organizations. The company is using AWS Control Tower to deploy a landing … |
| Q559 | 1 | B | 🟡 source-key-unverified | A company has accounts in an organization in AWS Organizations. The organization has all features enabled. The … |
| Q561 | 1 | A | 🟡 source-key-unverified | A multinational media company is building a video processing platform on AWS. The platform is deployed across m… |
| Q568 | 1 | C, D | 🟡 source-key-unverified | A company's solutions architect is analyzing costs of a multi-application environment. The environment is deplo… |
| Q577 | 1 | B | 🟡 source-key-unverified | A company has more than 20 application development teams. All the teams use AWS CloudFormation to deploy applic… |
| Q580 | 1 | A, D | 🟡 source-key-unverified | A company uses an AWS CloudFormation template to deploy an Amazon ECS service into a production environment. Th… |
| Q582 | 1 | A, C, E | 🟡 source-key-unverified | A publishing company's design team updates the icons and other static assets that an ecommerce web application … |
| Q585 | 1 | A | 🟡 source-key-unverified | A company is deploying a third-party web application on AWS. The application is packaged as a Docker image. The… |
| Q589 | 1 | B | 🟡 source-key-unverified | A company needs to create and manage multiple AWS accounts for a number of departments from a central location… |
| Q590 | 3 | D | 🟡 source-key-unverified | A company has separate AWS accounts for each of its departments. The accounts are in OUs that are in an organiz… |
| Q591 | 3 | D | 🟡 source-key-unverified | A team collects and routes behavioral data for an entire company The company runs a Multi-AZ VPC environment wi… |
| Q593 | 1 | B | 🟡 source-key-unverified | A company is running multiple workloads in the AWS Cloud. The company has separate units for software developme… |
| Q595 | 3 | D | 🟡 source-key-unverified | A company has an environment that has a single AWS account. A solutions architect is reviewing the environment … |
| Q598 | 3 | B | 🟡 source-key-unverified | A company wants to change its internal cloud billing strategy for each of its business units. Currently, the cl… |
| Q600 | 3 | B, D | 🟡 source-key-unverified | A solutions architect is designing an AWS account structure for a company that consists of multiple teams. All … |
| Q602 | 3 | C | 🟡 source-key-unverified | A company uses an Amazon Redshift cluster to ingest data from various sources. The data is shared with other in… |
| Q603 | 1 | A | 🟡 source-key-unverified | A company uses Microsoft Active Directory for user management and Microsoft Entra ID as an identity provider (I… |
| Q605 | 3 | A | 🟡 source-key-unverified | A company hosts an intranet web application on Amazon EC2 instances behind an Application Load Balancer (ALB). … |
| Q606 | 1 | A | 🟡 source-key-unverified | A solutions architect is reviewing a company's process for taking snapshots of Amazon RDS DB instances. The com… |
| Q611 | 1 | C | 🟡 source-key-unverified | A company is using AWS Organizations lo manage multiple AWS accounts For security purposes, the company require… |
| Q617 | 3 | C | 🟡 source-key-unverified | A company is running several workloads in a single AWS account. A new company policy states that engineers can … |
| Q626 | 4 | D | 🟡 source-key-unverified | A company's solutions architect needs to provide secure Remote Desktop connectivity to users for Amazon EC2 Win… |
| Q627 | 3 | A | 🟡 source-key-unverified | A company needs to optimize the cost of an AWS environment that contains multiple accounts in an organization i… |
| Q629 | 1 | D | 🟡 source-key-unverified | A company is running applications on AWS in a multi-account environment. The company's sales team and marketing… |
| Q634 | 3 | C | 🟡 source-key-unverified | Example Corp uses an organization in AWS Organizations with all features enabled to manage multiple AWS account… |
| Q637 | 1 | C | 🟡 source-key-unverified | SIMULATION A research company conducts mathematical simulations in the AWS Cloud. The simulations run on severa… |
| Q644 | 1 | A, D, F | 🟡 source-key-unverified | Example Corp recently acquired AnyCompany, which has been operating its AWS workloads in a single account. Exam… |
| Q645 | 1 | A | 🟡 source-key-unverified | A company has hundreds of AWS accounts. The company uses an organization in AWS Organizations to manage all the… |
| Q654 | 4 | C | 🟡 source-key-unverified | A company has applications in an AWS account that is named Source. The account is in an organization in AWS Org… |
| Q657 | 2 | B | 🟡 source-key-unverified | An external audit of a company's serverless application reveals IAM policies that grant too many permissions. T… |
| Q666 | 1 | B, C, E | 🟡 source-key-unverified | A company has five development teams that have each created five AWS accounts to develop and host applications… |
| Q668 | 1 | C | 🟡 source-key-unverified | A retail company has structured its AWS accounts to be part of an organization in AWS Organizations. The compan… |

## 2. Hybrid networking, Direct Connect & VPN — 88 questions

| Q | Domain | Existing key* | Status | Scenario cue |
|---|---:|---|---|---|
| Q3 | 4 | D | 🔴 source-key-unverified | A company is migrating an application to the AWS Cloud. The application runs in an on- premises data center and… |
| Q7 | 4 | A | 🟢 source-key-unverified | A company operates an on-premises software-as-a-service (SaaS) solution that ingests several files daily. The c… |
| Q9 | 2 | A, D, E | 🟢 source-key-unverified | A company wants to back up its on-premises intranet application to the AWS Cloud. The company wants to use AWS … |
| Q20 | 1 | B | 🟢 aws-docs-reviewed-external-pending | A company operates hundreds of VPCs across AWS accounts. Private subnets currently reach the internet through N… |
| Q21 | 4 | B | 🟢 aws-docs-reviewed-external-pending | A company is migrating an on-premises web application to EC2 instances in private subnets behind a public Appli… |
| Q38 | 1 | A | 🟢 source-key-unverified | A company deploys its applications on Amazon EC2 instances in a VPC in the us-east-1 Region. The company recent… |
| Q43 | 3 | B | 🟢 source-key-unverified | A company recently wanted a web application from an on-premises data center to the AWS Cloud. The web applicati… |
| Q48 | 2 | B | 🟢 source-key-unverified | A company hosts a payment processing platform across multiple AWS Regions. The processing platform exposes paym… |
| Q49 | 1 | B | 🟢 source-key-unverified | How can applications in multiple AWS accounts privately access aPostgreSQL RDS instancein a separate AWS accoun… |
| Q59 | 1 | B | 🟢 source-key-unverified | A company is running an application in the AWS Cloud. The application consists of microservices that run on a f… |
| Q73 | 2 | A | 🟢 source-key-unverified | A company is building an application on AWS. The application sends logs to an Amazon Elasticsearch Service (Ama… |
| Q86 | 2 | C | 🟢 source-key-unverified | A company is running a two-tier web-based application in an on-premises data center. The application layer cons… |
| Q91 | 1 | C | 🟢 source-key-unverified | A company is migrating mobile banking applications to run on Amazon EC2 instances in a VPC. Backend service app… |
| Q96 | 1 | B | 🟢 source-key-unverified | A company needs to establish a connection from its on-premises data center to AWS. The company needs to connect… |
| Q102 | 4 | C | 🟡 aws-doc-verified-external-question-matched | A company is migrating an application from on-premises infrastructure to the AWS Cloud. During migration design… |
| Q106 | 4 | A, D, E | 🟡 source-key-unverified | A company wants to migrate its workloads from on premises to AWS. The workloads run on Linuxand Windows. The co… |
| Q128 | 4 | C | 🟡 aws-doc-verified-external-question-matched | A life sciences company is using a combination of open source tools to manage data analysis workflows and Docke… |
| Q134 | 4 | B | 🟡 aws-doc-verified-external-question-matched | A company is migrating an on-premises application and a MySQL database to AWS. The application processes highly… |
| Q161 | 4 | A | 🟡 verified-aws-doc-external-printed-key-b-incorrect-ocr-source | A company needs to migrate an on-premises SFTP site to AWS. The SFTP site currently runs on a Linux VM. Uploade… |
| Q171 | 4 | B | 🔴 verified-aws-doc-external-exact-match-ocr-warning | A company has an application that analyzes and stores image data on premises The application receives millions … |
| Q176 | 4 | D | 🔴 verified-intended-d-jar-war-source-defect | A company plans to migrate a legacy on-premises application to AWS. The application is a Java web application t… |
| Q185 | 4 | D | 🟡 verified-d-native-cloud-wan-dx-exact-external | A company runs payment gateways in multiple AWS Regions. The company also operates on-premises data centers whe… |
| Q193 | 3 | B | 🟡 source-key-unverified | A company needs its remote employees to access the web interface of an application. The company hosts the appli… |
| Q195 | 3 | B | 🟡 source-key-unverified | A company runs an application on an Amazon EC2 instance in a private VPC. The application accesses data from an… |
| Q208 | 4 | C | 🔴 aws-verified-c-external-match-pending | A company is planning to migrate its business-critical applications from an on-premises data center to AWS. The… |
| Q211 | 4 | B | 🟡 verified-b-aws-and-external | A company is storing data on premises on a Windows file server. The company produces 5 GB of new data daily. Th… |
| Q212 | 4 | C | 🔴 outdated-historical-c-new-customers-aws-transform | A company has on-premises Linux, Windows, and Ubuntu servers that run many applications. The servers run on phy… |
| Q217 | 4 | C | 🔴 outdated-defective-historical-c | A company is planning a one-time migration of an on-premises MySQL database to Amazon Aurora MySQL in the us-ea… |
| Q218 | 4 | D | 🟡 verified-d-aws-and-external-with-caveats | A company needs to move some on-premises Oracle databases to AWS. The company has chosen to keep some of the da… |
| Q220 | 4 | A | 🟡 aws-verified-a-external-match-pending | A company is migrating internal business applications to Amazon EC2 and Amazon RDS in a VPC. The migration requ… |
| Q228 | 4 | C | 🔴 verified-c-aws-external-legacy-name-defects | A company has more than 10.000 sensors that send data to an on-premises Apache Kafka server by using the Messag… |
| Q239 | 4 | B | 🟡 verified-b-aws-external-ha-config-caveat | An online retail company hosts its stateful web-based application and MySQL database in an on-premises data cen… |
| Q241 | 4 | B, C | 🟡 source-key-unverified | A company wants to establish a dedicated connection between its on-premises infrastructure and AWS. The company… |
| Q248 | 4 | A, D | 🟡 source-key-unverified | A financial company is planning to migrate its web application from on premises to AWS. The company uses a thir… |
| Q249 | 4 | A, D | 🟡 source-key-unverified | A company is migrating a legacy application from an on-premises data center to AWS. The application consists of… |
| Q259 | 3 | A | 🟡 source-key-unverified | A video processing company wants to build a machine learning (ML) model by using 600 TB of compressed data that… |
| Q268 | 4 | A, E | 🟡 source-key-unverified | A company is building a hybrid environment that includes servers in an on-premises data center and in the AWS C… |
| Q269 | 2 | D | 🟡 source-key-unverified | To abide by industry regulations, a solutions architect must design a solution that will store a company's crit… |
| Q272 | 4 | B | 🔴 reviewed-with-caveats | A company is moving a business-critical, multi-tier application to AWS. The architecture consists of a desktop … |
| Q301 | 4 | D | 🟡 reviewed-with-caveats | A retail company has an on-premises data center in Europe. The company also has a multi-Region AWS presence tha… |
| Q308 | 4 | A | 🟡 verified | A company with global offices has a single 1 Gbps AWS Direct Connect connection to a single AWS Region. The com… |
| Q309 | 1 | C | 🟡 source-key-unverified | A company is changing the way that it handles patching of Amazon EC2 instances in its application account. The … |
| Q324 | 4 | B | 🟡 verified | A company is planning to migrate its on-premises VMware cluster of 120 VMS to AWS. The VMS have many different … |
| Q349 | 3 | A | 🟡 source-key-unverified | A company that develops consumer electronics with offices in Europe and Asia has 60 TB of software images store… |
| Q354 | 3 | C | 🟡 source-key-unverified | A company has introduced a new policy that allows employees to work remotely from their homes if they connect b… |
| Q360 | 1 | D | 🟡 source-key-unverified | A company has a transit gateway that connects multiple VPCs in the same AWS Region. The company needs a central… |
| Q363 | 4 | B | 🔴 verified-with-outdated-alternatives | A company has developed a hybrid solution between its data center and AWS. The company uses Amazon VPC and Amaz… |
| Q376 | 4 | C | 🔴 verified-historical-outdated-service | A global manufacturing company plans to migrate the majority of its applications to AWS. However, the company i… |
| Q383 | 3 | A | 🟡 source-key-unverified | A company is building an application on AWS. The application sends logs to an Amazon OpenSearch Service cluster… |
| Q385 | 4 | C | 🟡 verified-with-api-key-security-caveat | A company has developed a mobile game. The backend for the game runs on several virtual machines located in an … |
| Q386 | 4 | A | 🟡 verified-with-os-configuration-caveat | A company is planning to migrate its on-premises data analysis application to AWS. The application is hosted ac… |
| Q409 | 4 | C | 🔴 aws-verified-external-variant-unconfirmed | A company maintains information on premises in approximately 1 million .csv files that are hosted on a VM. The … |
| Q420 | 4 | C | 🔴 verified-aws-and-external-with-cutover-caveat | A company wants to migrate its data analytics environment from on premises to AWS. The environment consists of … |
| Q421 | 4 | A | 🔴 verified-duplicate-of-Q386 | How should EC2 instances in AWS synchronize their clocks with an on-premises atomic clock NTP server, with the … |
| Q427 | 4 | A | 🔴 verified-corrected-source-key | A company has many services running in its on-premises data center. The data center is connected to AWS using A… |
| Q429 | 3 | B | 🟡 source-key-unverified | A company stores data on an Amazon RDS for PostgreSQL DB instance in a private subnet in an AWS database accoun… |
| Q430 | 1 | A | 🟡 source-key-unverified | A company needs to architect a hybrid DNS solution. This solution will use an Amazon Route 53 private hosted zo… |
| Q447 | 4 | C | 🔴 source-defective-intended-answer-c | A company has migrated a legacy application to the AWS Cloud. The application runs on three Amazon EC2 instance… |
| Q453 | 4 | B | 🔴 verified-aws-and-external | A company is running an application on Amazon EC2 instances in the AWS Cloud. The application is using a MongoD… |
| Q454 | 1 | B | 🟡 source-key-unverified | A company provides a centralized Amazon EC2 application hosted in a single shared VPC The centralized applicati… |
| Q470 | 3 | C | 🟡 source-key-unverified | How can a company patch EC2 instanceswithout internet access, using apatch source in another account, while acc… |
| Q491 | 4 | C | 🔴 verified-aws-and-external-with-caveats | A company is creating a solution that can move 400 employees into a remote working environment in the event of … |
| Q492 | 4 | B | 🔴 verified-aws-and-external-with-caveats | A company has developed a hybrid solution between its data center and AWS. The company uses Amazon VPC and Amaz… |
| Q506 | 4 | A | 🟡 source-key-unverified | A company has an on-premises Microsoft SOL Server database that writes a nightly 200 GB export to a local drive… |
| Q510 | 4 | B, D, E | 🟡 source-key-unverified | A company runs an intranet application on premises. The company wants to configure a cloud backup of the applic… |
| Q513 | 4 | C, E | 🟡 source-key-unverified | A company is planning to migrate its applications from an on-premises data center to AWS. The on-premises data … |
| Q530 | 3 | A, D | 🟡 source-key-unverified | A company has an on-premises monitoring solution using a PostgreSQL database for persistence of events. The dat… |
| Q536 | 4 | C, D | 🟡 source-key-unverified | A company is migrating its blog platform to AWS. The company's on-premises servers connect to AWS through an AW… |
| Q538 | 4 | A | 🟡 source-key-unverified | A company is designing an AWS environment tor a manufacturing application. The application has been successful … |
| Q540 | 1 | C | 🟡 source-key-unverified | A company uses AWS CloudFormation to deploy applications within multiple VPCs that are all attached to a transi… |
| Q548 | 3 | B, C, E | 🟡 source-key-unverified | A company runs workloads on EC2 inmultiple VPCsin a single Region. They also have anon-premises DNS server(via … |
| Q551 | 1 | A, C | 🟡 source-key-unverified | A software as a service (SaaS) company provides a media software solution to customers The solution is hosted o… |
| Q556 | 4 | A | 🟡 source-key-unverified | A company is migrating a legacy application from an on-premises data center to AWS. The application uses MongoD… |
| Q564 | 4 | D, E | 🟡 source-key-unverified | An online magazine will launch its latest edition this month. This edition will be the first to be distributed … |
| Q576 | 3 | A, E | 🟡 source-key-unverified | A company operates a static content distribution platform that serves customers globally. The customers consume… |
| Q581 | 4 | A, D | 🟡 source-key-unverified | A solutions architect needs to migrate an on-premises legacy application to AWS. The application runs on two se… |
| Q584 | 3 | B | 🟡 source-key-unverified | A software development company has multiple engineers who ate working remotely. The company is running Active D… |
| Q607 | 4 | B | 🟡 source-key-unverified | A solutions architect is redesigning a three-tier application that a company hosts onpremises. The application … |
| Q610 | 4 | B, D, F | 🟡 source-key-unverified | A company is migrating some of its applications to AWS. The company wants to migrate and modernize the applicat… |
| Q613 | 4 | B, D | 🟡 source-key-unverified | A company hosts a VPN in an on-premises data center. Employees currently connect to the VPN to access files in … |
| Q616 | 4 | D | 🟡 source-key-unverified | A company needs to migratesome Oracle databases to AWSwhile keeping otherson- premisesfor compliance. The on-pr… |
| Q620 | 3 | B | 🟡 source-key-unverified | A company plans to deploy a new private intranet service on Amazon EC2 instances inside a VPC. An AWS Site-to-S… |
| Q625 | 4 | B | 🟡 source-key-unverified | A telecommunications company is running an application on AWS. The company has set up an AWS Direct Connect con… |
| Q636 | 4 | A | 🟡 source-key-unverified | A company wants to migrate virtual Microsoft workloads from an on-premises data center to AWS The company has s… |
| Q664 | 3 | A, C | 🟡 source-key-unverified | A company wants to send data from its on-premises systems to Amazon S3 buckets. The company created the S3 buck… |
| Q667 | 2 | C | 🟡 source-key-unverified | A company is hosting a three-tier web application in an on-premises environment. Due to a recentsurge in traffi… |
| Q671 | 4 | A | 🟡 source-key-unverified | An online retail company is migrating its legacy on-premises .NET application to AWS. The application runs on l… |
| Q672 | 4 | A, C, F | 🟡 source-key-unverified | A company needs a hybrid DNS architecture. The architecture must include the company’s on-premises network and … |

## 3. VPC, PrivateLink, endpoints, DNS & routing — 148 questions

| Q | Domain | Existing key* | Status | Scenario cue |
|---|---:|---|---|---|
| Q5 | 3 | A | 🟢 source-key-unverified | A VPC spans three Availability Zones, each with public and private subnets. One NAT gateway and one internet ga… |
| Q11 | 2 | B | 🟢 source-key-unverified | A company hosts an application on AWS. The application reads and writes objects that are stored in a single Ama… |
| Q15 | 2 | C | 🟢 aws-docs-verified-study-wording | A video-on-demand application serves videos through an Amazon CloudFront distribution with a default cache beha… |
| Q18 | 3 | A, B | 🟢 aws-docs-reviewed-external-pending | An events company operates a ticketing platform on Amazon ECS backed by EC2 On-Demand instances in an Auto Scal… |
| Q19 | 2 | A, B, C | 🟢 aws-docs-reviewed-external-pending | A company hosts an API with a Regional Amazon API Gateway endpoint and AWS Lambda in one Region. The API calls … |
| Q24 | 3 | A | 🟢 aws-docs-reviewed-external-pending | A company runs EC2 applications in private VPC subnets that use NAT gateways across multiple Availability Zones… |
| Q27 | 3 | C | 🟢 source-key-unverified | A company’s web application uses an Amazon API Gateway API, AWS Lambda functions, and Amazon DynamoDB global ta… |
| Q30 | 2 | C | 🟢 source-key-unverified | An environmental company is deploying sensors in major cities throughout a country to measure air quality The s… |
| Q34 | 3 | B | 🔴 corrected-aws-docs | A company has a website that runs on Amazon EC2 instances behind an Application Load Balancer (ALB). The instan… |
| Q37 | 3 | D | 🟢 source-key-unverified | A company is creating a REST API to share information with six of its partners based in the United States. The … |
| Q47 | 3 | C | 🟢 source-key-unverified | A company needs to improve the security of its web application on AWS. The application runs on a fleet of Amazo… |
| Q53 | 3 | A | 🟢 source-key-unverified | A solutions architect has created a single VPC on AWS. The VPC has one internet gateway and one NAT gateway. Th… |
| Q57 | 3 | A | 🟢 source-key-unverified | A medical company is running a REST API on a set of Amazon EC2 instances The EC2 instances run in an Auto Scali… |
| Q58 | 2 | B | 🟢 source-key-unverified | A company needs to build a disaster recovery (DR) solution for its ecommerce website. The web application is ho… |
| Q60 | 3 | B, D, E | 🟢 source-key-unverified | A company wants to run a custom network analysis software package to inspect traffic as traffic leaves and ente… |
| Q63 | 3 | A, E | 🟡 source-key-unverified | A public retail web application uses an Application Load Balancer (ALB) in front of Amazon EC2 instances runnin… |
| Q64 | 2 | B | 🟢 source-key-unverified | A company is running an application in the AWS Cloud. The core business logic is running on a set of Amazon EC2… |
| Q70 | 2 | C | 🟢 source-key-unverified | A company has developed APIs that use Amazon API Gateway with Regional endpoints. The APIs call AWS Lambda func… |
| Q74 | 4 | A, C, E | 🟡 aws-doc-verified-external-question-matched | A company is planning to migrate an Amazon RDS for Oracle database to an RDS for PostgreSQL DB instance in anot… |
| Q78 | 3 | A | 🟢 source-key-unverified | A company has a complex web application that leverages Amazon CloudFront for global scalability and performance… |
| Q79 | 2 | C | 🟢 source-key-unverified | A financial services company in North America plans to release a new online web application to its customers on… |
| Q82 | 3 | A | 🟢 source-key-unverified | A company runs an application on Amazon EC2 and AWS Lambda. The application stores temporary data in Amazon S3… |
| Q90 | 3 | D | 🟢 source-key-unverified | A company has VPC flow logs enabled for its NAT gateway. The company is seeing Action = ACCEPT for inbound traf… |
| Q98 | 3 | A | 🟢 source-key-unverified | A company runs a website on Amazon ECS containers that use the AWS Fargate launch type. The company configures … |
| Q100 | 2 | A | 🟢 source-key-unverified | A company has an application that runs as a ReplicaSet of multiple pods in an Amazon Elastic Kubernetes Service… |
| Q107 | 3 | A | 🟡 source-key-unverified | A company is building a serverless application that runs on an AWS Lambda function that is attached to a VPC. T… |
| Q112 | 3 | C | 🟡 source-key-unverified | A company is hosting an image-processing service on AWS in a VPC. The VPC extends across two Availability Zones… |
| Q116 | 4 | A, D, E | 🟡 source-key-unverified | A company is migrating its on-premises IoT platform to AWS. The platform consists of the following components: … |
| Q119 | 4 | B, C, E | 🟡 source-key-unverified | A solutions architect needs to define a reference architecture for a solution for three-tier applications with … |
| Q123 | 3 | A | 🟡 source-key-unverified | A company hosts an ecommerce site using EC2, ALB, and DynamoDB in one AWS Region. The site uses a custom domain… |
| Q124 | 3 | A | 🟡 source-key-unverified | A company is using Amazon SageMaker A1 Notebook Instances and SageMaker APIs to train machine learning (ML) mod… |
| Q133 | 3 | A | 🟡 source-key-unverified | A company built an application based on AWS Lambda deployed in an AWS CloudFormation stack. The last production… |
| Q135 | 3 | B, D | 🟡 source-key-unverified | A company has an application that runs on a fleet of Amazon EC2 instances behind an Application Load Balancer (… |
| Q148 | 4 | C | 🔴 verified-aws-doc-external-exact-match-option-d-truncated | A company runs its sales reporting application in an AWS Region in the United States. The application uses an A… |
| Q149 | 3 | C | 🟡 source-key-unverified | A company runs a highly available data collection application on Amazon EC2 in the eu- north-1 Region. The appl… |
| Q158 | 3 | A, C | 🟡 source-key-unverified | A company is building an electronic document management system in which users upload their documents. The appli… |
| Q159 | 3 | A, C, E | 🟡 source-key-unverified | A company is designing a new website that hosts static content. The website will give users the ability to uplo… |
| Q160 | 4 | C | 🟡 aws-doc-verified-external-match-pending | A company has a payment gateway that processes millions of daily transactions on AWS. The solution uses Amazon … |
| Q165 | 3 | C | 🟡 source-key-unverified | A company runs an unauthenticated static website (www.example.com) that includes a registration form for users… |
| Q175 | 3 | B, E | 🟡 source-key-unverified | A company is running a serverless application that consists of several AWS Lambda functions and Amazon DynamoDB… |
| Q179 | 3 | B | 🟡 source-key-unverified | A company is using Amazon API Gateway to deploy a private REST API that will provide access to sensitive data. … |
| Q182 | 3 | A, D, E | 🟡 source-key-unverified | A company is using a single AWS Region for its ecommerce website. The website includes a web application that r… |
| Q183 | 4 | B | 🔴 verified-b-aws-doc-exact-external-minor-wording | A company runs a test application on an Amazon EC2 instance. Testing clients across the United States send data… |
| Q187 | 3 | B | 🟡 source-key-unverified | A North American company with headquarters on the East Coast is deploying a new web application running on Amaz… |
| Q188 | 1 | A, C, D | 🟡 source-key-unverified | A company has deployed an application on AWS Elastic Beanstalk. The application uses Amazon Aurora for the data… |
| Q200 | 4 | C | 🟡 aws-verified-c-external-match-pending-caveats | A company runs an ecommerce website on Amazon ECS behind an Application Load Balancer (ALB). The company stores… |
| Q204 | 1 | A | 🟡 source-key-unverified | A company is planning to host a web application on AWS and works to load balance the traffic across a group of … |
| Q206 | 3 | B | 🟡 source-key-unverified | An online survey company runs its application in the AWS Cloud. The application is distributed and consists of … |
| Q215 | 3 | D | 🟡 source-key-unverified | A company is hosting a monolithic REST-based API for a mobile app on five Amazon EC2 instances in public subnet… |
| Q232 | 1 | A, D, F | 🟡 source-key-unverified | A company uses multiple software as a service SaaS applications for messaging, email, and file sharing. The Saa… |
| Q233 | 3 | D | 🟡 source-key-unverified | A company runs an ecommerce web application on AWS. The static website is hosted on Amazon S3 and served via Am… |
| Q235 | 3 | A | 🟡 source-key-unverified | A solutions architect has an operational workload deployed on Amazon EC2 instances in an Auto Scaling Group The… |
| Q242 | 4 | C | 🔴 best-intended-c-aws-external-rto-not-guaranteed | A company implements a containerized application by using Amazon Elastic Container Service (Amazon ECS) and Ama… |
| Q245 | 3 | B | 🟡 source-key-unverified | A company plans to refactor a monolithic application into a modern application designed deployed or AWS. The CL… |
| Q246 | 2 | B | 🟡 source-key-unverified | A company has a serverless application comprised of Amazon CloudFront, Amazon API Gateway, and AWS Lambda funct… |
| Q247 | 3 | A, B | 🟡 source-key-unverified | A company has an application that runs on Amazon EC2 instances. A solutions architect is designing VPC infrastr… |
| Q250 | 3 | D | 🟡 source-key-unverified | A large company is running a popular web application. The application runs on several Amazon EC2 Linux Instance… |
| Q261 | 3 | B | 🟡 source-key-unverified | A company is serving files to its customers through an SFTP server that is accessible over the internet The SFT… |
| Q271 | 3 | D | 🟡 source-key-unverified | A team of data scientists is using Amazon SageMaker instances and SageMaker APIs to train machine learning (ML)… |
| Q273 | 3 | C | 🟡 source-key-unverified | A company hosts a blog post application on AWS using Amazon API Gateway, Amazon DynamoDB, and AWS Lambda. The a… |
| Q275 | 3 | C | 🟡 source-key-unverified | A company is running its solution on AWS in a manually created VPC. The company is using AWS CloudFormation to … |
| Q278 | 4 | C | 🟡 reviewed-with-caveats | A company is creating a sequel for a popular online game. A large number of users from all over the world will … |
| Q280 | 3 | B | 🟡 source-key-unverified | A company's interactive web application uses an Amazon CloudFront distribution to serve images from an Amazon S… |
| Q284 | 3 | A | 🟡 source-key-unverified | A company needs to improve the security of its web-based application on AWS. The application uses Amazon CloudF… |
| Q285 | 3 | C | 🟡 source-key-unverified | A company is providing weather data over a REST-based API to several customers. The API is hosted by Amazon API… |
| Q287 | 3 | D | 🟡 source-key-unverified | A company runs a software-as-a-service <SaaS) application on AWS The application consists of AWS Lambda functio… |
| Q290 | 4 | C | 🔴 reviewed-with-caveats | A company used Amazon EC2 instances to deploy a web fleet to host a blog site The EC2 instances are behind an A… |
| Q294 | 2 | C | 🟡 source-key-unverified | A company is building an image service on the web that will allow users to upload and search random photos. At … |
| Q305 | 3 | A, D | 🟡 source-key-unverified | A video streaming company recently launched a mobile app for video sharing. The app uploads various files to an… |
| Q312 | 3 | D | 🟡 source-key-unverified | A company runs an ecommerce web application on AWS. The web application is hosted as a static website on Amazon… |
| Q317 | 3 | A | 🟡 source-key-unverified | An adventure company has launched a new feature on its mobile app. Users can use the feature to upload their hi… |
| Q318 | 3 | A | 🟡 source-key-unverified | A company is developing a serverless application that runs in a VPC. The VPC has public and private IPv4 subnet… |
| Q321 | 4 | A, D, F | 🟡 source-key-unverified | A company is running a three-tier web application in an on-premises data center. The frontend is a PHP applicat… |
| Q328 | 3 | A, B, D | 🟡 source-key-unverified | A company built an ecommerce website on AWS using a three-tier web architecture. The application is Java-based … |
| Q333 | 2 | D | 🟡 source-key-unverified | A financial services company runs a complex, multi-tier application on Amazon EC2 instances and AWS Lambda func… |
| Q334 | 4 | D | 🟡 verified | A company has application services that have been containerized and deployed on multiple Amazon EC2 instances w… |
| Q338 | 3 | B | 🟡 source-key-unverified | A company operates an API service in the AWS Cloud. The service is based on an Amazon API Gateway REST API that… |
| Q341 | 4 | B | 🟡 verified-with-caveats | A company has a multi-tier web application that runs on a fleet of Amazon EC2 instances behind an Application L… |
| Q346 | 4 | A, D | 🟡 source-key-unverified | A company hosts a game player-matching service on a public-facing, physical, on- premises instance that all use… |
| Q356 | 3 | C | 🟡 source-key-unverified | A company runs an application on a fleet of Amazon EC2 instances that are in private subnets behind an internet… |
| Q366 | 3 | A | 🟡 source-key-unverified | A company operates a proxy server on a fleet of Amazon EC2 instances. Partners in different countries use the p… |
| Q374 | 4 | B | 🟡 verified-with-privacy-caveats | A global company operates a platform that serves customers across multiple AWS Regions. The platform stores cus… |
| Q375 | 1 | A, C, F | 🟡 source-key-unverified | A company is deploying a third-party firewall appliance solution from AWS Marketplace to monitor and protect tr… |
| Q387 | 3 | D | 🟡 source-key-unverified | A company hosts a read-heavy web application on Amazon EKS and Amazon DynamoDB. The company uses Amazon Route 5… |
| Q388 | 3 | D, E | 🟡 source-key-unverified | A solutions architect has deployed a web application that serves users across two AWS Regionsunder a custom dom… |
| Q392 | 3 | A | 🟡 source-key-unverified | A company is building an application that will run on an AWS Lambda function. Hundreds of customers will use th… |
| Q396 | 3 | C, E, F | 🟡 source-key-unverified | A company has registered 10 new domain names. The company uses the domains for online marketing. The company ne… |
| Q397 | 3 | A | 🟡 source-key-unverified | A company is using Amazon SageMaker AI Notebook Instances and SageMaker APIs to train machine learning models. … |
| Q402 | 3 | A | 🟡 source-key-unverified | A company completed a successful Amazon Workspaces proof of concept. They now want to make Workspaceshighly ava… |
| Q410 | 3 | C | 🟡 source-key-unverified | A company is running a workload that consists of thousands of Amazon EC2 instances. The workload is running in … |
| Q411 | 3 | B | 🟡 source-key-unverified | A company provides a software as a service (SaaS) application that runs in the AWS Cloud. The application runs … |
| Q412 | 3 | A | 🟡 source-key-unverified | A company runs an application on Amazon EC2 and AWS Lambda. The application stores temporary data in Amazon 53… |
| Q417 | 2 | C | 🟡 source-key-unverified | A company is launching a new online game on Amazon EC2 instances. The game must be available globally. The comp… |
| Q424 | 4 | C | 🔴 verified-aws-and-external | A global media company is planning a multi-Region deployment of an application. Amazon DynamoDB global tables w… |
| Q425 | 3 | C, E | 🟡 source-key-unverified | A company is using multiple AWS accounts The DNS records are stored in a private hosted zone for Amazon Route 5… |
| Q428 | 3 | B, E | 🟡 source-key-unverified | An application uses CloudFront, App Runner, and two S3 buckets — one for static assets and one for user-uploade… |
| Q438 | 4 | B, D, E | 🟡 source-key-unverified | A company has an loT platform that runs in an on-premises environment. The platform consists of a server that c… |
| Q441 | 3 | C | 🟡 source-key-unverified | A company has developed a new release of a popular video game and wants to make it available for public downloa… |
| Q446 | 3 | B | 🟡 source-key-unverified | A company runs a processing engine in the AWS Cloud. The engine processes environmental data from logistics cen… |
| Q461 | 2 | B | 🟡 source-key-unverified | A company runs a new application as a static website in Amazon S3. The company has deployed the application to … |
| Q462 | 4 | B | 🔴 verified-aws-with-external-stem-match | A company hosts a multi-tier data processing application that consists of a static web application frontend and… |
| Q464 | 3 | D | 🟡 source-key-unverified | A company has a website that serves many visitors. The company deploys a backend service for the website in a p… |
| Q467 | 3 | A | 🟡 source-key-unverified | A company runs an loT application in the AWS Cloud. The company has millions of sensors that collect data from … |
| Q469 | 3 | D, E, F | 🟡 source-key-unverified | A company stores a static website on Amazon S3. AWS Lambda functions retrieve content from an S3 bucket and ser… |
| Q477 | 3 | B | 🟡 source-key-unverified | A finance company hosts a data lake in Amazon S3. The company receives financial data records over SFTP each ni… |
| Q481 | 4 | A | 🟡 verified-aws-and-external-with-caveats | A solutions architect is reviewing an application's resilience before launch. The application runs on an Amazon… |
| Q485 | 4 | B | 🟡 verified-aws-and-external-with-caveats | A company hosts a web application on AWS in the us-east-1 Region. The application servers are distributed acros… |
| Q487 | 4 | B | 🔴 corrected-aws-verified | A company plans to migrate a three-tiered web application from an on-premises data center to AWS. The company d… |
| Q488 | 3 | C | 🟡 source-key-unverified | A company runs a latency-sensitive application that consumes messages from an Amazon Managed Streaming for Apac… |
| Q489 | 1 | A | 🟡 source-key-unverified | A company owns a chain of travel agencies and is running an application in the AWS Cloud. Company employees use… |
| Q490 | 3 | C | 🟡 source-key-unverified | A company's solutions architect is reviewing a web application that runs on AWS. The application references sta… |
| Q494 | 2 | B | 🟡 source-key-unverified | A company is running a web application in the AWS Cloud. The application consists of dynamic content that is cr… |
| Q496 | 3 | C | 🟡 source-key-unverified | A company deploys workloads in multiple AWS accounts. Each account has a VPC with VPC flow logs published in te… |
| Q499 | 3 | B | 🟡 source-key-unverified | A company is running a critical stateful web application on two Linux Amazon EC2 instances behind an Applicatio… |
| Q514 | 4 | D | 🟡 source-key-unverified | A company’s solutions architect is evaluating an AWS workload that was deployed several years ago. The applicat… |
| Q519 | 3 | A, C | 🟡 source-key-unverified | A company is storing data in several Amazon DynamoDB tables. A solutions architect must use a serverless archit… |
| Q521 | 1 | C | 🟡 source-key-unverified | A company is deploying a third-party web application to an AWS account. The company wants to deploy the applica… |
| Q528 | 4 | A | 🟡 source-key-unverified | A company runs a workload in the AWS Cloud. The company stores data for the application in an older version of … |
| Q534 | 3 | B | 🟡 source-key-unverified | A solutions architect must update an application environment within AWS Elastic Beanstalk using a blue/green de… |
| Q535 | 1 | B | 🟡 source-key-unverified | A company mandates that all internal AWS communications useprivate IPs. A solutions architect createdinterface … |
| Q546 | 3 | B | 🟡 source-key-unverified | A solutions architect is determining the DNS strategy for an existing VPC. The VPC is provisioned to use the 10… |
| Q555 | 4 | A, C | 🟡 source-key-unverified | A company's AWS environment includes an Amazon RDS for MySQL database in a Multi- AZ deployment and an Amazon E… |
| Q562 | 3 | A | 🟡 source-key-unverified | A company has implemented a new security requirement According to the new requirement, the company must scan al… |
| Q565 | 1 | A | 🟡 source-key-unverified | A company runs a processing engine in the AWS Cloud The engine processes environmental data from logistics cent… |
| Q571 | 4 | D | 🟡 source-key-unverified | A company uses a service to collect metadata from applications that the company hosts on premises. Consumer dev… |
| Q574 | 3 | C | 🟡 source-key-unverified | A company is developing a solution to analyze images. The solution uses a 50 TB reference dataset and analyzes … |
| Q587 | 3 | A | 🟡 source-key-unverified | A company that is developing a mobile game is making game assets available in two AWS Regions. Game assets are … |
| Q592 | 3 | B, D | 🟡 source-key-unverified | A weather service provides high-resolution weather maps from a web application hosted on AWS in the eu-west-1 R… |
| Q596 | 3 | C | 🟡 source-key-unverified | A company uses Amazon CloudFront to serve a static application from an Amazon S3 bucket origin. A custom domain… |
| Q599 | 1 | A, C | 🟡 source-key-unverified | A company is creating a centralized logging service running on Amazon EC2 that will receive and analyze logs fr… |
| Q604 | 3 | C | 🟡 source-key-unverified | A company needs to improve the reliability ticketing application. The application runs on an Amazon Elastic Con… |
| Q612 | 1 | B | 🟡 source-key-unverified | A company hosts an application on AWS. The application uses AWS Lambda functions that are invoked by an Amazon … |
| Q621 | 3 | B | 🟡 source-key-unverified | A company runs a web application on AWS. The web application delivers static content from an Amazon S3 bucket t… |
| Q628 | 3 | C, E | 🟡 source-key-unverified | A solutions architect is designing an application to accept timesheet entries from employees on their mobile de… |
| Q631 | 3 | C | 🟡 source-key-unverified | A company is running a web application in a VPC. The web application runs on a group of Amazon EC2 instances be… |
| Q632 | 3 | A | 🟡 source-key-unverified | A company built an application based on AWS Lambda deployed in an AWS CloudFormation stack. The last production… |
| Q639 | 3 | A, D | 🟡 source-key-unverified | A company has a critical application in which the data tier is deployed in a single AWS Region. The data tier u… |
| Q641 | 3 | A, E | 🟡 source-key-unverified | A company is updating an application that customers use to make online orders. The number of attacks on the app… |
| Q642 | 3 | C | 🟡 source-key-unverified | A mobile gaming company is expanding into the global market. The company's game servers run in the us-east-1 Re… |
| Q648 | 3 | C | 🟡 source-key-unverified | A company provides auction services for artwork and has users across North America and Europe. The company host… |
| Q649 | 3 | C, E | 🟡 source-key-unverified | A retail company is operating its ecommerce application on AWS. The application runs on Amazon EC2 instances be… |
| Q650 | 2 | C | 🟡 source-key-unverified | A company needs to implement a disaster recovery (DR) plan for a web application. The application runs in a sin… |
| Q655 | 3 | B | 🟡 source-key-unverified | An education company is running a web application used by college students around the world. The application ru… |
| Q656 | 3 | C | 🟡 source-key-unverified | A software-as-a-service (SaaS) provider exposes APIs through an Application Load Balancer (ALB). The ALB connec… |
| Q659 | 3 | B | 🟡 source-key-unverified | A company has an asynchronous HTTP application that is hosted as an AWS Lambda function. A public Amazon API Ga… |
| Q663 | 1 | D | 🟡 source-key-unverified | A global company has a mobile app that displays ticket barcodes. Customers use the tickets on the mobile app to… |
| Q665 | 3 | D | 🟡 source-key-unverified | A company is building a call center by using Amazon Connect. The company’s operations team is defining a disast… |
| Q669 | 4 | A, C, F | 🟡 source-key-unverified | A company runs an application in (he cloud that consists of a database and a website Users can post data to the… |

## 4. Security, encryption, secrets & certificates — 30 questions

| Q | Domain | Existing key* | Status | Scenario cue |
|---|---:|---|---|---|
| Q1 | 3 | B | 🟢 source-key-unverified | A company has millions of objects in an Amazon S3 bucket. The objects are in the S3 Standard storage class. All… |
| Q39 | 2 | B | 🟢 source-key-unverified | A company is developing a web application that runs on Amazon EC2 instances in an Auto Scaling group behind a p… |
| Q41 | 3 | B | 🟢 source-key-unverified | A company runs a serverless ecommerce application on AWS. The application uses API Gateway to invoke Java Lambd… |
| Q95 | 2 | D | 🔴 disputed-no-valid-option | A health insurance company stores personally identifiable information (PII) in an Amazon S3 bucket. The company… |
| Q110 | 3 | B | 🟡 source-key-unverified | A company is running an application that uses an Amazon ElastiCache for Redis cluster as a caching layer A rece… |
| Q115 | 3 | A, C | 🟡 source-key-unverified | A healthcare company is designing a patient portal. The portal must use a database to store patient data. The p… |
| Q121 | 3 | A | 🟡 source-key-unverified | A company has Linux-based Amazon EC2 instances. Users must access the instances by using SSH with EC2 SSH Key p… |
| Q162 | 3 | C | 🟡 source-key-unverified | A company hosts its primary API on AWS using Amazon API Gateway and AWS Lambda functions. Internal applications… |
| Q219 | 3 | A | 🟡 source-key-unverified | A company has developed a web application. The company is hosting the application on a group of Amazon EC2 inst… |
| Q255 | 3 | C | 🟡 source-key-unverified | A company is building a solution in the AWS Cloud. Thousands or devices will connect to the solution and send d… |
| Q300 | 4 | B | 🟡 reviewed-with-caveats | A company wants to retire its Oracle Solaris NFS storage arrays. The company requires rapid data migration over… |
| Q307 | 3 | A | 🟡 source-key-unverified | IoT sensors are manufactured with certificates from a private CA. They must only connect to AWS after physical … |
| Q313 | 2 | B | 🟡 source-key-unverified | A company is deploying a new application on AWS. The application consists of an Amazon EKS cluster and an Amazo… |
| Q348 | 3 | C | 🟡 source-key-unverified | A company's public API runs as tasks on Amazon Elastic Container Service (Amazon ECS). The tasks run on AWS Far… |
| Q352 | 2 | C | 🟡 source-key-unverified | A company stores application data in many Amazon S3 buckets in one AWS account. Some of the S3 buckets contain … |
| Q358 | 1 | C | 🟡 source-key-unverified | A company needs to use an AWS Transfer Family SFTP-enabled server with an Amazon S3 bucket to receive updates f… |
| Q371 | 3 | B | 🟡 source-key-unverified | A security engineer determined that an existing application retrieves credentials to an Amazon RDS for MySQL da… |
| Q380 | 3 | B | 🟡 source-key-unverified | A company runs an application on AWS. The application uses an Amazon Aurora MySQL database that is encrypted wi… |
| Q426 | 3 | C | 🟡 source-key-unverified | A company needs to monitor a growing number of Amazon S3 buckets across two AWS Regions. The company also needs… |
| Q443 | 3 | D | 🟡 source-key-unverified | A company's compliance audit reveals that some Amazon Elastic Block Store (Amazon EBS) volumes that were create… |
| Q449 | 1 | D | 🟡 source-key-unverified | A company uses a load balancer to distribute traffic to Amazon EC2 instances in a single Availability Zone. The… |
| Q457 | 1 | B, D, E | 🟡 source-key-unverified | A company has several AWS Lambda functions written in Python. The functions are deployed with the .zip package … |
| Q502 | 4 | B | 🟡 source-key-unverified | A company is migrating an application to AWS. It wants to use fully managed services as much as possible during… |
| Q507 | 1 | B | 🟡 source-key-unverified | A company is deploying AWS Lambda functions that access an Amazon RDS for PostgreSQL database. The company need… |
| Q511 | 4 | B | 🟡 source-key-unverified | A company needs to migrate its customer transactions database from on premises to AWS. The database resides on … |
| Q532 | 3 | A | 🟡 source-key-unverified | A company wants to use Amazon Workspaces in combination with thin client devices to replace aging desktops. Emp… |
| Q597 | 1 | C | 🟡 source-key-unverified | A financial services company receives a regular data feed from its credit card servicing partner Approximately … |
| Q609 | 3 | A | 🟡 source-key-unverified | A solutions architect needs to improve an application that is hosted in the AWS Cloud. The application uses an … |
| Q658 | 3 | D | 🟡 source-key-unverified | A company deploys a new web application. As pari of the setup, the company configures AWS WAF to log to Amazon … |
| Q662 | 3 | D | 🟡 source-key-unverified | A company creates an Amazon API Gateway API and shares the API with an external development team. The API uses … |

## 5. Amazon S3, lifecycle, replication & object storage — 82 questions

| Q | Domain | Existing key* | Status | Scenario cue |
|---|---:|---|---|---|
| Q8 | 2 | D | 🟢 source-key-unverified | A company wants to use AWS for disaster recovery for an on-premises application. The company has hundreds of Wi… |
| Q17 | 3 | A | 🟢 aws-docs-reviewed-external-pending | A company runs a data-intensive monthly reporting job on hundreds of EC2 instances. Its shared file system, hos… |
| Q32 | 3 | C, E | 🟢 source-key-unverified | A company has an application that stores user-uploaded videos in an Amazon S3 bucket that uses S3 Standard stor… |
| Q35 | 3 | C | 🟢 source-key-unverified | A company migrated its antivirus solution for 10,000 Amazon EC2 instances to a new software as a service SaaS s… |
| Q42 | 2 | B | 🟢 source-key-unverified | A company is developing a gene reporting device that will collect genomic information to assist researchers wit… |
| Q61 | 2 | C | 🔴 corrected-aws-docs | A company uses an AWS CodeCommit repository The company must store a backup copy of the data that is in the rep… |
| Q62 | 4 | D | 🟢 domain4-aws-docs-reviewed | A company has an application that uses an on-premises Oracle database. The company is migrating the database to… |
| Q66 | 4 | B | 🔴 domain4-answer-corrected-source-option-invalid | A company is migrating a document processing workload to AWS. The company has updated many applications to nati… |
| Q72 | 3 | B | 🟢 source-key-unverified | A company is using AWS CodePipeline for the CI/CD of an application to an Amazon EC2 Auto Scaling group. All AW… |
| Q83 | 3 | C, E | 🟢 source-key-unverified | A company has an application that stores user-uploaded videos in an Amazon S3 bucket using S3 Standard storage… |
| Q85 | 3 | C | 🟢 source-key-unverified | A company runs AWS workloads that are integrated with software as a service (SaaS) applications. The company ne… |
| Q94 | 2 | A, C | 🔴 disputed-wording | A company runs a serverless application in a single AWS Region. The application accesses external URLs and extr… |
| Q130 | 3 | B | 🟡 source-key-unverified | A company has an application that is deployed on Amazon EC2 instances behind an Application Load Balancer (ALB)… |
| Q132 | 2 | C | 🟡 source-key-unverified | An international delivery company hosts a delivery management system on AWS. Drivers use the system to upload c… |
| Q142 | 4 | D | 🔴 aws-doc-verified-external-question-matched-outdated-service | A company is planning to migrate 1,000 on-premises servers to AWS. The servers run on several VMware clusters i… |
| Q166 | 3 | C | 🟡 source-key-unverified | A company is developing an application that will display financial reports. The company needs a solution that c… |
| Q177 | 3 | B, E | 🟡 source-key-unverified | A company runs a web-crawling process on a list of target URLs to obtain training documents for machine learnin… |
| Q202 | 4 | B | 🟡 aws-verified-b-external-match-pending | A company wants to migrate its website from its on-premises data center to AWS. The website service APIs are ho… |
| Q205 | 3 | C | 🟡 source-key-unverified | A company needs to gather data from an experiment in a remote location that does not have internet connectivity… |
| Q222 | 3 | A | 🟡 source-key-unverified | A company uses a software package for surveys. During surveys, data is uploaded from a field operator's device … |
| Q234 | 3 | A | 🟡 source-key-unverified | A company is using AWS CloudFormation as its deployment tool for all applications. It stages all application bi… |
| Q236 | 3 | C | 🟡 source-key-unverified | A company wants to refactor its retail ordering web application that currently has a load- balanced Amazon EC2 … |
| Q240 | 4 | B | 🔴 verified-b-aws-conflicting-external-key-d | A manufacturing company is building an inspection solution for its factory. The company has IPcameras at the en… |
| Q260 | 3 | D | 🟡 source-key-unverified | A company gives users the ability to upload images from a custom application. The upload process invokes an AWS… |
| Q266 | 4 | B | 🔴 corrected-b-aws-external-key-d-defective | A company is planning to migrate workloads from its on-premises data center to Amazon EC2 instances. The worklo… |
| Q281 | 4 | B | 🟡 reviewed-with-caveats | A company is migrating a document processing workload to AWS. Client applications upload documents to an Amazon… |
| Q286 | 4 | B | 🟡 reviewed-with-caveats | A company is planning to migrate its on-premises transaction-processing application to AWS. The application run… |
| Q288 | 3 | B | 🟡 source-key-unverified | A flood monitoring agency has deployed more than 10.000 water-level monitoring sensors. Sensors send continuous… |
| Q297 | 2 | A, B | 🟡 source-key-unverified | A video processing company has an application that downloads images from an Amazon S3 bucket, processes the ima… |
| Q298 | 4 | B | 🟡 reviewed-with-caveats | A company needs to modernize an application and migrate the application to AWS. The application stores user pro… |
| Q306 | 4 | C | 🟡 reviewed-with-caveats | A company is migrating its on-premises file transfer solution to AWS Transfer Family. The current system includ… |
| Q314 | 3 | C | 🟡 source-key-unverified | A company wants to design a disaster recovery (DR) solution for an application that runs in the company's data … |
| Q320 | 4 | C | 🟡 verified | A global company runs an analytics application on Amazon EC2 for computing. The company uses Amazon EBS as prim… |
| Q323 | 3 | B, D | 🟡 source-key-unverified | A media storage application uploads user photos to Amazon S3 for processing by AWS Lambda functions. Applicatio… |
| Q330 | 3 | C | 🟡 source-key-unverified | A company hosts a ticketing service on a fleet of Linux Amazon EC2 instances that are in an Auto Scaling group… |
| Q331 | 3 | A, D, F | 🟡 source-key-unverified | A company is storing sensitive data in an Amazon S3 bucket. The company must log all activities for objects in … |
| Q343 | 3 | B | 🟡 source-key-unverified | A company is developing a new serverless API by using Amazon API Gateway and AWS Lambda. The company integrated… |
| Q353 | 3 | A, C | 🟡 source-key-unverified | A travel company built a web application that uses Amazon SES to send email notifications to users. The company… |
| Q365 | 4 | A, C | 🟡 source-key-unverified | A company needs to store sensitive and crucial business data in an Amazon S3 bucket. Because of the criticality… |
| Q367 | 4 | D | 🟡 verified-with-wording-caveat | A company has migrated its forms-processing application to AWS. When users interact with the application, they … |
| Q390 | 3 | A, B, E | 🟡 source-key-unverified | A solutions architect is creating an application that stores objects in an Amazon S3 bucket The solutions archi… |
| Q391 | 3 | C | 🟡 source-key-unverified | A company runs an application on AWS. The company curates data from several different sources. The company uses… |
| Q399 | 3 | B | 🟡 source-key-unverified | A company ingests and processes streaming market data. The data rate is constant. A nightly process that calcul… |
| Q401 | 4 | A, D, E | 🟡 source-key-unverified | A company generates approximately 20 GB of data multiple times each day. The company uses AWS DataSync to copy … |
| Q403 | 3 | C | 🟡 source-key-unverified | A company is running an application in the AWS Cloud. The application collects and stores a large amount of uns… |
| Q405 | 3 | D | 🟡 source-key-unverified | A company is deploying a newbig data analytics clusteracross multiple Availability Zones. All nodes must havere… |
| Q413 | 4 | C | 🔴 aws-verified-external-variant-unconfirmed | A company is running a containerized workload on AWS. The workload consists of several data-processing services… |
| Q418 | 3 | B | 🟡 source-key-unverified | A solutions architect is designing the data storage and retrieval architecture for a new application that a com… |
| Q419 | 3 | A | 🟡 source-key-unverified | A company has purchased appliances from different vendors. The appliances all have loT sensors. The sensors sen… |
| Q431 | 3 | B | 🟡 source-key-unverified | An application is using an Amazon RDS for MySQL Multi-AZ DB instance in the us-east-1 Region. After a failover … |
| Q434 | 4 | A | 🔴 verified-aws-and-external-with-conflicting-source | A company runs a Python script on an Amazon EC2 instance to process data. The script runs every 10 minutes. The… |
| Q445 | 4 | C | 🔴 verified-aws-and-external-with-trigger-caveat | A company is migrating its on-premises file transfer solution to AWS Transfer Family. The on-premises host incl… |
| Q448 | 4 | C | 🟡 verified-corrected-source-key | A company hosts a data-processing application on Amazon EC2 instances. The application polls an Amazon Elastic … |
| Q460 | 4 | C | 🟡 verified-aws-and-external-with-caveats | A company needs to implement disaster recovery for a critical application that runs in a single AWS Region. The… |
| Q479 | 4 | D | 🔴 verified-aws-and-external-with-caveats | A company is planning to migrate an application from on premises to the AWS Cloud. The company will begin the m… |
| Q495 | 4 | D | 🟡 verified-aws-and-external-with-caveats | A scientific company needs to process text and image data from an Amazon S3 bucket. The data is collected from … |
| Q497 | 4 | B, D | 🟡 source-key-unverified | A company has migrated an application from on premises to AWS. The application frontend is a static website tha… |
| Q498 | 4 | B | 🟡 source-key-unverified | A company is running an application on premises. The application uses a set of web servers that host a static R… |
| Q504 | 4 | C | 🟡 source-key-unverified | A global ecommerce company has many data centers around the world. With the growth of its stored data, the comp… |
| Q515 | 3 | A | 🟡 source-key-unverified | A company has a sales system that stores transactions as .csv files in an Amazon S3 bucket. The S3 bucket is co… |
| Q517 | 4 | B | 🟡 source-key-unverified | A company has developed an application that is running Windows Server on VMware vSphere VMs that the company ho… |
| Q524 | 3 | B | 🟡 source-key-unverified | A company is collecting a large amount of data from a fleet of loT devices Data is stored as Optimized Row Colu… |
| Q527 | 4 | D | 🟡 source-key-unverified | A software as a service (SaaS) based company provides a case management solution to customers A3 part of the so… |
| Q529 | 3 | D | 🟡 source-key-unverified | A SaaS web app runs on EC2 Linux behind an ALB. It storesuser sessionsin an RDS Multi- AZ database. During high… |
| Q539 | 3 | C | 🟡 source-key-unverified | A company needs to optimize the infrastructure for an application that uploads data to Amazon S3. The uploads a… |
| Q542 | 1 | B, C, E | 🟡 source-key-unverified | A company needs to store and process image data that will be uploaded from mobile devices using a custom mobile… |
| Q544 | 3 | B | 🟡 source-key-unverified | An online gaming company needs to optimize the cost of its workloads on AWS. The company uses a dedicated accou… |
| Q560 | 4 | B | 🟡 source-key-unverified | A solutions architect is planning to migrate critical Microsoft SOL Server databases to AWS. Because the databa… |
| Q578 | 4 | D | 🟡 source-key-unverified | A solutions architect needs to advise a company on how to migrate its on-premises data processing application t… |
| Q579 | 2 | B | 🟡 source-key-unverified | A company is using Amazon OpenSearch Service to analyze data. The company loads data into an OpenSearch Service… |
| Q583 | 4 | B | 🟡 source-key-unverified | A company manufactures smart vehicles. The company uses a custom application to collect vehicle data. The vehic… |
| Q586 | 3 | B | 🟡 source-key-unverified | A company needs to run large batch-processing jobs on data that is stored in an Amazon S3 bucket. The jobs perf… |
| Q594 | 3 | C | 🟡 source-key-unverified | A company has a web application that allows users to upload short videos. The videos are stored on Amazon EBS v… |
| Q601 | 4 | C | 🟡 source-key-unverified | A company is migrating infrastructure for its massive multiplayer game to AWS. The game's application features … |
| Q615 | 4 | E | 🟡 source-key-unverified | A company wants to use Amazon S3 to back up its on-premises file storage solution. The company's on-premises fi… |
| Q619 | 3 | A, D | 🟡 source-key-unverified | A video processing company uses an AWS Lambda function to handle image processing tasks. An Amazon EventBridge … |
| Q630 | 3 | A | 🟡 source-key-unverified | A solutions architect works for a government agency that has strict disaster recovery requirements. All Amazon … |
| Q633 | 3 | C | 🟡 source-key-unverified | A company that provides image storage services wants to deploy a customer-lacing solution to AWS. Millions of i… |
| Q653 | 1 | B | 🟡 source-key-unverified | A company is running an application on several Amazon EC2 instances in an Auto Scaling group behind an Applicat… |
| Q660 | 3 | B | 🟡 source-key-unverified | A company ingests and processes streaming market data. The data rate is constant. A nightly process that calcul… |
| Q670 | 3 | D | 🟡 source-key-unverified | A company hosts an application that uses several Amazon EC2 instances in an Auto Scaling group behind an Applic… |
| Q673 | 3 | D | 🟡 source-key-unverified | A company is deploying a new cluster for big data analytics on AWS. The cluster will run across many Linux Amaz… |

## 6. EFS, FSx, EBS & file storage — 27 questions

| Q | Domain | Existing key* | Status | Scenario cue |
|---|---:|---|---|---|
| Q14 | 2 | C | 🟢 aws-docs-verified-study-wording | A company runs an application on 20 persistent Amazon EC2 instances with multiple attached Amazon EBS volumes. … |
| Q31 | 3 | C | 🟢 source-key-unverified | A solutions architect must analyze a company's Amazon EC2 Instances and Amazon Elastic Block Store (Amazon EBS)… |
| Q68 | 3 | A | 🟢 source-key-unverified | A company uses AWS Cloud Formation to deploy its infrastructure. The company is concerned that data stored in A… |
| Q88 | 3 | A | 🟢 source-key-unverified | A solutions architect needs to review the design of an Amazon EMR cluster that is using the EMR File System (EM… |
| Q97 | 3 | B | 🟢 source-key-unverified | A solutions architect is investigating an issue in which a company cannot establish new sessions in Amazon Work… |
| Q105 | 3 | D | 🟡 source-key-unverified | A retail company is hosting an ecommerce website on AWS across multiple AWS Regions. The company wants the webs… |
| Q122 | 2 | A, B, D | 🔴 disputed-wording | A company recently started hosting new application workloads in the AWS Cloud. The company is using Amazon EC2 … |
| Q131 | 3 | C | 🟡 source-key-unverified | A large education company recently introduced Amazon Workspaces to provide access to internal applications acro… |
| Q141 | 4 | D | 🟡 aws-doc-verified-external-question-matched | A company wants to containerize a multi-tier web application and move the application from an on-premises data … |
| Q143 | 4 | C | 🔴 aws-doc-verified-external-question-matched | A global ecommerce company has many data centers worldwide. The company needs scalable cloud storage for legacy… |
| Q147 | 3 | A, C, F | 🟡 source-key-unverified | A company has built a high performance computing (HPC) cluster in AWS tor a tightly coupled workload that gener… |
| Q169 | 4 | B, E | 🟡 source-key-unverified | A company has a platform that consists of an on-premises single-node Kubernetes cluster. The cluster uses Windo… |
| Q178 | 4 | B | 🔴 verified-b-external-reordered-c-legacy-github-warning | A startup company recently migrated a large ecommerce website to AWS The website has experienced a 70% increase… |
| Q184 | 2 | B | 🟡 source-key-unverified | A company has a website that runs on four Amazon EC2 instances that are behind an Application Load Balancer (AL… |
| Q231 | 3 | B | 🟡 source-key-unverified | A finance company is running its business-critical application on current-generation Linux EC2 instances The ap… |
| Q258 | 4 | C | 🔴 source-c-defective-ambiguous-d-also-valid | A company has an on-premises website application that provides real estate information for potential renters an… |
| Q270 | 2 | C | 🟡 source-key-unverified | A company has an internal application running on AWS that is used to track and process shipments in the company… |
| Q277 | 3 | A | 🟡 source-key-unverified | A company is using AWS CloudFormation to deploy its infrastructure. The company is concerned that, if a product… |
| Q345 | 3 | A | 🟡 source-key-unverified | A company is deploying a new web-based application and needs a storage solution for the Linux application serve… |
| Q377 | 4 | A | 🟡 verified-with-tco-scope-caveat | A company wants to migrate its website to AWS. The website uses containers that are deployed in an on-premises,… |
| Q398 | 3 | C | 🟡 source-key-unverified | An EC2-based ticketing service pulls a frequently updated pricing file (stored in S3) on startup. Sometimes EC2… |
| Q416 | 4 | D | 🔴 verified-aws-and-external-with-wording-fixes | A company migrated an application to the AWS Cloud. The application runs on two Amazon EC2 instances behind an … |
| Q482 | 3 | C | 🟡 source-key-unverified | A company uses a Grafana data visualization solution that runs on a single Amazon EC2 instance to monitor the h… |
| Q520 | 4 | B | 🟡 source-key-unverified | A company wants to migrate its website to AWS. The website uses microservices and runs on containers that are d… |
| Q525 | 3 | B | 🟡 source-key-unverified | A company is planning a large event where a promotional offer will be introduced. The company's website is host… |
| Q588 | 3 | A | 🟡 source-key-unverified | A company needs to optimize the cost of backups for Amazon Elastic File System (Amazon EFS). A solutions archit… |
| Q635 | 2 | C | 🟡 source-key-unverified | A company runs a content management application on a single Windows Amazon EC2 instance in a development enviro… |

## 7. RDS, Aurora, DynamoDB & caching — 61 questions

| Q | Domain | Existing key* | Status | Scenario cue |
|---|---:|---|---|---|
| Q2 | 3 | C | 🟢 source-key-unverified | An ecommerce company runs an application on AWS. The application has an Amazon API Gateway API that invokes an … |
| Q16 | 3 | D | 🔴 outdated | A company is running an application in the AWS Cloud. The application uses AWS Lambda functions and Amazon Elas… |
| Q22 | 4 | C | 🟢 aws-docs-reviewed-external-pending | A gaming company is rehosting a compute-intensive application on AWS. It runs a Node.js application on Ubuntu E… |
| Q23 | 2 | B | 🟢 aws-docs-reviewed-external-pending | An e-commerce company needs a simple, highly available, loosely coupled order-processing application. Order tra… |
| Q54 | 2 | A | 🟢 source-key-unverified | A company has deployed its database on an Amazon RDS for MySQL DB instance in the us-east-1 Region. The company… |
| Q56 | 4 | B | 🔴 domain4-reviewed-legacy-service-check-needed | A company is planning to migrate to the AWS Cloud. The company hosts many applications on Windows servers and L… |
| Q77 | 4 | D | 🔴 aws-doc-verified-external-question-matched | A company is migrating a monolithic on-premises .NET Framework production application to AWS. Application deman… |
| Q92 | 4 | C | 🟡 source-key-unverified | A company needs to migrate its on-premises database fleet to Amazon RDS. The company is currently using a mixtu… |
| Q93 | 2 | B | 🟢 source-key-unverified | A company deploys an AI agent on Amazon Bedrock AgentCore Runtime. The agent processes customer requests. Some … |
| Q103 | 2 | B | 🔴 disputed-cost-optimization | A company is running an event ticketing platform on AWS and wants to optimize the platform's cost-effectiveness… |
| Q129 | 3 | A | 🟡 source-key-unverified | A company is replicating an application in asecondary Region. The application usesDynamoDBandRDS for MySQL. The… |
| Q137 | 4 | A | 🟡 aws-doc-verified-external-question-matched | A company is replicating an application in a secondary AWS Region. The application in the primary Region reads … |
| Q138 | 4 | B | 🟡 source-key-corroborated-question-wording-flawed | A company wants to use AWS to create a business continuity solution in case the company's main on-premises appl… |
| Q144 | 4 | C | 🔴 corrected-source-key-aws-doc-verified-external-question-matched-legacy-check | A company migrated to AWS and uses AWS Business Support. The company wants to monitor thecost-effectiveness of … |
| Q145 | 3 | D | 🟡 source-key-unverified | A company recently deployed an application on AWS. The application uses Amazon DynamoDB.The company measured th… |
| Q146 | 4 | B | 🔴 verified-intended-answer-b-source-defective | A company is migrating a containerized Kubernetes app with manifest files to AWS. What is the easiest migration… |
| Q151 | 3 | A | 🟡 source-key-unverified | A solutions architect is designing a solution to process events. The solution must have the ability to scale in… |
| Q167 | 3 | C | 🟡 source-key-unverified | A company has deployed production workloads on Amazon EC2 On-Demand Instances and Amazon RDS for PostgreSQL DB … |
| Q168 | 4 | B | 🔴 historical-key-b-verified-but-outdated-aws-transform | A company is migrating to AWS and needs to inventory physical and virtual servers, apps, and database relations… |
| Q190 | 4 | A, D, F | 🔴 legacy-service-warning | A company wants to migrate its on-premises data center to the AWS Cloud. This includes thousands of virtualized… |
| Q197 | 3 | D | 🟡 source-key-unverified | A financial services company loaded millions of historical stock trades into an Amazon DynamoDB table. The tabl… |
| Q203 | 3 | A | 🟡 source-key-unverified | A company runs its application on Amazon EC2 instances and AWS Lambda functions. The EC2 instances experience a… |
| Q207 | 3 | C | 🟡 source-key-unverified | A retailer is deploying a customer service AI agent that uses multiple tools to look up orders, process refunds… |
| Q210 | 3 | A, B, C | 🟡 source-key-unverified | A company has automated the nightly retraining of its machine learning models by using AWS Step Functions. The … |
| Q230 | 3 | A | 🟡 source-key-unverified | A company has an application that uses an Amazon Aurora PostgreSQL DB cluster for the application's database. T… |
| Q238 | 4 | D | 🔴 verified-d-aws-external-heterogeneous-migration-warning | A company has a legacy application that runs on multiple .NET Framework components. The components share the sa… |
| Q257 | 3 | C | 🟡 source-key-unverified | A company's inventory application stores data in an Amazon Aurora PostgreSQL DB cluster in a single AWS Region… |
| Q274 | 3 | B | 🟡 source-key-unverified | A company has a latency-sensitive trading platform that uses Amazon DynamoDB as a storage backend. The company … |
| Q293 | 4 | A | 🔴 reviewed-with-caveats | A company is running an application in the AWS Cloud. The application runs on containers in an Amazon Elastic C… |
| Q311 | 3 | A | 🟡 source-key-unverified | A company is modernizing a legacy.NET Frameworkapplication backed by SQL Server. Requirements: Containerize int… |
| Q326 | 4 | C, D, E | 🟡 source-key-unverified | A company is running a critical application that uses an Amazon RDS for MySQL database to store data. The RDS D… |
| Q329 | 3 | B | 🟡 source-key-unverified | A company is currently in the design phase of an application that will need an RPO of less than 5 minutes and a… |
| Q342 | 3 | D | 🟡 source-key-unverified | A company needs to optimize the cost of its application on AWS. The application uses AWS Lambda functions and A… |
| Q347 | 4 | C | 🔴 corrected-source-defect | A company wants to migrate its on-premises application to AWS. The database for the application stores structur… |
| Q355 | 4 | C | 🔴 verified | A company that provisions job boards for a seasonal workforce is seeing an increase in traffic and usage. The b… |
| Q364 | 3 | C | 🟡 source-key-unverified | A company runs production workloads on EC2 On-Demand Instances and RDS for PostgreSQL. They want to reduce cost… |
| Q368 | 2 | D | 🟡 source-key-unverified | A company hosts a software as a service (SaaS) solution on AWS. The solution has an Amazon API Gateway API that… |
| Q372 | 3 | B | 🟡 source-key-unverified | A company processes environment data. The has a set up sensors to provide a continuous stream of data from diff… |
| Q393 | 3 | B | 🟡 source-key-unverified | A software as a service (SaaS) company has developed a multi-tenant environment. The company uses Amazon Dynamo… |
| Q394 | 3 | B | 🟡 source-key-unverified | A company needs a highly available database solution for an application. The solution must be able to fail over… |
| Q422 | 3 | A, C, E | 🟡 source-key-unverified | A company has loT sensors that monitor traffic patterns throughout a large city. The company wants to read and … |
| Q435 | 3 | B, E | 🟡 source-key-unverified | A company runs an loT platform on AWS loT sensors in various locations send data to the company's Node js API s… |
| Q436 | 3 | B | 🟡 source-key-unverified | A company runs its application in the eu-west-1 Region and has one account for each of its environments develop… |
| Q437 | 4 | C | 🟡 verified-best-answer-with-ingestion-caveat | A retail company wants to improve its application architecture. The company's applications register new orders,… |
| Q440 | 2 | D | 🟡 source-key-unverified | A live-events company is designing a scaling solution for its ticket application on AWS. The application has hi… |
| Q478 | 4 | B | 🟡 verified-aws-and-external-with-caveats | A solutions architect must create a business case for migration of a company's on-premises data center to the A… |
| Q493 | 3 | C | 🟡 source-key-unverified | A company is deploying a distributed in-memory database on a fleet of Amazon EC2 instances. The fleet consists … |
| Q509 | 3 | B | 🟡 source-key-unverified | A company collects air quality data from sensors. The company plans to use the MQTT protocol to send the data t… |
| Q516 | 3 | A | 🟡 source-key-unverified | A car rental company has built a serverless REST API to provide data to its mobile app. The app consists of an … |
| Q537 | 4 | C | 🟡 source-key-unverified | A solutions architect needs to assess a newly acquired company’s portfolio of applications and databases. The s… |
| Q545 | 4 | C | 🟡 source-key-unverified | A company wants to migrate to AWS. The company is running thousands of VMs in a VMware ESXi environment. The co… |
| Q552 | 3 | B | 🟡 source-key-unverified | A software company has deployed an application that consumes a REST API by using Amazon API Gateway. AWS Lambda… |
| Q563 | 3 | A, D | 🟡 source-key-unverified | A utility company collects usage data from smart meters every 5 minutes. Data is sent to API Gateway, processed… |
| Q566 | 3 | B | 🟡 source-key-unverified | A company has a web application that uses Amazon API Gateway. AWS Lambda and Amazon DynamoDB A recent marketing… |
| Q570 | 3 | B, D | 🟡 source-key-unverified | A solutions architect has developed a web application that uses an Amazon API Gateway Regional endpoint and an … |
| Q572 | 3 | C | 🟡 source-key-unverified | A company operates quick-service restaurants. The restaurants follow a predictable model with high sales traffi… |
| Q614 | 3 | B, D, E | 🟡 source-key-unverified | A company has several Amazon DynamoDB tables in an AWS Region. Each table has more than 100,000 records and was… |
| Q622 | 3 | A, D, F | 🟡 source-key-unverified | A company is hosting a critical application on a single Amazon EC2 instance. The application uses an Amazon Ela… |
| Q640 | 2 | C | 🟡 source-key-unverified | A delivery company is running a serverless solution in tneAWS Cloud The solution manages user data, delivery in… |
| Q646 | 4 | D | 🟡 source-key-unverified | A company is migrating a large on-prem Oracle database (withstored procedures) to AWS. The solution must useman… |
| Q651 | 2 | D | 🟡 source-key-unverified | A live-events company is designing a scaling solution for its ticket application on AWS. The application has hi… |

## 8. Compute, Auto Scaling, load balancing & containers — 43 questions

| Q | Domain | Existing key* | Status | Scenario cue |
|---|---:|---|---|---|
| Q4 | 3 | B | 🟢 source-key-unverified | A solutions architect has launched multiple Amazon EC2 instances in a placement group within a single Availabil… |
| Q10 | 3 | D | 🟢 source-key-unverified | A company has an application that runs on Amazon EC2 instances in an Amazon EC2 Auto Scaling group. The company… |
| Q26 | 2 | C | 🟢 source-key-unverified | A company is developing a new service that will be accessed using TCP on a static port A solutions architect mu… |
| Q40 | 2 | B | 🟢 source-key-unverified | A company is running a compute workload by using Amazon EC2 Spot Instances that are in an Auto Scaling group. T… |
| Q45 | 3 | A, C, E | 🟢 source-key-unverified | A company runs a Linux app on Amazon EKS usingM6iEC2 instances under a Savings Plan that is about to expire. Th… |
| Q52 | 3 | B | 🟢 source-key-unverified | A company is running a large containerized workload in the AWS Cloud using Amazon ECS. The development team rec… |
| Q55 | 3 | C | 🟢 source-key-unverified | A company developed a pilot application by using AWS Elastic Beanstalk and Java. To save costs during developme… |
| Q84 | 1 | A | 🟡 source-key-unverified | A company is using an organization in AWS organization to manage AWS accounts. For each new project the company… |
| Q109 | 3 | B | 🟡 source-key-unverified | A company is running a large containerized workload in the AWS Cloud. The workload consists of approximately 10… |
| Q114 | 3 | C | 🟡 source-key-unverified | A company has mounted sensors to collect information about environmental parameters such as humidity and light … |
| Q127 | 3 | C, D | 🟡 source-key-unverified | A company has used infrastructure as code (IaC) to provision a set of two Amazon EC2 instances. The instances h… |
| Q181 | 3 | C | 🟡 source-key-unverified | A retail business runs an orders and payments solution that uses more than 100 AWS Lambda functions that are wr… |
| Q194 | 3 | A | 🟡 source-key-unverified | How should a companyefficiently processinfrequently uploaded S3 data using a long- running (up to 25 minutes) c… |
| Q199 | 4 | B | 🔴 verified-b-exact-external-2026-caveats | A company wants to manage the costs associated with a group of 20 applications that are infrequently used, but … |
| Q264 | 4 | A | 🟡 verified-a-aws-external-agentless-2024-update | A company is migrating to the cloud. It wants to evaluate the configurations of virtual machines in its existin… |
| Q265 | 3 | B | 🟡 source-key-unverified | A company has AWS accounts that are in an organization in AWS rganizations. The company wants to track Amazon E… |
| Q279 | 3 | B | 🟡 source-key-unverified | A company is processing videos in the AWS Cloud by using Amazon EC2 instances in an Auto Scaling group. It take… |
| Q292 | 4 | A | 🟡 reviewed-with-caveats | A company is refactoring its on-premises order-processing platform in the AWS Cloud. The platform includes a we… |
| Q295 | 3 | A | 🟡 source-key-unverified | A company recently deployed an application on Amazon ECS with the Fargate launch type. The company uses an AWS … |
| Q303 | 3 | D | 🟡 source-key-unverified | A company is running a compute workload by using Amazon EC2 Spot Instances in an Auto Scaling group. The launch… |
| Q337 | 4 | A, C, E | 🟡 source-key-unverified | A company runs a simple Linux application on Amazon EKS by using nodes of the M6i (general purpose) instance ty… |
| Q357 | 3 | D | 🟡 source-key-unverified | A company uses an on-premises data analytics platform. The system is highly available in a fully redundant conf… |
| Q433 | 3 | B | 🟡 source-key-unverified | A company is using an Amazon ECS cluster to run a data-processing application. Different business groups share … |
| Q450 | 4 | A | 🟡 verified-best-answer-with-cost-qualification | A company migrated an application from on-premises VMs to Amazon EC2 instances in an AWS account 6 months ago. … |
| Q474 | 3 | C | 🟡 source-key-unverified | A company is developing a new on-demand video application that is based on microservices. The application will … |
| Q475 | 4 | A | 🔴 outdated-no-currently-valid-option | A company runs a customer service center that accepts calls and automatically sends all customers a managed, in… |
| Q501 | 3 | B | 🟡 source-key-unverified | A company's CISO has asked a Solutions Architect to re-engineer the company's current CI/CD practices to make s… |
| Q523 | 3 | D | 🟡 source-key-unverified | A company is hosting an application on AWS for a project that will run for the next 3 years. The application co… |
| Q543 | 3 | D | 🟡 source-key-unverified | A company is preparing to deploy an Amazon Elastic Kubernetes Service (Amazon EKS) cluster for a workload. The … |
| Q550 | 2 | A | 🟡 source-key-unverified | A company has a new application that needs to run on five Amazon EC2 instances in a single AWS Region. The appl… |
| Q567 | 1 | C, D | 🟡 source-key-unverified | A company uses infrastructure as code (IaC) to provision Amazon EC2 instances. The company uses a launch templa… |
| Q569 | 1 | A | 🟡 source-key-unverified | A company is running a containerized application in the AWS Cloud. The application is running by using Amazon E… |
| Q573 | 4 | D | 🟡 source-key-unverified | A delivery company needs to migrate its third-party route planning application to AWS. The third party supplies… |
| Q575 | 3 | B, D | 🟡 source-key-unverified | A solutions architect wants to cost-optimize and appropriately size Amazon EC2 instances in a single AWS accoun… |
| Q608 | 3 | A | 🟡 source-key-unverified | A company is rearchitecting its applications to run on AWS. The company's infrastructure includes multiple Amaz… |
| Q618 | 3 | A | 🟡 source-key-unverified | A company needs to implement a patching process for its servers. The on-premises servers and Amazon EC2 instanc… |
| Q624 | 4 | D | 🟡 source-key-unverified | A machine learning (ML) company continuously develops new versions of its models. The models are integrated int… |
| Q638 | 4 | C | 🟡 source-key-unverified | A company is migrating its legacy .NET workload to AWS. The company has a containerized setup that includes a b… |
| Q643 | 3 | B | 🟡 source-key-unverified | A company is running a traditional web application on Amazon EC2 instances. The company needsto refactor the ap… |
| Q647 | 4 | C | 🟡 source-key-unverified | A company has a Windows-based desktop application that is packaged and deployed to the users' Windows machines… |
| Q652 | 3 | D | 🟡 source-key-unverified | A company runs a web application on a single Amazon EC2 instance. End users experience slow application perform… |
| Q661 | 3 | C | 🟡 source-key-unverified | A company runs a proprietary stateless ETL application on an Amazon EC2 Linux instance. The application is a Li… |
| Q674 | 4 | B | 🟡 source-key-unverified | A company hosts a Git repository in an on-premises data center. The company uses webhooks to invoke functionali… |

## 9. Serverless, messaging, APIs & event-driven design — 8 questions

| Q | Domain | Existing key* | Status | Scenario cue |
|---|---:|---|---|---|
| Q36 | 2 | D | 🟢 source-key-unverified | A healthcare company is building a user support chat-based assistant on Amazon Bedrock. Users will ask health q… |
| Q46 | 3 | C | 🟡 source-key-unverified | A data analytics company has an Amazon Redshift cluster that consists of several reserved nodes. The cluster is… |
| Q163 | 3 | C | 🟡 source-key-unverified | A company has a solution that analyzes weather data from thousands of weather stations. The weather stations se… |
| Q196 | 3 | B | 🟡 source-key-unverified | A company is building an automated pipeline that uses AWS Step Functions to orchestrate multiple stages. The pi… |
| Q198 | 3 | C | 🟡 source-key-unverified | A company is building a software-as-a-service (SaaS) solution on AWS. The company has deployed an Amazon API Ga… |
| Q223 | 3 | B | 🟡 source-key-unverified | A company stores all its infrastructure code in a central Git repository that is hosted on GitHub Enterprise. T… |
| Q253 | 1 | D | 🟡 source-key-unverified | A company has implemented an ordering system using an event-driven architecture. During initial testing, the sy… |
| Q344 | 3 | A | 🟡 source-key-unverified | A company is running an application in the AWS Cloud. Recent application metrics show inconsistent response tim… |

## 10. Observability, operations & governance — 1 questions

| Q | Domain | Existing key* | Status | Scenario cue |
|---|---:|---|---|---|
| Q623 | 3 | C | 🟡 source-key-unverified | A retail company has an ecommerce application that uses ML to make product recommendations. The company creates… |

## 11. Performance, cost & Well-Architected — 0 questions

| Q | Domain | Existing key* | Status | Scenario cue |
|---|---:|---|---|---|

## 12. Resilience, backup & disaster recovery — 0 questions

| Q | Domain | Existing key* | Status | Scenario cue |
|---|---:|---|---|---|

## 13. Discovery, assessment & migration planning — 0 questions

| Q | Domain | Existing key* | Status | Scenario cue |
|---|---:|---|---|---|

## 14. AWS DMS, database migration & change data capture — 0 questions

| Q | Domain | Existing key* | Status | Scenario cue |
|---|---:|---|---|---|

## 15. Application Migration Service, modernization & containers — 0 questions

| Q | Domain | Existing key* | Status | Scenario cue |
|---|---:|---|---|---|

## 16. DataSync, Storage Gateway, Transfer Family & Snow — 0 questions

| Q | Domain | Existing key* | Status | Scenario cue |
|---|---:|---|---|---|

## 17. Data analytics, streaming & machine learning — 1 questions

| Q | Domain | Existing key* | Status | Scenario cue |
|---|---:|---|---|---|
| Q152 | 1 | A | 🟡 source-key-unverified | A company provisions short-lived AWS accounts for students. Each account needs access to ml.p2.xlarge SageMaker… |

*Existing key = current dataset answer only; not independently reverified for this index.*

Count checked: **674 of 674** entries. Topic counts sum to 674.
