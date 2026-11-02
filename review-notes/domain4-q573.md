# Domain 4 Q573 — single-answer question 123/139

**Verified answer D.** Original question and choices preserved in `src/data/questions.json`.

## Explanation
The route planning image can run as independently configured workers per delivery section. **ECS on Fargate** avoids EC2 node provisioning, patching and scaling, and resources scale with the number of running tasks. Use `aws ecs run-task --launch-type FARGATE --enable-ecs-managed-tags --tags key=Section,value=North` plus the task definition, cluster, `awsvpc` networking, and task/container overrides for per-section settings. `enableECSManagedTags` is the **API field**, `--enable-ecs-managed-tags` the **CLI flag**. Custom tags identify/organize tasks but do not change which orders a container processes.

## Options
- **A wrong:** EKS on EC2 requires worker node management; Kubernetes pods use labels/annotations, not the suggested `-tags` CLI option.
- **B wrong:** EKS on Fargate removes node management but `tag-resource` does not attach AWS tags to individual Kubernetes pods; EKS is more operational complexity for simple container tasks.
- **C wrong:** ECS on EC2 requires EC2 capacity management; `run-tasks set to true` and `- tags` are invalid CLI syntax.
- **D correct:** ECS Fargate + RunTask supports per-task resource allocation, custom tags and ECS-managed tags with minimal operational overhead.

## Cross-verification
Exact-stem FreeCram 2023 Q121/205 and 2025 PDF Q223 both answer D. No confirmed Choose TWO/THREE version; no retired services. Flag only minor API-vs-CLI wording and distinction between tagging and runtime configuration.

## AWS documentation
- https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask.html
- https://docs.aws.amazon.com/cli/latest/reference/ecs/run-task.html
- https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html
- https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_AWSCLI_Fargate.html

## External exact-stem copies
- https://www.freecram.net/question/Amazon.SAP-C02.v2023-09-16.q205/a-delivery-company-needs-to-migrate-its-third-party-route-planning-application-to-aws-the-third-party
- https://www.freecram.net/Amazon.SAP-C02.v2025-04-03.q227.pdf

Reviewed 2026-11-01.