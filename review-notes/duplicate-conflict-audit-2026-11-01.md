# Duplicate and conflicting-answer audit

- Q333 corrected D -> A: S3 bucket must be empty before CloudFormation deletion. https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3-bucket.html
- Q565 corrected A -> B: ALB cannot target SQS; HTTP API can integrate with SQS. https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html
- Q446 is the same scenario as Q565 and already has B.
- Q82 and Q412 are the same S3 deletion scenario and already have A.
- Q40/Q303 have different answer letters but same selected answer text.
- Q9/Q510 are similar but differ in private dedicated connection and bandwidth requirements; Q510 flagged for further review rather than changed automatically.
- Preliminary text-similarity scan identified 26 candidate pairs; not all are duplicates.
