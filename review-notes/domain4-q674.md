# Domain 4 Q674 — question 139 of 139

**Verified intended answer: B.** Single answer.

## Full original question
A company hosts a Git repository in an on-premises data center. The company uses webhooks to invoke functionality that runs in the AWS Cloud. The company hosts the webhook logic on a set of Amazon EC2 instances in an Auto Scaling group that the company set as a target for an Application Load Balancer (ALB). The Git server calls the ALB for the configured webhooks. The company wants to move the solution to a serverless architecture. Which solution will meet these requirements with the LEAST operational overhead?

## Original options
- **A:** For each webhook, create and configure an AWS Lambda function URL. Update the Git servers to call the individual Lambda function URLs.
- **B:** Create an Amazon API Gateway HTTP API. Implement each webhook logic in a separate AWS Lambda function. Update the Git servers to call the API Gateway endpoint.
- **C:** Deploy the webhook logic to AWS App Runner. Create an ALB, and set App Runner as the target. Update the Git servers to call the ALB endpoint.
- **D:** Containerize the webhook logic. Create an Amazon Elastic Container Service (Amazon ECS) cluster, and run the webhook logic in AWS Fargate. Create an Amazon API Gateway REST API, and set Fargate as the target. Update the Git servers to call the API Gateway endpoint.

## Detailed review
B: API Gateway HTTP API provides a single managed HTTPS endpoint with routes integrating separately with Lambda functions, avoiding EC2 and container infrastructure. AWS: https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations.html and https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html .

A: Lambda function URLs work and can be simpler for individual functions, but multiple separately managed endpoints are less cohesive than one routed HTTP API; the question is somewhat ambiguous on absolute minimum overhead. B: best intended answer for multiple webhooks and centralized routing. C: ALB target groups support instance, IP, Lambda, not App Runner as a native target. D: Fargate requires containers/task/networking and REST API private integration complexity, higher overhead.

## Caveats and variants
No confirmed Choose TWO/THREE variant. Exact-stem external sites CertLibrary, FreeCram Topic 3 Q232, SpotO and SecExams key B; ExamsLabs rearranges options so the same API Gateway answer is letter D. Wording ambiguity: A is also serverless and could minimize overhead if independent endpoints are acceptable; B is the exam-intended centralized routing solution. No obsolete services identified.

## AWS documentation
- https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations.html
- https://docs.aws.amazon.com/lambda/latest/dg/furls-http-invoke-decision.html
- https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html

## Independent exam sites
- https://www.certlibrary.com/exam/AWS%20Certified%20Solutions%20Architect%20-%20Professional%20SAP-C02
- https://www.freecram.com/discussions/Amazon/exam-sap-c02-topic-3-question-232-discussion-p1320651.html
- https://cciedump.spoto.net/exam-questions/free-aws-sap-c02-practice-questions-answers-2026-part2
- https://realexamcollection.examslabs.com/articles/mar-2025-newly-released-sap-c02-exam-questions-for-you-to-pass-q59-q76/
