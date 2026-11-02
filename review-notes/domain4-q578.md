# Domain 4 Q578 — single-answer question 124/139

**Verified answer D** (original source answer retained). Original question/options retained verbatim in `src/data/questions.json`.

## AWS-verified explanation
One media job can take an hour. Standard Lambda invocations have a 15-minute maximum; AWS now documents a special Lambda Managed Instances exception of up to 90 minutes for eligible async/event source mapping invocations, not mentioned by A/C. SQS + EC2 Auto Scaling workers can process one-hour jobs, scale with peak daytime demand, and save output to S3. AWS recommends target tracking on SQS **backlog per instance**, not raw queue length; apply scale-in protection during in-flight work. Set appropriate SQS visibility timeout (up to 12 hours), extend with heartbeat as necessary, delete on success, use idempotent processing and DLQ.

## Option-by-option
- **A wrong:** standard Lambda times out before one-hour work completes.
- **B wrong:** MQ and EFS are unnecessary without protocol/POSIX requirement; launching one EC2 per message is inefficient and higher operational overhead.
- **C wrong:** standard Lambda still times out; EFS doesn't fix runtime limit.
- **D correct:** SQS buffers tasks, EC2 Auto Scaling adjusts processing capacity, S3 stores output cost-effectively.

## External exact-stem check and defects
CertLibrary SAP-C02 Q12 and FreeCram Q127/183 both key D; iPassleader reletters the same architecture as C. No confirmed Choose TWO/THREE variant. OCR defects: `Amazon M` / `Amazon MO` => Amazon MQ, `Amazon SOS` => Amazon SQS. Original D says queue length; backlog-per-instance is more precise. No retired services.

## Official AWS sources
- https://docs.aws.amazon.com/en_en/lambda/latest/dg/configuration-timeout.html
- https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-using-sqs-queue.html
- https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-target-tracking-metric-math.html
- https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html

## External sources
- https://www.certlibrary.com/exam/AWS%20Certified%20Solutions%20Architect%20-%20Professional%20SAP-C02
- https://www.freecram.net/question/Amazon.SAP-C02.v2023-11-04.q183/a-solutions-architect-needs-to-advise-a-company-on-how-to-migrate-its-on-premises-data-processing-applicat
- https://www.ipassleader.com/Amazon/SAP-C02-practice-exam-dumps.html

Reviewed 2026-11-01.