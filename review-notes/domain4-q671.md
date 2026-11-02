# Domain 4 Q671 — 138/139

**Verified A**, single-answer.

## Original stem
An online retail company is migrating its legacy on-premises .NET application to AWS. The application runs on load-balanced frontend web servers, load-balanced application servers, and a Microsoft SQL Server database. The company wants to use AWS managed services where possible and does not want to rewrite the application. A solutions architect needs to implement a solution to resolve scaling issues and minimize licensing costs as the application scales. Which solution will meet these requirements MOST cost-effectively?

## Original options
- A. Deploy Amazon EC2 instances in an Auto Scaling group behind an Application Load Balancerfor the web tier and for the application tier. Use Amazon Aurora PostgreSQL with Babelfish turned on to replatform the SOL Server database.
- B. Create images of all the servers by using AWS Database Migration Service (AWS DMS). Deploy Amazon EC2 instances that are based on the on-premises imports. Deploy the instances in an Auto Scaling group behind a Network Load Balancer for the web tier and for the application tier. Use Amazon DynamoDB as the database tier.
- C. Containerize the web frontend tier and the application tier. Provision an Amazon Elastic Kubernetes Service (Amazon EKS) cluster. Create an Auto Scaling group behind a Network Load Balancer for the web tier and for the application tier. Use Amazon RDS for SOL Server to host the database.
- D. Separate the application functions into AWS Lambda functions. Use Amazon API Gateway for the web frontend tier and the application tier. Migrate the data to Amazon S3. Use Amazon Athena to query the data.

## Review
A: EC2 Auto Scaling behind ALBs scales existing .NET web and application tiers. Aurora PostgreSQL with Babelfish provides T-SQL/TDS compatibility, reducing SQL Server licensing and extensive rewrites. Assess unsupported SQL Server features before migration. https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-migration.html

A correct: scalable tiers plus Babelfish. B incorrect: DMS does not image servers; DynamoDB requires redesign. C incorrect: EKS containerization adds effort and RDS SQL Server retains licensing. D incorrect: Lambda/API Gateway/S3/Athena require extensive rewrite and Athena is not an OLTP database.

Original OCR defects: 'ALBfor' and 'SOL Server'. Exact stem found at https://www.exam-tests.com/SAP-C02-exam/Amazon.SAP-C02.v2025-02-24.q513.html?p=10 . No confirmed Choose TWO/THREE variant or independently verified second external answer key.

## AWS sources
https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-migration.html
https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-compatibility.html
https://aws.amazon.com/rds/aurora/babelfish/
