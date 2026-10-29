# SAP-C02 question bank answer audit

Generated: 2026-10-28. **This is an inventory and structural check, not an independent answer verification.** No existing answer keys have been changed by this audit.

## Current audit status

- Total: **674** questions.
- All **674** answer keys currently carry `source-key-unverified`.
- Exact duplicate stems: **Q139/Q243, Q133/Q632, Q389/Q637**.
- Existing source warnings: **Q3, Q12, Q16, Q34**.
- Suspiciously short options: **Q190 (B: AWS SMS, C: AWS x-Ray), Q408 (C: kmsGetPubKKey, D: kms:SKjn)**. Some short answers may be intentional; verify against original source.
- Previously discussed answer-key concerns, **not yet resolved by an independent source audit**: Q61 (CodeCommit/AWS Backup), Q95 (SSE-S3/KMS), Q103 (EKS/RDS cost tradeoffs), Q94 (SNS/SQS regional wording), Q122 (AWS Backup SNS configuration wording).

## Verification standard

1. Match exact stem and full option texts against an independent public source where possible; record URL and whether option ordering differs.
2. Check AWS official documentation for feasibility, limitations, and current availability.
3. Label each question `verified`, `disputed`, `outdated`, `truncated`, or `unverified` with evidence and review date.
4. Change `answers` only when evidence supports the correction; preserve original key and explain any changed options.
5. Never interpret a third-party site's matching answer key as independent technical verification.

Official exam guide: https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-professional-02/solutions-architect-professional-02.html

## Batch 1 — independently checked against AWS docs (2026-10-28)

| Question | Original | Updated | Result | Evidence |
|---|---|---|---|---|
| Q34 | C | B | Corrected: route tables cannot deny attacker IPs; Shield Advanced option is feasible | https://docs.aws.amazon.com/waf/latest/developerguide/ddos-app-layer-web-ACL-and-rbr.html ; https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html |
| Q61 | B | C | Corrected: AWS Backup does not support CodeCommit | https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-feature-availability.html |
| Q95 | D | D (retained) | Disputed: AES256 is SSE-S3; no option clearly specifies a customer-managed KMS key | https://docs.aws.amazon.com/AmazonS3/latest/userguide/specifying-kms-encryption.html |

**Scope note:** These are AWS technical feasibility checks. Matching exact copies on third-party exam sites remains to be completed; do not describe the entire bank as verified.

## Batch 2 — six further technical reviews (2026-10-28)

| ID | Source answer | Audit classification | Finding |
|---|---|---|---|
| Q16 | D | outdated | Aurora Serverless v1 legacy; no current v2 option provided |
| Q94 | A,C | disputed-wording | Single SNS topic must fan out to regional SQS queues, not regional SNS topics |
| Q103 | B | disputed-cost-optimization | D has Spot and Compute Savings Plans for Fargate; cheapest choice depends on assumptions |
| Q122 | A,B,D | disputed-wording | Backup SNS notifications belong to backup vault, event is BACKUP_JOB_FAILED |
| Q190 | A,D,F | legacy-service-warning | AWS SMS is legacy; short names alone not truncation evidence |
| Q408 | A | source-truncated | Missing IAM policy in stem and malformed action names |

All six answer keys retained pending stronger independent verification. AWS docs: https://docs.aws.amazon.com/sns/latest/dg/sns-cross-region-delivery.html ; https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-notifications.html ; https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-ris.html ; https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html

## Batch 3 — external site comparisons and links (2026-10-28)

