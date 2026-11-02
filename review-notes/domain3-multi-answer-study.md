# Domain 3 multi-answer study — Q83 (6 of 58)

## Verdict
**C and E verified.** Q83 is a near-duplicate of Q32 (same five options, answers, and core scenario) and should be flagged, not deleted automatically. Source text has missing spaces; Q83 omits Q32's explicit anonymous/named requester constraint.

## Original question
A company has an application that stores user-uploaded videos in an Amazon S3 bucket using S3 Standard storage. Users access videos frequently for the first 180 days, and rarely after that. Most videos are over 100 MB. Users often have poor internet connectivity, and the company uses multipart uploads. A solutions architect needs tooptimize S3 storage costs. Which combination of actions will meet these requirements? (Select TWO.)

- **A.** Configure the S3 bucket to be a Requester Pays bucket.
- **B.** Use S3 Transfer Acceleration to upload the videos.
- **C.** Create a lifecycle rule to expireincomplete multipart uploadsafter 7 days.
- **D.** Create a lifecycle rule to transition objects toS3 Glacier Instant Retrieval after 1 day.
- **E.** Create a lifecycle rule to transition objects toS3 Standard-IA after 180 days.

## Explain the answer
- **A incorrect:** Requester Pays moves requester charges, does not reduce underlying stored bytes. Unlike Q32, Q83 does not explicitly mention anonymous access, so do not claim that alone disproves A for Q83.
- **B incorrect:** S3 Transfer Acceleration improves upload speed for some paths, but adds transfer charges and does not clear orphaned multipart-upload parts.
- **C correct:** S3 Lifecycle `AbortIncompleteMultipartUpload` after 7 days deletes stored parts that were never completed, stopping ongoing part charges; does not delete completed objects.
- **D incorrect:** S3 Glacier Instant Retrieval after 1 day conflicts with frequent reads for 180 days and imposes retrieval fees and 90-day minimum storage duration.
- **E correct:** Transition completed objects from S3 Standard to S3 Standard-IA after 180 days, matching later infrequent access (retrieval fees; 30-day minimum).

## Diagram
```text
User multipart video upload
    |-- Complete --> S3 Standard (day 0–180) --> Standard-IA (day 180+): E
    +-- Incomplete -> charged staged parts --> abort after 7 days: C
```

## Duplicate/variant check
- **Q32:** near-identical objective, storage class, lifecycle timings, options A–E, answer C+E; Q32 additionally states named/anonymous users and explicitly distinguishes >100 MB objects.
- **Q305:** other large video S3 uploads, but its performance/geography requirements change the solution. Do not carry C+E into Q305 automatically.
- Published exact Q83 text variants at examsvce and certprep also give C+E, but these are third-party sources, not an AWS exam authority.
- Source typos: `tooptimize`, `expireincomplete multipart uploadsafter`, `toS3`. Original question and options preserved in questions.json for traceability.

## AWS documentation
- https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpu-abort-incomplete-mpu-lifecycle-config.html
- https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html
- https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html
- https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-transition-general-considerations.html

## External variants
- https://www.examsvce.com/sap-c02/questiona-company-has-an-application-that-stores-question-answer.html
- https://www.certprep.io/amazon/sap-c02/questions
