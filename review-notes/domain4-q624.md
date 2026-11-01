# Domain 4 Q624 — question 130/139

**Intended answer D verified, with integration caveat.** Original stem and options preserved; reviewed 2026-11-01.

## Question
An EC2-hosted Python ML inference API needs a gradual 10% new-model rollout and minimal infrastructure management.

## Every option
- **A incorrect as written:** Multi-model endpoints host model artifacts on shared inference resources; weighting production variants is a separate SageMaker real-time endpoint capability. Does not simply configure per-model 10/90 weights on one multi-model endpoint.
- **B technically feasible, less optimal:** Two SageMaker serverless endpoints and custom random selection in Lambda. More routing logic to maintain than API Gateway's native canary.
- **C technically feasible, less optimal:** Two single-model real-time endpoints and Lambda custom routing; must manage inference capacity/scaling and custom routing.
- **D intended best:** SageMaker Serverless Inference + API Gateway REST API canary releases, configured for 10% canary and 90% production.

## Critical AWS limitation / source defect
SageMaker **Serverless Inference does not support multiple production variants or multi-model endpoints**. D cannot mean one serverless endpoint automatically hosts both versions with 90/10 routing. Implement **two distinct serverless inference endpoints**, each invoked by the corresponding API Gateway production/canary integration (for example separate Lambda integration or stage-variable overrides). The original option omits this necessary detail. Canary traffic routing is performed by API Gateway, not the SageMaker endpoint. REST API canary feature and appropriate backend mapping are required. SageMaker serverless cold starts may matter for latency.

## Independent sources / variants
- Exact-stem ExamCollection SAP-C02 question 178 lists answer **D**.
- No confirmed Choose TWO/THREE variant found.
- Do not confuse SageMaker real-time production variant A/B testing with multi-model endpoint model artifact selection.

## AWS sources
- https://docs.aws.amazon.com/apigateway/latest/developerguide/canary-release.html
- https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html
- https://docs.aws.amazon.com/sagemaker/latest/dg/model-ab-testing.html
- https://docs.aws.amazon.com/sagemaker/latest/dg/multi-model-endpoints.html

## External exam source
- https://www.examcollection.us/exam/SAP-C02-question-answer-12.html