- **Q95**: [FreeCram says B](https://www.freecram.net/question/Amazon.SAP-C02.v2025-07-25.q355/a-health-insurance-company-stores-personally-identifiable-information-pii-in-an-amazon-s3-bucket-the); [FreePDFDumps says D](https://www.freepdfdumps.com/Amazon.SAP-C02.v2024-09-24.q208.html?p=28); [Certsmania says D](https://www.certsmania.com/pdf/amazon-web-services-test-prep-material-pack-sap-c02-passing-score-by-binod.pdf). AWS [SSE-C](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerSideEncryptionCustomerKeys.html) vs [SSE-KMS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/specifying-kms-encryption.html). Disputed; stored D unchanged.
- **Q122**: [CertEnsure](https://www.certensure.com/amazon-web-services/sap-c02-cert-practice-test.html), [CertsTest](https://www.certstest.com/test/SAP-C02?page=8), and [FreePDFDumps](https://www.freepdfdumps.com/Amazon.SAP-C02.v2025-06-02.q210.html?p=15) all show A+B+D; [AWS vault notifications](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-notifications.html) reveal D's wording problem.
- **Q16**: [AWS retirement announcement](https://repost.aws/questions/QUhcMVoChXRm2HLi8F-yih1g/announcement-support-for-aurora-serverless-v1-ending-soon) confirms v1 retirement. External exam-question match not yet found.

## Batch 4 — applied study-text repairs (2026-10-28)

- **Q16:** Option D modernized from Aurora Serverless v1 to v2 (NOT a restoration of original exam wording). Explanation now discusses write scaling and Compute Savings Plans. [AWS Aurora Serverless](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.html).
- **Q94:** Repaired question grammar, SQS typo in A, and the SNS subscription destination in C; expanded why A+C wins. [AWS cross-Region SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-cross-region-delivery.html).
- **Q122:** Fixed option D to vault-level SNS BACKUP_JOB_FAILED notifications and expanded why A+B+D wins. [AWS Backup notifications](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-notifications.html).
- **Q408:** Normalized IAM action names and grammar; missing source IAM policy **not reconstructed**; answer remains provisional. [AWS S3 KMS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html).

Every edited entry includes `originalQuestionSnapshot` preserving original stem, options, and source answers. The edits are corrected **study wording**, not independently restored original exam text. Do not mark Q408 fully verified.

## Batch 5 — detailed explanations and wording repair (2026-10-28)

| ID | Change | Verification status |
|---|---|---|
| Q12 | Explain why B+C+E overlaps; SCP A conditional; original snapshot retained | Ambiguous source key; no new answer asserted |
| Q94 | Rewrite stem for readability while retaining original and A+C | Corrected study wording |
| Q95 | Full option-by-option rationale and proposed corrected B (not applied to options) | No fully correct source option; D retained as source key |
| Q103 | Explain why B versus D cost comparison is disputed | Source B retained, not independently resolved |
| Q190 | Fix MySQL/grammar; explain each choice and missing detailed cost estimator | Source A+D+F retained |

Official references: [IAM cross-account policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic-cross-account.html), [IAM trust policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_update-role-trust-policy.html), [Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-ris.html), [Migration Discovery](https://docs.aws.amazon.com/application-discovery/latest/userguide/what-is-appdiscovery.html).

## Question inventory

| ID | Domain in bank | Stored answer(s) | Current status | Existing warning |
|---:|---:|---|---|---|
| 1 | 3 | B | source-key-unverified | — |
| 2 | 3 | C | source-key-unverified | — |
| 3 | 4 | D | source-key-unverified | Warning |
| 4 | 3 | B | source-key-unverified | — |
| 5 | 3 | A | source-key-unverified | — |
| 6 | 2 | B | source-key-unverified | — |
| 7 | 4 | A | source-key-unverified | — |
| 8 | 2 | D | source-key-unverified | — |
| 9 | 2 | A,D,E | source-key-unverified | — |
| 10 | 3 | D | source-key-unverified | — |
| 11 | 2 | B | source-key-unverified | — |
| 12 | 1 | B,C,E | source-key-unverified | Warning |
| 13 | 1 | A | source-key-unverified | — |
| 14 | 2 | C | source-key-unverified | — |
| 15 | 2 | C | source-key-unverified | — |
| 16 | 3 | D | source-key-unverified | Warning |
| 17 | 3 | A | source-key-unverified | — |
| 18 | 3 | A,B | source-key-unverified | — |
| 19 | 2 | A,B,C | source-key-unverified | — |
| 20 | 1 | B | source-key-unverified | — |
| 21 | 4 | B | source-key-unverified | — |
| 22 | 4 | C | source-key-unverified | — |
| 23 | 2 | B | source-key-unverified | — |
| 24 | 3 | A | source-key-unverified | — |
| 25 | 1 | B,D | source-key-unverified | — |
| 26 | 2 | C | source-key-unverified | — |
| 27 | 3 | C | source-key-unverified | — |
| 28 | 1 | C | source-key-unverified | — |
| 29 | 1 | D | source-key-unverified | — |
| 30 | 2 | C | source-key-unverified | — |
| 31 | 3 | C | source-key-unverified | — |
| 32 | 3 | C,E | source-key-unverified | — |
| 33 | 1 | D | source-key-unverified | — |
| 34 | 3 | C | source-key-unverified | Warning |
| 35 | 3 | C | source-key-unverified | — |
| 36 | 2 | D | source-key-unverified | — |
| 37 | 3 | D | source-key-unverified | — |
| 38 | 1 | A | source-key-unverified | — |
| 39 | 2 | B | source-key-unverified | — |
| 40 | 2 | B | source-key-unverified | — |
| 41 | 3 | B | source-key-unverified | — |
| 42 | 2 | B | source-key-unverified | — |
| 43 | 3 | B | source-key-unverified | — |
| 44 | 4 | D | source-key-unverified | — |
| 45 | 3 | A,C,E | source-key-unverified | — |
| 46 | 3 | C | source-key-unverified | — |
| 47 | 3 | C | source-key-unverified | — |
| 48 | 2 | B | source-key-unverified | — |
| 49 | 1 | B | source-key-unverified | — |
| 50 | 1 | B | source-key-unverified | — |
| 51 | 1 | A,C,F | source-key-unverified | — |
| 52 | 3 | B | source-key-unverified | — |
| 53 | 3 | A | source-key-unverified | — |
| 54 | 2 | A | source-key-unverified | — |
| 55 | 3 | C | source-key-unverified | — |
| 56 | 4 | B | source-key-unverified | — |
| 57 | 3 | A | source-key-unverified | — |
| 58 | 2 | B | source-key-unverified | — |
| 59 | 1 | B | source-key-unverified | — |
| 60 | 3 | B,D,E | source-key-unverified | — |
| 61 | 2 | B | source-key-unverified | — |
| 62 | 4 | D | source-key-unverified | — |
| 63 | 3 | A,E | source-key-unverified | — |
| 64 | 2 | B | source-key-unverified | — |
| 65 | 1 | C | source-key-unverified | — |
| 66 | 4 | C | source-key-unverified | — |
| 67 | 3 | D | source-key-unverified | — |
| 68 | 3 | A | source-key-unverified | — |
| 69 | 1 | C,D | source-key-unverified | — |
| 70 | 2 | C | source-key-unverified | — |
| 71 | 1 | C,E | source-key-unverified | — |
| 72 | 3 | B | source-key-unverified | — |
| 73 | 2 | A | source-key-unverified | — |
| 74 | 4 | A,C,E | source-key-unverified | — |
| 75 | 3 | B | source-key-unverified | — |
| 76 | 2 | B | source-key-unverified | — |
| 77 | 4 | D | source-key-unverified | — |
| 78 | 3 | A | source-key-unverified | — |
| 79 | 2 | C | source-key-unverified | — |
| 80 | 1 | D | source-key-unverified | — |
| 81 | 1 | A | source-key-unverified | — |
| 82 | 3 | A | source-key-unverified | — |
| 83 | 3 | C,E | source-key-unverified | — |
| 84 | 1 | A | source-key-unverified | — |
| 85 | 3 | C | source-key-unverified | — |
| 86 | 2 | C | source-key-unverified | — |
| 87 | 1 | D | source-key-unverified | — |
| 88 | 3 | A | source-key-unverified | — |
| 89 | 1 | B | source-key-unverified | — |
| 90 | 3 | D | source-key-unverified | — |
| 91 | 1 | C | source-key-unverified | — |
| 92 | 4 | C | source-key-unverified | — |
| 93 | 2 | B | source-key-unverified | — |
| 94 | 2 | A,C | source-key-unverified | — |
| 95 | 2 | D | source-key-unverified | — |
| 96 | 1 | B | source-key-unverified | — |
| 97 | 3 | B | source-key-unverified | — |
| 98 | 3 | A | source-key-unverified | — |
| 99 | 1 | B | source-key-unverified | — |
| 100 | 2 | A | source-key-unverified | — |
| 101 | 3 | B | source-key-unverified | — |
| 102 | 4 | C | source-key-unverified | — |
| 103 | 2 | B | source-key-unverified | — |
| 104 | 1 | B,D,E | source-key-unverified | — |
| 105 | 3 | D | source-key-unverified | — |
| 106 | 4 | A,D,E | source-key-unverified | — |
| 107 | 3 | A | source-key-unverified | — |
| 108 | 1 | B | source-key-unverified | — |
| 109 | 3 | B | source-key-unverified | — |
| 110 | 3 | B | source-key-unverified | — |
| 111 | 3 | D | source-key-unverified | — |
| 112 | 3 | C | source-key-unverified | — |
| 113 | 1 | C,D | source-key-unverified | — |
| 114 | 3 | C | source-key-unverified | — |
| 115 | 3 | A,C | source-key-unverified | — |
| 116 | 4 | A,D,E | source-key-unverified | — |
| 117 | 1 | D | source-key-unverified | — |
| 118 | 1 | B | source-key-unverified | — |
| 119 | 4 | B,C,E | source-key-unverified | — |
| 120 | 1 | B | source-key-unverified | — |
| 121 | 3 | A | source-key-unverified | — |
| 122 | 2 | A,B,D | source-key-unverified | — |
| 123 | 3 | A | source-key-unverified | — |
| 124 | 3 | A | source-key-unverified | — |
| 125 | 1 | C | source-key-unverified | — |
| 126 | 1 | C | source-key-unverified | — |
| 127 | 3 | C,D | source-key-unverified | — |
| 128 | 4 | C | source-key-unverified | — |
| 129 | 3 | A | source-key-unverified | — |
| 130 | 3 | B | source-key-unverified | — |
| 131 | 3 | C | source-key-unverified | — |
| 132 | 2 | C | source-key-unverified | — |
| 133 | 3 | A | source-key-unverified | — |
| 134 | 4 | B | source-key-unverified | — |
| 135 | 3 | B,D | source-key-unverified | — |
| 136 | 1 | A,C | source-key-unverified | — |
| 137 | 4 | A | source-key-unverified | — |
| 138 | 4 | B | source-key-unverified | — |
| 139 | 1 | A,C,E | source-key-unverified | — |
| 140 | 3 | A,B | source-key-unverified | — |
| 141 | 4 | D | source-key-unverified | — |
| 142 | 4 | D | source-key-unverified | — |
| 143 | 4 | C | source-key-unverified | — |
| 144 | 4 | B | source-key-unverified | — |
| 145 | 3 | D | source-key-unverified | — |
| 146 | 4 | B | source-key-unverified | — |
| 147 | 3 | A,C,F | source-key-unverified | — |
| 148 | 4 | C | source-key-unverified | — |
| 149 | 3 | C | source-key-unverified | — |
| 150 | 1 | A | source-key-unverified | — |
| 151 | 3 | A | source-key-unverified | — |
| 152 | 1 | A | source-key-unverified | — |
| 153 | 4 | A | source-key-unverified | — |
| 154 | 1 | B | source-key-unverified | — |
| 155 | 3 | A,D,E | source-key-unverified | — |
| 156 | 3 | A | source-key-unverified | — |
| 157 | 3 | A,D,E | source-key-unverified | — |
| 158 | 3 | A,C | source-key-unverified | — |
| 159 | 3 | A,C,E | source-key-unverified | — |
| 160 | 4 | C | source-key-unverified | — |
| 161 | 4 | A | source-key-unverified | — |
| 162 | 3 | C | source-key-unverified | — |
| 163 | 3 | C | source-key-unverified | — |
| 164 | 2 | D | source-key-unverified | — |
| 165 | 3 | C | source-key-unverified | — |
| 166 | 3 | C | source-key-unverified | — |
| 167 | 3 | C | source-key-unverified | — |
| 168 | 4 | B | source-key-unverified | — |
| 169 | 4 | B,E | source-key-unverified | — |
| 170 | 3 | C | source-key-unverified | — |
| 171 | 4 | B | source-key-unverified | — |
| 172 | 3 | A,D,F | source-key-unverified | — |
| 173 | 1 | A | source-key-unverified | — |
| 174 | 3 | A,C | source-key-unverified | — |
| 175 | 3 | B,E | source-key-unverified | — |
| 176 | 4 | D | source-key-unverified | — |
| 177 | 3 | B,E | source-key-unverified | — |
| 178 | 4 | B | source-key-unverified | — |
| 179 | 3 | B | source-key-unverified | — |
| 180 | 1 | A | source-key-unverified | — |
| 181 | 3 | C | source-key-unverified | — |
| 182 | 3 | A,D,E | source-key-unverified | — |
| 183 | 4 | B | source-key-unverified | — |
| 184 | 2 | B | source-key-unverified | — |
| 185 | 4 | D | source-key-unverified | — |
| 186 | 4 | B | source-key-unverified | — |
| 187 | 3 | B | source-key-unverified | — |
| 188 | 1 | A,C,D | source-key-unverified | — |
| 189 | 4 | B,E,F | source-key-unverified | — |
| 190 | 4 | A,D,F | source-key-unverified | — |
| 191 | 1 | B | source-key-unverified | — |
| 192 | 1 | B,C,F | source-key-unverified | — |
| 193 | 3 | B | source-key-unverified | — |
| 194 | 3 | A | source-key-unverified | — |
| 195 | 3 | B | source-key-unverified | — |
| 196 | 3 | B | source-key-unverified | — |
| 197 | 3 | D | source-key-unverified | — |
| 198 | 3 | C | source-key-unverified | — |
| 199 | 4 | B | source-key-unverified | — |
| 200 | 4 | C | source-key-unverified | — |
| 201 | 1 | D | source-key-unverified | — |
| 202 | 4 | B | source-key-unverified | — |
| 203 | 3 | A | source-key-unverified | — |
| 204 | 1 | A | source-key-unverified | — |
| 205 | 3 | C | source-key-unverified | — |
| 206 | 3 | B | source-key-unverified | — |
| 207 | 3 | C | source-key-unverified | — |
| 208 | 4 | C | source-key-unverified | — |
| 209 | 1 | D | source-key-unverified | — |
| 210 | 3 | A,B,C | source-key-unverified | — |
| 211 | 4 | B | source-key-unverified | — |
| 212 | 4 | C | source-key-unverified | — |
| 213 | 1 | B | source-key-unverified | — |
| 214 | 3 | B | source-key-unverified | — |
| 215 | 3 | D | source-key-unverified | — |
| 216 | 3 | B | source-key-unverified | — |
| 217 | 4 | C | source-key-unverified | — |
| 218 | 4 | D | source-key-unverified | — |
| 219 | 3 | A | source-key-unverified | — |
| 220 | 4 | A | source-key-unverified | — |
| 221 | 4 | B | source-key-unverified | — |
| 222 | 3 | A | source-key-unverified | — |
| 223 | 3 | B | source-key-unverified | — |
| 224 | 4 | B | source-key-unverified | — |
| 225 | 3 | A,B | source-key-unverified | — |
| 226 | 3 | B | source-key-unverified | — |
| 227 | 4 | C | source-key-unverified | — |
| 228 | 4 | C | source-key-unverified | — |
| 229 | 1 | C | source-key-unverified | — |
| 230 | 3 | A | source-key-unverified | — |
| 231 | 3 | B | source-key-unverified | — |
| 232 | 1 | A,D,F | source-key-unverified | — |
| 233 | 3 | D | source-key-unverified | — |
| 234 | 3 | A | source-key-unverified | — |
| 235 | 3 | A | source-key-unverified | — |
| 236 | 3 | C | source-key-unverified | — |
| 237 | 3 | A | source-key-unverified | — |
| 238 | 4 | D | source-key-unverified | — |
| 239 | 4 | B | source-key-unverified | — |
| 240 | 4 | B | source-key-unverified | — |
| 241 | 4 | B,C | source-key-unverified | — |
| 242 | 4 | C | source-key-unverified | — |
| 243 | 1 | A,C,E | source-key-unverified | — |
| 244 | 4 | B | source-key-unverified | — |
| 245 | 3 | B | source-key-unverified | — |
| 246 | 2 | B | source-key-unverified | — |
| 247 | 3 | A,B | source-key-unverified | — |
| 248 | 4 | A,D | source-key-unverified | — |
| 249 | 4 | A,D | source-key-unverified | — |
| 250 | 3 | D | source-key-unverified | — |
| 251 | 1 | C | source-key-unverified | — |
| 252 | 1 | C | source-key-unverified | — |
| 253 | 1 | D | source-key-unverified | — |
| 254 | 1 | A | source-key-unverified | — |
| 255 | 3 | C | source-key-unverified | — |
| 256 | 1 | C | source-key-unverified | — |
| 257 | 3 | C | source-key-unverified | — |
| 258 | 4 | C | source-key-unverified | — |
| 259 | 3 | A | source-key-unverified | — |
| 260 | 3 | D | source-key-unverified | — |
| 261 | 3 | B | source-key-unverified | — |
| 262 | 3 | B | source-key-unverified | — |
| 263 | 1 | C | source-key-unverified | — |
| 264 | 4 | A | source-key-unverified | — |
| 265 | 3 | B | source-key-unverified | — |
| 266 | 4 | D | source-key-unverified | — |
| 267 | 1 | A | source-key-unverified | — |
| 268 | 4 | A,E | source-key-unverified | — |
| 269 | 2 | D | source-key-unverified | — |
| 270 | 2 | C | source-key-unverified | — |
| 271 | 3 | D | source-key-unverified | — |
| 272 | 4 | B | source-key-unverified | — |
| 273 | 3 | C | source-key-unverified | — |
| 274 | 3 | B | source-key-unverified | — |
| 275 | 3 | C | source-key-unverified | — |
| 276 | 4 | A,B,C | source-key-unverified | — |
| 277 | 3 | A | source-key-unverified | — |
| 278 | 4 | C | source-key-unverified | — |
| 279 | 3 | B | source-key-unverified | — |
| 280 | 3 | B | source-key-unverified | — |
| 281 | 4 | B | source-key-unverified | — |
| 282 | 1 | D | source-key-unverified | — |
| 283 | 3 | C,D,E | source-key-unverified | — |
| 284 | 3 | A | source-key-unverified | — |
| 285 | 3 | C | source-key-unverified | — |
| 286 | 4 | B | source-key-unverified | — |
| 287 | 3 | D | source-key-unverified | — |
| 288 | 3 | B | source-key-unverified | — |
| 289 | 1 | A | source-key-unverified | — |
| 290 | 4 | C | source-key-unverified | — |
| 291 | 4 | B | source-key-unverified | — |
| 292 | 4 | A | source-key-unverified | — |
| 293 | 4 | A | source-key-unverified | — |
| 294 | 2 | C | source-key-unverified | — |
| 295 | 3 | A | source-key-unverified | — |
| 296 | 1 | C | source-key-unverified | — |
| 297 | 2 | A,B | source-key-unverified | — |
| 298 | 4 | B | source-key-unverified | — |
| 299 | 1 | A,E | source-key-unverified | — |
| 300 | 4 | B | source-key-unverified | — |
| 301 | 4 | D | source-key-unverified | — |
| 302 | 3 | A,E | source-key-unverified | — |
| 303 | 3 | D | source-key-unverified | — |
| 304 | 1 | A,C | source-key-unverified | — |
| 305 | 3 | A,D | source-key-unverified | — |
| 306 | 4 | C | source-key-unverified | — |
| 307 | 3 | A | source-key-unverified | — |
| 308 | 4 | A | source-key-unverified | — |
| 309 | 1 | C | source-key-unverified | — |
| 310 | 1 | A,C | source-key-unverified | — |
| 311 | 3 | A | source-key-unverified | — |
| 312 | 3 | D | source-key-unverified | — |
| 313 | 2 | B | source-key-unverified | — |
| 314 | 3 | C | source-key-unverified | — |
| 315 | 1 | B | source-key-unverified | — |
| 316 | 3 | D | source-key-unverified | — |
| 317 | 3 | A | source-key-unverified | — |
| 318 | 3 | A | source-key-unverified | — |
| 319 | 1 | A | source-key-unverified | — |
| 320 | 4 | C | source-key-unverified | — |
| 321 | 4 | A,D,F | source-key-unverified | — |
| 322 | 3 | A | source-key-unverified | — |
| 323 | 3 | B,D | source-key-unverified | — |
| 324 | 4 | B | source-key-unverified | — |
| 325 | 1 | A | source-key-unverified | — |
| 326 | 4 | C,D,E | source-key-unverified | — |
| 327 | 4 | A | source-key-unverified | — |
| 328 | 3 | A,B,D | source-key-unverified | — |
| 329 | 3 | B | source-key-unverified | — |
| 330 | 3 | C | source-key-unverified | — |
| 331 | 3 | A,D,F | source-key-unverified | — |
| 332 | 3 | B | source-key-unverified | — |
| 333 | 2 | D | source-key-unverified | — |
| 334 | 4 | D | source-key-unverified | — |
| 335 | 1 | B | source-key-unverified | — |
| 336 | 3 | A | source-key-unverified | — |
| 337 | 4 | A,C,E | source-key-unverified | — |
| 338 | 3 | B | source-key-unverified | — |
| 339 | 1 | C | source-key-unverified | — |
| 340 | 3 | B | source-key-unverified | — |
| 341 | 4 | B | source-key-unverified | — |
| 342 | 3 | D | source-key-unverified | — |
| 343 | 3 | B | source-key-unverified | — |
| 344 | 3 | A | source-key-unverified | — |
| 345 | 3 | A | source-key-unverified | — |
| 346 | 4 | A,D | source-key-unverified | — |
| 347 | 4 | B | source-key-unverified | — |
| 348 | 3 | C | source-key-unverified | — |
| 349 | 3 | A | source-key-unverified | — |
| 350 | 4 | B,E | source-key-unverified | — |
| 351 | 3 | B | source-key-unverified | — |
| 352 | 2 | C | source-key-unverified | — |
| 353 | 3 | A,C | source-key-unverified | — |
| 354 | 3 | C | source-key-unverified | — |
| 355 | 4 | C | source-key-unverified | — |
| 356 | 3 | C | source-key-unverified | — |
| 357 | 3 | D | source-key-unverified | — |
| 358 | 1 | C | source-key-unverified | — |
| 359 | 1 | C | source-key-unverified | — |
| 360 | 1 | D | source-key-unverified | — |
| 361 | 3 | C | source-key-unverified | — |
| 362 | 1 | C | source-key-unverified | — |
| 363 | 4 | B | source-key-unverified | — |
| 364 | 3 | C | source-key-unverified | — |
| 365 | 4 | A,C | source-key-unverified | — |
| 366 | 3 | A | source-key-unverified | — |
| 367 | 4 | D | source-key-unverified | — |
| 368 | 2 | D | source-key-unverified | — |
| 369 | 1 | B | source-key-unverified | — |
| 370 | 1 | A,C,D | source-key-unverified | — |
| 371 | 3 | B | source-key-unverified | — |
| 372 | 3 | B | source-key-unverified | — |
| 373 | 1 | A | source-key-unverified | — |
| 374 | 4 | B | source-key-unverified | — |
| 375 | 1 | A,C,F | source-key-unverified | — |
| 376 | 4 | C | source-key-unverified | — |
| 377 | 4 | A | source-key-unverified | — |
| 378 | 1 | C | source-key-unverified | — |
| 379 | 1 | A,B,C | source-key-unverified | — |
| 380 | 3 | B | source-key-unverified | — |
| 381 | 4 | B,D,F | source-key-unverified | — |
| 382 | 1 | A,C,E | source-key-unverified | — |
| 383 | 3 | A | source-key-unverified | — |
| 384 | 1 | D | source-key-unverified | — |
| 385 | 4 | C | source-key-unverified | — |
| 386 | 4 | A | source-key-unverified | — |
| 387 | 3 | D | source-key-unverified | — |
| 388 | 3 | D,E | source-key-unverified | — |
| 389 | 1 | C | source-key-unverified | — |
| 390 | 3 | A,B,E | source-key-unverified | — |
| 391 | 3 | C | source-key-unverified | — |
| 392 | 3 | A | source-key-unverified | — |
| 393 | 3 | B | source-key-unverified | — |
| 394 | 3 | B | source-key-unverified | — |
| 395 | 4 | A | source-key-unverified | — |
| 396 | 3 | C,E,F | source-key-unverified | — |
| 397 | 3 | A | source-key-unverified | — |
| 398 | 3 | C | source-key-unverified | — |
| 399 | 3 | B | source-key-unverified | — |
| 400 | 3 | A | source-key-unverified | — |
| 401 | 4 | A,D,E | source-key-unverified | — |
| 402 | 3 | A | source-key-unverified | — |
| 403 | 3 | C | source-key-unverified | — |
| 404 | 1 | C | source-key-unverified | — |
| 405 | 3 | D | source-key-unverified | — |
| 406 | 1 | D | source-key-unverified | — |
| 407 | 1 | A,B,E | source-key-unverified | — |
| 408 | 3 | A | source-key-unverified | — |
| 409 | 4 | C | source-key-unverified | — |
| 410 | 3 | C | source-key-unverified | — |
| 411 | 3 | B | source-key-unverified | — |
| 412 | 3 | A | source-key-unverified | — |
| 413 | 4 | C | source-key-unverified | — |
| 414 | 4 | D | source-key-unverified | — |
| 415 | 3 | D | source-key-unverified | — |
| 416 | 4 | D | source-key-unverified | — |
| 417 | 2 | C | source-key-unverified | — |
| 418 | 3 | B | source-key-unverified | — |
| 419 | 3 | A | source-key-unverified | — |
| 420 | 4 | C | source-key-unverified | — |
| 421 | 4 | A | source-key-unverified | — |
| 422 | 3 | A,C,E | source-key-unverified | — |
| 423 | 1 | A,D | source-key-unverified | — |
| 424 | 4 | C | source-key-unverified | — |
| 425 | 3 | C,E | source-key-unverified | — |
| 426 | 3 | C | source-key-unverified | — |
| 427 | 4 | B | source-key-unverified | — |
| 428 | 3 | B,E | source-key-unverified | — |
| 429 | 3 | B | source-key-unverified | — |
| 430 | 1 | A | source-key-unverified | — |
| 431 | 3 | B | source-key-unverified | — |
| 432 | 1 | A,E | source-key-unverified | — |
| 433 | 3 | B | source-key-unverified | — |
| 434 | 4 | A | source-key-unverified | — |
| 435 | 3 | B,E | source-key-unverified | — |
| 436 | 3 | B | source-key-unverified | — |
| 437 | 4 | C | source-key-unverified | — |
| 438 | 4 | B,D,E | source-key-unverified | — |
| 439 | 1 | D | source-key-unverified | — |
| 440 | 2 | D | source-key-unverified | — |
| 441 | 3 | C | source-key-unverified | — |
| 442 | 3 | A,C,F | source-key-unverified | — |
| 443 | 3 | D | source-key-unverified | — |
| 444 | 1 | A,C | source-key-unverified | — |
| 445 | 4 | C | source-key-unverified | — |
| 446 | 3 | B | source-key-unverified | — |
| 447 | 4 | C | source-key-unverified | — |
| 448 | 4 | D | source-key-unverified | — |
| 449 | 1 | D | source-key-unverified | — |
| 450 | 4 | A | source-key-unverified | — |
| 451 | 1 | A,C,F | source-key-unverified | — |
| 452 | 1 | C | source-key-unverified | — |
| 453 | 4 | B | source-key-unverified | — |
| 454 | 1 | B | source-key-unverified | — |
| 455 | 1 | A | source-key-unverified | — |
| 456 | 1 | B,D,F | source-key-unverified | — |
| 457 | 1 | B,D,E | source-key-unverified | — |
| 458 | 3 | D | source-key-unverified | — |
| 459 | 1 | D | source-key-unverified | — |
| 460 | 4 | C | source-key-unverified | — |
| 461 | 2 | B | source-key-unverified | — |
| 462 | 4 | B | source-key-unverified | — |
| 463 | 1 | A,C | source-key-unverified | — |
| 464 | 3 | D | source-key-unverified | — |
| 465 | 1 | A | source-key-unverified | — |
| 466 | 1 | C | source-key-unverified | — |
| 467 | 3 | A | source-key-unverified | — |
| 468 | 1 | B | source-key-unverified | — |
| 469 | 3 | D,E,F | source-key-unverified | — |
| 470 | 3 | C | source-key-unverified | — |
| 471 | 1 | C | source-key-unverified | — |
| 472 | 1 | A | source-key-unverified | — |
| 473 | 3 | B | source-key-unverified | — |
| 474 | 3 | C | source-key-unverified | — |
| 475 | 4 | A | source-key-unverified | — |
| 476 | 1 | B,E | source-key-unverified | — |
| 477 | 3 | B | source-key-unverified | — |
| 478 | 4 | B | source-key-unverified | — |
| 479 | 4 | D | source-key-unverified | — |
| 480 | 1 | A | source-key-unverified | — |
| 481 | 4 | A | source-key-unverified | — |
| 482 | 3 | C | source-key-unverified | — |
| 483 | 1 | A | source-key-unverified | — |
| 484 | 2 | A | source-key-unverified | — |
| 485 | 4 | B | source-key-unverified | — |
| 486 | 3 | A,B | source-key-unverified | — |
| 487 | 4 | A | source-key-unverified | — |
| 488 | 3 | C | source-key-unverified | — |
| 489 | 1 | A | source-key-unverified | — |
| 490 | 3 | C | source-key-unverified | — |
| 491 | 4 | C | source-key-unverified | — |
| 492 | 4 | B | source-key-unverified | — |
| 493 | 3 | C | source-key-unverified | — |
| 494 | 2 | B | source-key-unverified | — |
| 495 | 4 | D | source-key-unverified | — |
| 496 | 3 | C | source-key-unverified | — |
| 497 | 4 | B,D | source-key-unverified | — |
| 498 | 4 | B | source-key-unverified | — |
| 499 | 3 | B | source-key-unverified | — |
| 500 | 1 | D | source-key-unverified | — |
| 501 | 3 | B | source-key-unverified | — |
| 502 | 4 | B | source-key-unverified | — |
| 503 | 1 | C | source-key-unverified | — |
| 504 | 4 | C | source-key-unverified | — |
| 505 | 3 | A | source-key-unverified | — |
| 506 | 4 | A | source-key-unverified | — |
| 507 | 1 | B | source-key-unverified | — |
| 508 | 1 | C | source-key-unverified | — |
| 509 | 3 | B | source-key-unverified | — |
| 510 | 4 | B,D,E | source-key-unverified | — |
| 511 | 4 | B | source-key-unverified | — |
| 512 | 1 | D | source-key-unverified | — |
| 513 | 4 | C,E | source-key-unverified | — |
| 514 | 4 | D | source-key-unverified | — |
| 515 | 3 | A | source-key-unverified | — |
| 516 | 3 | A | source-key-unverified | — |
| 517 | 4 | B | source-key-unverified | — |
| 518 | 1 | A | source-key-unverified | — |
| 519 | 3 | A,C | source-key-unverified | — |
| 520 | 4 | B | source-key-unverified | — |
| 521 | 1 | C | source-key-unverified | — |
| 522 | 1 | A | source-key-unverified | — |
| 523 | 3 | D | source-key-unverified | — |
| 524 | 3 | B | source-key-unverified | — |
| 525 | 3 | B | source-key-unverified | — |
| 526 | 4 | A,B | source-key-unverified | — |
| 527 | 4 | D | source-key-unverified | — |
| 528 | 4 | A | source-key-unverified | — |
| 529 | 3 | D | source-key-unverified | — |
| 530 | 3 | A,D | source-key-unverified | — |
| 531 | 3 | B | source-key-unverified | — |
| 532 | 3 | A | source-key-unverified | — |
| 533 | 3 | C,D | source-key-unverified | — |
| 534 | 3 | B | source-key-unverified | — |
| 535 | 1 | B | source-key-unverified | — |
| 536 | 4 | C,D | source-key-unverified | — |
| 537 | 4 | C | source-key-unverified | — |
| 538 | 4 | A | source-key-unverified | — |
| 539 | 3 | C | source-key-unverified | — |
| 540 | 1 | C | source-key-unverified | — |
| 541 | 1 | C,D,F | source-key-unverified | — |
| 542 | 1 | B,C,E | source-key-unverified | — |
| 543 | 3 | D | source-key-unverified | — |
| 544 | 3 | B | source-key-unverified | — |
| 545 | 4 | C | source-key-unverified | — |
| 546 | 3 | B | source-key-unverified | — |
| 547 | 3 | C | source-key-unverified | — |
| 548 | 3 | B,C,E | source-key-unverified | — |
| 549 | 1 | C | source-key-unverified | — |
| 550 | 2 | A | source-key-unverified | — |
| 551 | 1 | A,C | source-key-unverified | — |
| 552 | 3 | B | source-key-unverified | — |
| 553 | 1 | A | source-key-unverified | — |
| 554 | 1 | A | source-key-unverified | — |
| 555 | 4 | A,C | source-key-unverified | — |
| 556 | 4 | A | source-key-unverified | — |
| 557 | 1 | B | source-key-unverified | — |
| 558 | 1 | B | source-key-unverified | — |
| 559 | 1 | B | source-key-unverified | — |
| 560 | 4 | B | source-key-unverified | — |
| 561 | 1 | A | source-key-unverified | — |
| 562 | 3 | A | source-key-unverified | — |
| 563 | 3 | A,D | source-key-unverified | — |
| 564 | 4 | D,E | source-key-unverified | — |
| 565 | 1 | A | source-key-unverified | — |
| 566 | 3 | B | source-key-unverified | — |
| 567 | 1 | C,D | source-key-unverified | — |
| 568 | 1 | C,D | source-key-unverified | — |
| 569 | 1 | A | source-key-unverified | — |
| 570 | 3 | B,D | source-key-unverified | — |
| 571 | 4 | D | source-key-unverified | — |
| 572 | 3 | C | source-key-unverified | — |
| 573 | 4 | D | source-key-unverified | — |
| 574 | 3 | C | source-key-unverified | — |
| 575 | 3 | B,D | source-key-unverified | — |
| 576 | 3 | A,E | source-key-unverified | — |
| 577 | 1 | B | source-key-unverified | — |
| 578 | 4 | D | source-key-unverified | — |
| 579 | 2 | B | source-key-unverified | — |
| 580 | 1 | A,D | source-key-unverified | — |
| 581 | 4 | A,D | source-key-unverified | — |
| 582 | 1 | A,C,E | source-key-unverified | — |
| 583 | 4 | B | source-key-unverified | — |
| 584 | 3 | B | source-key-unverified | — |
| 585 | 1 | A | source-key-unverified | — |
| 586 | 3 | B | source-key-unverified | — |
| 587 | 3 | A | source-key-unverified | — |
| 588 | 3 | A | source-key-unverified | — |
| 589 | 1 | B | source-key-unverified | — |
| 590 | 3 | D | source-key-unverified | — |
| 591 | 3 | D | source-key-unverified | — |
| 592 | 3 | B,D | source-key-unverified | — |
| 593 | 1 | B | source-key-unverified | — |
| 594 | 3 | C | source-key-unverified | — |
| 595 | 3 | D | source-key-unverified | — |
| 596 | 3 | C | source-key-unverified | — |
| 597 | 1 | C | source-key-unverified | — |
| 598 | 3 | B | source-key-unverified | — |
| 599 | 1 | A,C | source-key-unverified | — |
| 600 | 3 | B,D | source-key-unverified | — |
| 601 | 4 | C | source-key-unverified | — |
| 602 | 3 | C | source-key-unverified | — |
| 603 | 1 | A | source-key-unverified | — |
| 604 | 3 | C | source-key-unverified | — |
| 605 | 3 | A | source-key-unverified | — |
| 606 | 1 | A | source-key-unverified | — |
| 607 | 4 | B | source-key-unverified | — |
| 608 | 3 | A | source-key-unverified | — |
| 609 | 3 | A | source-key-unverified | — |
| 610 | 4 | B,D,F | source-key-unverified | — |
| 611 | 1 | C | source-key-unverified | — |
| 612 | 1 | B | source-key-unverified | — |
| 613 | 4 | B,D | source-key-unverified | — |
| 614 | 3 | B,D,E | source-key-unverified | — |
| 615 | 4 | E | source-key-unverified | — |
| 616 | 4 | D | source-key-unverified | — |
| 617 | 3 | C | source-key-unverified | — |
| 618 | 3 | A | source-key-unverified | — |
| 619 | 3 | A,D | source-key-unverified | — |
| 620 | 3 | B | source-key-unverified | — |
| 621 | 3 | B | source-key-unverified | — |
| 622 | 3 | A,D,F | source-key-unverified | — |
| 623 | 3 | C | source-key-unverified | — |
| 624 | 4 | D | source-key-unverified | — |
| 625 | 4 | B | source-key-unverified | — |
| 626 | 4 | D | source-key-unverified | — |
| 627 | 3 | A | source-key-unverified | — |
| 628 | 3 | C,E | source-key-unverified | — |
| 629 | 1 | D | source-key-unverified | — |
| 630 | 3 | A | source-key-unverified | — |
| 631 | 3 | C | source-key-unverified | — |
| 632 | 3 | A | source-key-unverified | — |
| 633 | 3 | C | source-key-unverified | — |
| 634 | 3 | C | source-key-unverified | — |
| 635 | 2 | C | source-key-unverified | — |
| 636 | 4 | A | source-key-unverified | — |
| 637 | 1 | C | source-key-unverified | — |
| 638 | 4 | C | source-key-unverified | — |
| 639 | 3 | A,D | source-key-unverified | — |
| 640 | 2 | C | source-key-unverified | — |
| 641 | 3 | A,E | source-key-unverified | — |
| 642 | 3 | C | source-key-unverified | — |
| 643 | 3 | B | source-key-unverified | — |
| 644 | 1 | A,D,F | source-key-unverified | — |
| 645 | 1 | A | source-key-unverified | — |
| 646 | 4 | D | source-key-unverified | — |
| 647 | 4 | C | source-key-unverified | — |
| 648 | 3 | C | source-key-unverified | — |
| 649 | 3 | C,E | source-key-unverified | — |
| 650 | 2 | C | source-key-unverified | — |
| 651 | 2 | D | source-key-unverified | — |
| 652 | 3 | D | source-key-unverified | — |
| 653 | 1 | B | source-key-unverified | — |
| 654 | 4 | C | source-key-unverified | — |
| 655 | 3 | B | source-key-unverified | — |
| 656 | 3 | C | source-key-unverified | — |
| 657 | 2 | B | source-key-unverified | — |
| 658 | 3 | D | source-key-unverified | — |
| 659 | 3 | B | source-key-unverified | — |
| 660 | 3 | B | source-key-unverified | — |
| 661 | 3 | C | source-key-unverified | — |
| 662 | 3 | D | source-key-unverified | — |
| 663 | 1 | D | source-key-unverified | — |
| 664 | 3 | A,C | source-key-unverified | — |
| 665 | 3 | D | source-key-unverified | — |
| 666 | 1 | B,C,E | source-key-unverified | — |
| 667 | 2 | C | source-key-unverified | — |
| 668 | 1 | C | source-key-unverified | — |
| 669 | 4 | A,C,F | source-key-unverified | — |
| 670 | 3 | D | source-key-unverified | — |
| 671 | 4 | A | source-key-unverified | — |
| 672 | 4 | A,C,F | source-key-unverified | — |
| 673 | 3 | D | source-key-unverified | — |
| 674 | 4 | B | source-key-unverified | — |

## Q144 — Domain 4 single-answer 18/138 (verified 2026-10-29)

- **Answer: C (AWS Trusted Advisor → EventBridge → Lambda)**. Previously corrected from B in question bank; review reconfirmed from current AWS documentation and exact-question external source.
- **Original question retained** in `src/data/questions.json`; original typo `thecost-effectiveness` preserved.
- **Threshold:** Legacy Trusted Advisor low-utilization EC2 check `Qch7DwouX1` flags ≤10% daily average CPU and ≤5 MB network I/O on at least 4 of previous 14 days. AWS now recommends newer check `c1z7kmr00n`.
- **A incorrect:** CloudWatch dashboard does not implement historical 4-of-14-day combined metric evaluation by itself.
- **B incorrect:** Systems Manager does not provide the stated check; monitoring and history logic would need further implementation.
- **C correct (intended exam answer):** Trusted Advisor evaluates the legacy threshold; EventBridge invokes Lambda to filter environment/department/business-unit tags and stop eligible development EC2 instances.
- **D incorrect:** Custom Lambda collection, DynamoDB storage and QuickSight dashboard add overhead; dashboard alone does not stop instances.
- **Caveats:** Trusted Advisor event delivery best effort and emitted from `us-east-1`; production systems should reconcile periodically, avoid stopping Auto Scaling-managed or critical instances and apply tag-based exclusion rules. AWS documentation now uses Business Support+ terminology.
- **Official references:** https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html ; https://docs.aws.amazon.com/awssupport/latest/user/cloudwatch-events-ta.html ; https://docs.aws.amazon.com/eventbridge/latest/ref/events-ref-trustedadvisor.html
- **Exact-question matches:** https://www.examtopics.com/discussions/amazon/view/143186-exam-aws-certified-solutions-architect-professional-sap-c02-topic-1-question-524-discussion/ ; https://www.examtopics.cn/exam-aws-certified-solutions-architect-professional-1
- **Review classification:** verified-with-legacy-warning. External answer C agrees, but AWS documentation is the technical authority.

## Q146 — Domain 4 single-answer 20/139 (2026-10-29)

- **Answer: B (retained, qualified).** Exact wording/options match CertEnsure SAP-C02 Question 33, which selects B. AWS EKS docs independently support retaining Kubernetes manifests and using managed node groups to reduce node management.
- **Original question:** `A company is migrating a containerized Kubernetes app with manifest files to AWS. What is the easiest migration path?`
- **Original options:** A `App Runner + open-source repo`; B `Amazon EKSwith managed node groups and Aurora`; C `ECS on EC2 + task definitions`; D `Rebuild Kubernetes cluster on EC2 manually`.
- **A incorrect:** App Runner consumes source code or images for web services; no direct Kubernetes manifest deployment semantics.
- **B intended correct:** EKS runs Kubernetes and supports deploying existing manifests using kubectl; managed node groups automate node provisioning and lifecycle. **Defect:** Aurora is not warranted because no database is described. This is best among options, not an unqualified fully specified solution.
- **C incorrect:** ECS needs task definitions, implying conversion from Kubernetes manifests and potentially orchestration changes.
- **D incorrect:** Manually running Kubernetes on EC2 increases control-plane and node maintenance overhead.
- **Source warnings:** Original question/options unusually abbreviated; exact external copy is similarly abbreviated and does not prove complete original exam wording. Typo `EKSwith` preserved. EKS Auto Mode offers additional managed infrastructure in 2026 but is not an answer option.
- **Count discrepancy:** In current `questions.json`, Domain 4 entries with `answerCount===1` number **139**; Q146 is **20/139** in ascending ID order, rather than 19/138 inferred from prior turn. Do not change dataset counts or IDs without separate audit.
- **Official docs:** https://docs.aws.amazon.com/eks/latest/userguide/sample-deployment.html ; https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html ; https://docs.aws.amazon.com/eks/latest/userguide/automode.html ; https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html ; https://docs.aws.amazon.com/apprunner/latest/dg/service-source-code.html
- **External exact match:** https://www.certensure.com/amazon-web-services/sap-c02-cert-practice-test.html (Question 33).
- **Classification:** `verified-intended-answer-with-defective-wording`; preserve original key B and source text. React question data populated with explanation, option analysis, plain words, key points, source warning, and review metadata.

## Q148 — Domain 4 single-answer 21/139 (reviewed 2026-10-29)

- **Verified answer C**, original answer retained: cross-Region Amazon RDS for MySQL read replica in Europe and Route 53 latency-based routing to regional API Gateway APIs. External exact match CertEnsure SAP-C02 Question 150 also selects C.
- **A wrong:** DMS full load alone does not keep the regional database current after migration, despite appropriate latency routing.
- **B wrong:** DMS full load+CDC can replicate ongoing changes but adds operational management, while geolocation routing targets geographic locations rather than lowest measured latency.
- **C correct:** Native RDS asynchronous cross-Region read replication supports >90% read-only reports in Europe, while Route 53 latency records select a low-latency regional API. Regional Lambda must use regional read endpoints and direct writes to US primary.
- **D wrong:** Replica suitable but geolocation routing not latency optimized. **Source defective:** Option D ends at `connect to the API` in both source JSON and exact external Question 150; do not invent missing text.
- **Caveats:** Replica lag and eventual consistency; CloudFront for frontend does not eliminate backend API/database latency. CertEnsure explanation includes unrelated Redshift options and must not be treated as reliable option-specific reasoning.
- **AWS sources:** https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.XRgn.html ; https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html ; https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-latency.html ; https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-geo.html ; https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Task.CDC.html
- **External exact match:** https://www.certensure.com/amazon-web-services/sap-c02-cert-practice-test.html (Question 150, key C).
- **Classification:** `verified-answer-with-truncated-option`. Original stem and options preserved; React source JSON now has explanations, sources and defect flags.

## Q153 — Domain 4 single-answer 22/139 (reviewed 2026-10-29)

- **Verified answer A** (retained): ECS Fargate with Amazon EFS meets Docker, NFS version 4, secure shared storage and no underlying host management requirements.
- **Original stem/options:** Preserved verbatim in `src/data/questions.json`; complete wording independently matched at ExamTopics SAP-C02 topic 1 Q191 and PUPUWEB.
- **A correct:** Fargate manages container infrastructure, EFS provides managed elastic NFS shared storage; ECS task definition configures EFS file system ID, mount point and IAM authorization.
- **B wrong:** FSx for Lustre uses Lustre rather than NFSv4 and AWS explicitly states FSx for Lustre cannot be mounted by Fargate tasks.
- **C wrong:** EFS appropriate but ECS EC2 launch type requires customer-managed EC2 instances, patching, capacity and host configuration, violating no infrastructure management.
- **D wrong:** EC2 management remains, and EBS Multi-Attach is block storage rather than NFSv4 shared file service; multi-writer correctness needs careful file-system coordination.
- **Minor source imprecision:** 'EFS authorization IAM role' is not a separate ECS task definition field. EFS IAM authorization uses ECS **task IAM role** with `authorizationConfig.iam=ENABLED`, `transitEncryption=ENABLED`. For secure use restrict TCP 2049 via security groups, apply least privilege and EFS access points.
- **AWS references:** https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specify-efs-config.html ; https://docs.aws.amazon.com/AmazonECS/latest/developerguide/efs-best-practices.html ; https://docs.aws.amazon.com/fsx/latest/LustreGuide/mounting-ecs.html
- **External exact question:** https://www.examtopics.com/discussions/amazon/view/110392-exam-aws-certified-solutions-architect-professional-sap-c02/ ; https://pupuweb.com/aws-sap-c02-exam-question-answer-secure-scalable-containerized-solution/ (selects A).
- **Classification:** `verified-answer-minor-iam-terminology`; answer A retained. Question data now has explanation, per-option reasoning, study notes, source warning and references for React display.

## Q160 — Domain 4 single-answer 23/139 (2026-10-29)

- **AWS-doc-verified answer C retained:** ECS services on Fargate spread multiple tasks across AZs, and adding an Aurora PostgreSQL reader in another AZ supplies automatic failover target.
- **A wrong:** RDS Proxy and Aurora Replica improve database availability but leave the single EC2 ECS host as an application SPOF.
- **B wrong:** Cross-Region reader and scripted manual failover create unnecessary operational overhead and do not provide automatic writer failover.
- **C correct:** AWS-managed Fargate removes EC2 instance operations and distributes ECS tasks across AZs; Aurora Replica in another AZ can be promoted automatically if writer fails.
- **D wrong:** Multi-Region global DB and active-active DNS add complexity; Aurora Global Database normally has a single writable primary Region, so routing both Regions active-active does not independently enable writes.
- **Defects/caveats:** Aurora's cross-AZ reader configuration should not be conflated with the distinct RDS Multi-AZ DB cluster product (writer + two readers across 3 AZs). Production needs >=2 Fargate tasks, multi-AZ ALB, health checks, and idempotent payment processing.
- **Official AWS evidence:** https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-rebalancing.html ; https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_service-options.html ; https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraHighAvailability.html ; https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html
- **External exam sites:** Exact independent question match **not established**; external answer-key verification pending. Do not classify as exact-site-verified.
- **Classification:** `aws-doc-verified-external-exact-match-pending`. Original question and options preserved. JSON populated with explanations, review notes, and source warnings for React.

## Q161 — Domain 4 single-answer 24/139 (2026-10-29)

- **Answer A verified by current AWS documentation**, original JSON answer retained. Use AWS Transfer Family managed SFTP with internet-facing VPC-hosted endpoint and one Elastic IP per selected subnet, backed by EFS Regional shared NFS storage accessible to downstream applications, including via Direct Connect if networking allows.
- **A correct:** Transfer Family VPC internet-facing endpoints support fixed public EIPs, multi-AZ hosting and EFS NFS backing; least operational overhead.
- **B incorrect:** Ordinary public Transfer Family endpoint cannot associate static Elastic IPs, violating vendor allowlist requirement.
- **C incorrect:** Lift-and-shift to a single EC2 SFTP host retains single compute SPOF and host administration.
- **D incorrect:** AWS MGN cannot migrate VM into managed Transfer Family; ordinary public endpoint lacks EIP; FSx for Lustre not an NFS replacement.
- **Exact external match:** https://www.scribd.com/document/921182718/SAP-C02-CSL-09-26-341 Question 292. **WARNING: external printed key B is wrong**; community votes A (100%), and official AWS endpoint matrix definitively supports A.
- **OCR/source defects:** Original JSON options contain typos `pace`, `Fie system`, `EFSfile`, `FSx for Luster`, malformed punctuation. Cleaner complete wording available in the external Question 292; original source strings preserved in JSON, with warnings, rather than silently edited.
- **AWS docs:** https://docs.aws.amazon.com/transfer/latest/userguide/sftp-for-transfer-family.html ; https://docs.aws.amazon.com/transfer/latest/userguide/create-server-in-vpc.html ; https://docs.aws.amazon.com/transfer/latest/userguide/configure-storage.html ; https://docs.aws.amazon.com/transfer/latest/userguide/
- **Implementation notes:** EFS Regional file system and mount targets across AZs, TCP 2049 for NFS, Transfer Family endpoint source-IP security groups, Direct Connect routes and IAM/POSIX permissions.
- **Classification:** `aws-doc-verified-external-key-conflict-ocr-defects`; answer A retained; JSON populated for React with detailed explanation, option analysis, sources and warnings.

## Q168 — Domain 4 single-answer 25/139 (2026-10-29)

- **Historical answer B retained (qualified/outdated):** Application Discovery Agent captures utilization, running processes and TCP network dependencies on physical and virtual hosts; Migration Hub Strategy Recommendations supports migration strategy analysis.
- **Original stem/options:** Short/abbreviated in source; preserved verbatim in JSON. No complete original question or exact third-party exam-site match established.
- **A wrong:** Migration Evaluator with Agentless Collector helps assessment/cost and VMware/DB inventory but is not the strongest choice for comprehensive physical-server and application/process dependencies.
- **B historically correct:** Discovery Agent covers physical/VM hosts, processes, network connections and performance; Strategy Recommendations provides migration options. **2026 defect:** AWS Migration Hub stopped accepting new customers Nov 7 2025, and AWS recommends AWS Transform for new projects; existing customers continue using Migration Hub.
- **C wrong:** Agentless Collector differs from Discovery Agent for process/physical-host discovery, and vague 'Migration Service' does not provide the stated migration strategy workflow.
- **D wrong:** CSV/import requires previously collected data and cannot inspect runtime processes/network dependencies.
- **AWS sources:** https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-agent.html ; https://docs.aws.amazon.com/application-discovery/latest/userguide/what-is-appdiscovery.html ; https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/getting-started-get-recommendations.html ; https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/migrationhub-availability-change.html
- **External study source (not exact exam question):** https://certnotes.cloud/services/migration-transfer/application-discovery-service/ supports agent/agentless comparison and 2025 availability change. **Exact external question match pending**; do not claim independently confirmed third-party answer key.
- **Classification:** `historically-correct-outdated-migration-hub-new-customers`. Original wording retained; JSON explanation, per-option reasoning, references, status and warnings added for React.
