# Domain 4 Q583 — question 125 of 139

**Historical answer: B. No option fully valid for new deployments in November 2026.** Original question and options preserved in `src/data/questions.json`.

## Independent AWS verification
AWS IoT Core natively accepts MQTT and can route messages through an IoT rule to Amazon Data Firehose for S3 delivery. The old **Kinesis Data Analytics for SQL** could historically ingest Firehose as an input source, but AWS restricted new Firehose-input SQL applications after **September 12, 2023**, stopped new SQL applications **October 15, 2025**, and discontinued SQL applications **January 27, 2026**. The current **Amazon Managed Service for Apache Flink** normally reads Kinesis Data Streams or MSK, not Firehose as a standard streaming input.

## Options
- **A incorrect:** Greengrass is edge runtime, MSK plus custom Kafka application and SageMaker model impose more overhead.
- **B historical intended answer, outdated:** IoT Core MQTT + Firehose -> S3 are valid, but the stated Kinesis Data Analytics app reading Firehose relies on retired SQL functionality. No longer deployable as written.
- **C incorrect:** IoT FleetWise stopped accepting new customers April 30, 2026; Glue built-in FindMatches ML transform is record matching, not time-series anomaly detection.
- **D incorrect:** MQ for RabbitMQ adds broker complexity; Amazon Lookout for Metrics ended support October 10, 2025.

## Modern corrected architecture
**Vehicles MQTT -> AWS IoT Core -> Kinesis Data Streams -> Amazon Managed Service for Apache Flink** for five-minute event-time windows and anomaly detection. Use **Amazon Data Firehose** to consume Kinesis Data Streams and archive telematics to **Amazon S3**. Configure adequate throughput, partition keys, retry/buffering, monitoring, and device auth.

## External and variant check
Pupuweb SAP-C02 Q313 reproduces the exact single-answer question and keys **B**. No confirmed Choose TWO/THREE variant. Preserve B as historical key but flag as outdated/unanswerable for current service availability.

## Official AWS references
- https://docs.aws.amazon.com/iot/latest/developerguide/iot-rule-actions.html
- https://docs.aws.amazon.com/iot/latest/developerguide/kinesis-firehose-rule-action.html
- https://docs.aws.amazon.com/kinesisanalytics/latest/dev/
- https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works.html
- https://docs.aws.amazon.com/managed-flink/latest/java/how-sources.html
- https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html
- https://docs.aws.amazon.com/glue/latest/dg/machine-learning.html
- https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/

## External source
- https://pupuweb.com/aws-certified-solutions-architect-professional-sap-c02-actual-exam-question-answer-dumps-4/2/

Reviewed 2026-11-01.