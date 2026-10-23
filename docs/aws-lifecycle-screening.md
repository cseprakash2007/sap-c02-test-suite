# AWS SAP-C02 lifecycle review — 2026-10-22

## Scope and evidence

This is a **service-lifecycle screening reference**, not proof that any particular exam question is incorrect. A question that mentions a retired service might still have a valid answer if it asks for a migration *away* from that service. Assess the scenario and every option before changing an answer key.

Official AWS lifecycle lists:

- Full shutdown: https://docs.aws.amazon.com/general/latest/gr/full_shutdown_services.html
- Sunset: https://docs.aws.amazon.com/general/latest/gr/sunset_services.html
- Maintenance: https://docs.aws.amazon.com/general/latest/gr/maintenance_services.html
- Definitions: https://docs.aws.amazon.com/general/latest/gr/service-lifecycle.html

## Additional high-priority terms to screen in the 674-question bank

| Term / feature | AWS lifecycle category as of 2026-10-22 | Screening caveat |
| --- | --- | --- |
| AWS CodeStar | Full shutdown | Do not confuse with CodeStar Connections/CodeConnections |
| AWS OpsWorks Stacks | Full shutdown | Distinguish service from Chef/Puppet tools |
| Amazon QLDB | Full shutdown | Check any proposed ledger architecture |
| AWS IoT Analytics | Full shutdown | Check any new IoT ingestion recommendation |
| Amazon Kinesis Data Analytics for SQL | Full shutdown | Distinguish from Managed Service for Apache Flink |
| Amazon Elastic Transcoder | Full shutdown | Compare MediaConvert |
| Amazon WorkDocs | Full shutdown | Check any collaboration/storage recommendation |
| Amazon CloudWatch Evidently | Full shutdown | Check feature rollout/experiment options |
| AWS App Mesh | Sunset date passed | Distinguish from service mesh generally |
| AWS Proton | Sunset date passed | Review any new provisioning recommendation |
| AWS WAF Classic | Sunset date passed | Distinguish from AWS WAF |
| Amazon Pinpoint | Sunset date October 30, 2026 | Still before listed date as of this review |
| Amazon CloudSearch | Maintenance | Existing customers may continue |
| AWS Cloud9 | Maintenance | Existing customers may continue |
| Amazon S3 Select | Maintenance | Existing customers may continue |
| AWS App Runner | Maintenance | Not shut down |

## Previously identified candidates

The application uses `src/data/outdated-review.json` for question-specific lifecycle notes. Q85 AppFabric was **removed from the lifecycle filter** because its alleged full-service discontinuation was not substantiated. The six remaining lifecycle candidates are **not** the complete outdated-question count.

## Work still required

1. Search every question stem and all answer options for the terms above and AWS product aliases.
2. Inspect matches manually, including whether the affected service is the recommended answer or only background context.
3. Verify each candidate with its product documentation and lifecycle date.
4. Record question ID, exact outdated claim, status, replacement solution, and citation.
5. Reassess answer keys and run the React build. No complete 674-question scan or successful build is claimed in this file.
