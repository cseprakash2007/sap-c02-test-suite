# Domain 4 Q615 — question 128/139

**Verified answer E.** Original question and all five options preserved in `src/data/questions.json`. Reviewed 2026-11-01.

## Scenario
Back up an on-premises NFS file share to S3. Archive backups after five days. Disaster recovery restores can take days. Minimize cost.

## Answer
**E:** AWS Storage Gateway **S3 File Gateway** presents NFS/SMB and stores files as S3 objects. An S3 Lifecycle policy transitions eligible objects to **S3 Glacier Deep Archive** after five days. This is a low-cost long-term archive for rarely restored backup objects.

## Every option
- **A incorrect:** File Gateway supports NFS but Standard-IA remains online and is generally more costly than Deep Archive for long-retained, seldom restored backups.
- **B incorrect:** Volume Gateway provides iSCSI block volumes, not NFS file shares. Its volume snapshots are not File Gateway-style S3 objects managed with the proposed lifecycle rule.
- **C incorrect:** Tape Gateway provides virtual tape devices, not NFS file shares. S3 Standard-IA is not the best archive tier here.
- **D incorrect:** Internally contradictory: deploy File Gateway but move files to Tape Gateway. Also selects Standard-IA rather than Deep Archive.
- **E correct:** NFS file interface plus inexpensive S3 Deep Archive after five days; delayed restore is acceptable.

## Important 2026 caveats
- **180-day minimum storage duration charge** for Deep Archive is a billing condition, **not** a prohibition on transitioning objects after five days.
- Deep Archive standard retrieval is typically around 12 hours; bulk retrieval can take up to 48 hours. Objects must be restored before normal use.
- File Gateway clients can receive I/O errors for objects transitioned to archival Glacier classes until restored.
- S3 Lifecycle configurations since September 2024 by default do not transition objects **under 128 KB**, unless supported exception behavior is explicitly configured.
- Lifecycle transitions and archival metadata incur request and per-object overhead; small-object economics matter.

## Source quality and variants
- Exact-stem external ITDumpsKR SAP-C02 practice test keys **E** with five single-choice options; A-D are in a different order. No verified Choose TWO/THREE variant.
- Original stem typo `t he`; A `files gateway` inconsistent terminology; D impossible file/tape gateway wording. Original stem/options retained unchanged for traceability.

## Official AWS sources
- https://aws.amazon.com/storagegateway/faqs/
- https://docs.aws.amazon.com/filegateway/latest/files3/storage-classes.html
- https://docs.aws.amazon.com/AmazonS3/latest/userguide/glacier-storage-classes.html
- https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-transition-general-considerations.html

## External source
- https://www.itdumpskr.com/SAP-C02-practice-test.html
