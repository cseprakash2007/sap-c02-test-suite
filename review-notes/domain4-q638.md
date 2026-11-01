# Domain 4 Q638 — question 134/139

**Verified answer C.** Reviewed 2026-11-01; original stem and options preserved in questions.json.

## Scenario
Legacy .NET container image with tens-of-gigabytes shared base layers; custom component images inherit from it. ECR is required. Minimize container startup time.

## All options
- **A incorrect:** ECS Fargate has no customer EC2 AMI to preload huge container layers.
- **B incorrect:** AWS App Runner manages its own host infrastructure; cannot pre-bake custom host AMI layers.
- **C correct:** ECS on EC2 supports a custom AMI containing a pre-pulled base container image and layer cache; derived component images from ECR reuse matching layers, reducing download latency.
- **D incorrect:** EKS on Fargate cannot use a customer EC2 AMI as the worker environment.

## Important implementation details
- Actually pre-pull image into Docker/container runtime cache before baking the AMI; placing files on disk alone is insufficient.
- Match image layer digests; configure ECS_IMAGE_PULL_BEHAVIOR=once or prefer-cached where appropriate; maintain compatible ECS agent/runtime and adequate disk space.
- AMI baking trades faster task startup for AMI management and potential slower EC2 instance provisioning. Question asks container startup time, not lowest operational overhead.
- Preserve original transcription typos `onAWS` and missing final punctuation.

## Independent cross-site answer comparison
- P2PExams SAP-C02 PDF Question 1: **C**, same as repository.
- Exam-Tests SAP-C02 Question 219: **A**, same ECS EC2 custom AMI architecture as repository C (options reordered).
- GoShiken SAP-C02 Question 234: **C**, same architecture.
- No confirmed Choose TWO/THREE variant.

## Official AWS references
- https://docs.aws.amazon.com/AmazonECS/latest/developerguide/pull-behavior.html
- https://docs.aws.amazon.com/AmazonECS/latest/bestpracticesguide/pull-behavior.html
- https://repost.aws/knowledge-center/ecs-create-custom-amis
- https://repost.aws/knowledge-center/ecs-images-latency

## External question references
- https://www.p2pexams.com/free-questions/expert-designed-amazon-sap-c02-exam-study-material-by-goodwin.pdf
- https://www.exam-tests.com/SAP-C02-exam/Amazon.SAP-C02.v2025-02-24.q513.html?p=45
- https://www.goshiken.com/blog/%E7%84%A1%E6%96%99sap-c02%E3%82%B5%E3%83%B3%E3%83%97%E3%83%AB%E5%95%8F%E9%A1%8C%E3%81%A7100-%E3%82%AB%E3%83%90%E3%83%BC%E7%8E%87%E3%81%AE%E3%83%AA%E3%82%A2%E3%83%AB%E8%A9%A6%E9%A8%93%E5%95%8F%E9%A1%8C-%E6%9B%B4%E6%96%B0%E3%81%95%E3%82%8C%E3%81%9F485%E5%95%8F%E3%81%82%E3%82%8A%E3%81%BE%E3%81%99-q227-q245/
