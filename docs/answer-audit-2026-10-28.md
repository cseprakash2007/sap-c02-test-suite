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

## Q171 — Domain 4 single-answer 26/139 (2026-10-29)

- **Verified answer B retained.** Existing on-premises Hyper-V capacity hosts DataSync agent, reads zipped image archives from NFS, copies directly to S3 Glacier Deep Archive; schedule off-hours and apply DataSync bandwidth throttle. Deep Archive hours-to-days restore fits retrieval within one week.
- **A wrong:** Unneeded GPU EC2 host plus higher-cost Glacier Instant Retrieval for access that need not be instant.
- **B correct:** Hyper-V VM DataSync agent, direct NFS to S3 Glacier Deep Archive, built-in transfer scheduling/throttling; least long-term cost for rare retrieval.
- **C wrong:** Extra EC2 compute and S3 Standard temporary staging/lifecycle transition cost; direct Deep Archive transfer is supported.
- **D wrong:** Tape Gateway uses virtual tape/backup workflow, not straightforward NFS ZIP file transfer; adds workflow changes and complexity.
- **AWS documentation:** https://aws.amazon.com/datasync/faqs/ ; https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html (direct Deep Archive supported; archived object restore needed; verification setting).
- **Exact external match:** https://www.examtopics.com/discussions/amazon/view/136604-exam-aws-certified-solutions-architect-professional-sap-c02-topic-1-question-457-discussion/ (SAP-C02 Q457); https://www.freecram.net/question/Amazon.SAP-C02.v2026-03-31.q264/a-company-has-an-application-that-analyzes-and-stores-image-data-on-premises-the-application-receives (answer B).
- **Source defects:** OCR `imagestogether`, `t week` = **1 week**, `dunng`, missing punctuation. Preserve original JSON stem/options; corrected copy externally confirmed.
- **Operational caution:** Delete source only after successful verified transfer; use DataSync Verify only data transferred for Deep Archive; archive retrieval requires an S3 restore operation.
- **Classification:** `verified-aws-doc-external-exact-match-source-ocr`; React question data enriched with option-by-option explanation, plain words, AWS and external references, and source warning.

## Q176 — Domain 4 single-answer 27/139 (2026-10-29)

- **Verified intended answer D**, source key retained. Elastic Beanstalk Tomcat load-balanced environment with Auto Scaling across AZs + RDS for PostgreSQL + ALB; CloudFront can accelerate cacheable/static content. Lowest operational overhead among options.
- **A incorrect:** Manual EC2 Tomcat and PostgreSQL deployment plus Step Functions custom scale-out has high operational burden; EFS is not a managed relational DB architecture.
- **B incorrect:** EKS multi-Region container and PostgreSQL deployment introduces unnecessary Kubernetes/stateful DB operations; NLB is not an auto-scaler.
- **C incorrect:** Refactoring Java to Python is infeasible without source code, DynamoDB requires major data/application redesign, Storage Gateway unrelated to scale-out.
- **D best available:** Elastic Beanstalk supports Java/Tomcat, managed EC2 provisioning and Auto Scaling; RDS PostgreSQL removes database host management. ALB balances; Auto Scaling scales capacity; CloudFront optional for cacheable traffic.
- **Critical source defect:** Stem says only Java Archive **JAR** files can be deployed, but Elastic Beanstalk **Tomcat** expects a deployable **WAR**. Elastic Beanstalk **Java SE** can run an executable JAR, which is not the same as an arbitrary Tomcat JAR. If only library JARs are available, none of the options fully specifies a deployable artifact. Preserve source text and qualify answer D.
- **Official AWS:** https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_Java.html ; https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/java-tomcat-platform.html ; https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/java-se-platform.html ; https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/java-rds.html
- **Exact external matches:** https://www.examtopics.com/discussions/amazon/view/142998-exam-aws-certified-solutions-architect-professional-sap-c02-topic-1-question-504-discussion/ (Q504); https://www.certstopics.com/questions/exactprep-sap-c02-questions.html (Q48, key D). Both retain packaging ambiguity.
- **Classification:** `verified-intended-answer-with-jar-war-packaging-defect`. Original stem/options preserved; JSON enriched with option analysis, explanations, references and source warning for React.

## Q178 — Domain 4 single-answer 28/139 (2026-10-29)

- **Verified intended answer B retained:** GitHub change-event webhook, existing Jenkins build/test workflow, SNS bad-build alerts, and CodeDeploy blue/green traffic shifting for safer rollback.
- **A wrong:** GitHub 'websockets' incorrect for source-change triggers; in-place all-at-once deployment risks downtime.
- **B best intended:** GitHub webhook, Jenkins test/build integration, SNS failure alerts, CodeDeploy blue/green deployment and rollback. Blue/green needs configured health checks and traffic shifting to achieve minimal/zero user-visible downtime.
- **C wrong:** GitHub websockets wrong; AWS X-Ray is tracing, not unit testing/static analysis. Blue/green alone does not rescue choice.
- **D wrong:** X-Ray is not a test framework; all-at-once in-place deployment risks interruption.
- **Exact external question match:** https://myportal.utt.edu.tt/ICS/icsfs/e500bdfa-17d4-440e-8e02-1a46ed59d675.pdf?target=95f8256a-0bbf-48f2-b967-cb2097efacb3 . **IMPORTANT: external answer letter C corresponds to the same technical text as JSON answer B because external options are reordered.** Never change the user's JSON key to C.
- **2026 AWS guidance:** https://docs.aws.amazon.com/codepipeline/latest/userguide/update-github-action-connections.html ; https://docs.aws.amazon.com/codepipeline/latest/userguide/connections-github.html ; https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-CodestarConnectionSource.html . For new pipelines AWS recommends GitHub App via AWS CodeConnections rather than old OAuth-plus-separate-webhook GitHub source action.
- **Defects:** OCR `sates`, `CodePipelme`, `inan`, `blue'green`, `m-place`; 'Jenkins plugin for AWS CodeBuild' is ambiguous (Jenkins CodePipeline action vs Jenkins invoking CodeBuild); zero downtime depends on deployment readiness and traffic-shifting details.
- **Classification:** `verified-intended-b-external-option-reordered-legacy-github-source`. Original question/options preserved; React JSON enriched with explanations, AWS/external refs, warnings and answer status.

## Q183 — Domain 4 single-answer 29/139 (2026-10-29)

- **Verified answer B retained.** API Gateway HTTP API `SQS-SendMessage` integration receives REST/HTTP requests, SQS buffers traffic, Lambda polls SQS via event source mapping to run business logic, Lambda publishes to AppSync Events HTTP endpoint, clients subscribe via managed WebSockets.
- **A wrong:** Step Functions state machines do not use arbitrary connected WebSocket clients as targets or deliver WebSocket streams.
- **B correct:** API Gateway HTTP API + SQS + Lambda + AWS AppSync Events provides fully managed ingestion, burst decoupling, processing and real-time WebSocket broadcasting.
- **C wrong:** Direct SQS-AppSync integration and EventBridge rules with arbitrary WebSocket clients as targets are not supported as described.
- **D wrong:** CloudFront Functions cannot be CloudFront origins or serve as general application logic with IoT MQTT publishing; IoT Core WebSockets support alone is insufficient.
- **AWS evidence:** https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-aws-services.html ; https://docs.aws.amazon.com/lambda/latest/dg/services-sqs-configure.html ; https://docs.aws.amazon.com/appsync/latest/eventapi/publish-http.html ; https://docs.aws.amazon.com/appsync/latest/eventapi/event-api-websocket-protocol.html ; https://docs.aws.amazon.com/appsync/latest/devguide/ (AppSync Events available since March 2025).
- **Exact independent exam-site match:** https://www.dumpspedia.com/sap-c02-aws-certified-solutions-architect-professional-dumps.html Question 179, matching original stem and options.
- **Minor technical source defect:** SQS does **not** itself push-invoke Lambda; Lambda polls via an event source mapping. AppSync Events requires Event API/channel/authorization and HTTP publish request, omitted in simplified answer. Consider SQS/Lambda idempotency, retry and DLQ handling.
- **Classification:** `verified-aws-doc-external-exact-match-minor-technical-imprecision`. Original stem and options preserved, source answer B retained, explanations/links/warnings added to JSON for React.

## Q185 — Domain 4 single-answer 30/139 (2026-10-29)

- **Verified answer D retained:** AWS Cloud WAN core network with native AWS Direct Connect gateway attachments supplies dedicated on-premises connectivity, centrally managed multi-Region routing/segmentation, and BGP dynamic route propagation.
- **A wrong:** Global Accelerator optimizes endpoint traffic but does not establish a dedicated private link to existing on-premises HSMs.
- **B wrong:** Standard Site-to-Site VPN plus TGW gives centralized routing/encrypted tunnels, but not dedicated private Direct Connect connectivity.
- **C wrong:** CloudHSM replaces or changes the on-premises HSM deployment rather than connecting the existing HSMs to AWS workloads.
- **D correct:** Direct Connect provides dedicated circuit, Cloud WAN centralizes policy and global routing. Native Direct Connect gateway attachments avoid a mandatory intermediate TGW.
- **AWS current evidence:** https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-dxattach-about.html ; https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-dxattachment-add.html ; https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-cloud-wan.html ; https://aws.amazon.com/about-aws/whats-new/2024/11/aws-cloud-wan-on-premises-connectivity-direct-connect/ .
- **Exact external match:** https://www.certensure.com/amazon-web-services/sap-c02-cert-practice-test.html Q15, same wording and options, answer D.
- **Source implementation caveat:** Option D omits Direct Connect physical connection, Direct Connect gateway, transit virtual interface, BGP and Cloud WAN core-network/VPC attachments. Direct Connect is not inherently encrypted; payment workloads require appropriate TLS/MACsec, redundancy and security review.
- **Outdated external/AWS background:** Pre-November 25, 2024 architecture articles that require intermediate Transit Gateway for Cloud WAN–Direct Connect are stale. Native gateway attachment is now supported.
- **Classification:** `verified-aws-doc-external-exact-match-implementation-caveats`. Original stem/options preserved; JSON explanation, option analysis, warnings and references updated for React.


### Domain 4 Q186 — single-answer 31/139 (2026-10-29)
- **Original source answer: B**, confirmed by matching third-party practice question at [CertEnsure Q7](https://www.certensure.com/amazon-web-services/sap-c02-cert-practice-test.html) and [FreeCram](https://www.freecram.net/question/Amazon.SAP-C02.v2026-08-19.q305/a-company-wants-to-modernize-a-monolithic-application-in-the-company-s-data-center-and-deploy-the-application).
- **Audit verdict: DEFECTIVE / NON-UNIQUE. A is also valid.** AWS documents cross-account SNS topic subscription to independent per-microservice SQS queues: https://docs.aws.amazon.com/sns/latest/dg/sns-send-message-to-sqs-cross-account.html .
- **B** central EventBridge with content-filter rules works when event bus or cross-account targets and appropriate IAM execution roles/resource policies are configured: https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-cross-account.html ; https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-cross-account.html .
- **C** falsely implies a Kinesis stream can directly invoke arbitrary Fargate microservices without consumer implementation. **D** shares a single SQS competing-consumer queue and does not fan out every message.
- **Correction proposal:** Add a requirement for per-microservice *content-based routing by event fields* and central rules; otherwise accept A and B. Keep original wording and options unchanged for traceability.


### Domain 4 Q199 — single-answer 32/139 (2026-10-29)
- **Source answer B VERIFIED**, exact external [CertEmpire SAP-C02 PDF Q7](https://certempire.com/demo-files/sap-c02-demo-certempire.pdf).
- ECS on EC2 consolidates Java/Node.js containers, supports multi-hour jobs and task/cluster scaling. AWS: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-auto-scaling.html and https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-scaling-behavior.html .
- A cannot accommodate uninterrupted several-hour processing: standard Lambda 15 min; eligible Lambda Managed Instances async/ESM 90 min since September 2026 (https://aws.amazon.com/blogs/compute/announcing-90-minute-function-timeout-on-aws-lambda-managed-instances/). C per-app Beanstalk has inefficient baseline; D reserves peak fleet for 3 years.
- Source typos preserved ('tor', punctuation); 75% memory target is not guaranteed optimal, recommend ECS capacity providers, binpack and scheduled task runs where applicable.


### Domain 4 Q200 — single-answer 33/139 (2026-10-29)
- Source answer **C** best-supported by AWS docs; no exact third-party exam match independently confirmed. Original question and options retained.
- Aurora Global Database: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.html ; AWS Backup Vault Lock: https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html .
- A multivalue routing not failover, regional ECR dependency; B omits tamper protection and S3 recovery; C ECR replication, ECS secondary, Aurora global, compliance vault, S3 backup/replication, Route 53 failover; D governance mode removable and geolocation not failover.
- Warnings: source typo 'secondaryrecord'; S3 PITR ambiguous (versioning versus continuous AWS Backup); asynchronous CRR does not guarantee 5-minute RPO; compliance vault lock does not automatically protect live S3 objects; RTO 15 minutes requires health checks, failover orchestration, tests.


### Domain 4 Q202 — single-answer 34/139 (2026-10-29)
- **Answer B AWS-doc verified**: EKS managed node groups can use custom host AMIs via EC2 launch templates to install proprietary security agents, while AWS manages Kubernetes control plane and node lifecycle; DMS to RDS MySQL Multi-AZ.
- AWS references: https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html ; https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html .
- A feasible host agent but higher self-managed orchestration overhead; C Lambda host agents unavailable; D **invalid** because Fargate cannot use a custom host AMI.
- Caveats: custom AMI bootstrapping, node patching remain customer responsibilities; Multi-AZ standby is not a readable replica. Exact independent exam-site match **not confirmed**. Original wording/options preserved.


### Domain 4 Q208 — single-answer 35/139 (2026-10-29)
- **Answer C AWS-doc verified**: SQL Server Always On -> RDS for MySQL heterogeneous migration uses schema conversion (SCT or DMS Schema Conversion) followed by AWS DMS data migration/CDC. AWS walkthrough: https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-sql-server-mysql.html ; overview: https://aws.amazon.com/documentation-overview/dms/ .
- A incompatible SQL Server native restore into MySQL; B Snowball/S3 transport does not convert schema and SQL Server BULK INSERT is wrong target mechanism; C correct; D DataSync files/S3 cannot convert relational engine.
- Defects: option C 'MeSQL' typo preserved; AWS recommends managed DMS Schema Conversion over legacy SCT now (https://docs.aws.amazon.com/dms/latest/userguide/CHAP_GettingStarted.SCT.html); business-critical migration requires SQL Server Always On CDC checks, code conversion, validation and HA. **Exact third-party exam-site match not verified**.


### Domain 4 Q211 — single-answer 36/139 (2026-10-29)
- **B independently verified**: AWS DataSync scheduled SMB->Amazon FSx for Windows File Server over Direct Connect, supports Windows ACL/metadata preservation. AWS: https://docs.aws.amazon.com/fsx/latest/WindowsGuide/migrate-files-to-fsx-datasync.html ; https://docs.aws.amazon.com/datasync/latest/userguide/create-smb-location.html .
- Exact external matches **B**: https://www.freepdfdumps.com/Amazon.SAP-C02.v2024-09-24.q208.html?p=31 (Q150); https://cciedump.spoto.net/exam-questions/free-aws-sap-c02-practice-questions-answers-2026-part2 (Q137); https://www.certensure.com/amazon-web-services/sap-c02-cert-practice-test.html (Q183).
- A S3-backed File Gateway not direct Windows FSx replication; B correct; C Data Pipeline unsuitable and EFS NFS; D DataSync SMB->EFS **supported**, but EFS lacks native Windows SMB semantics.
- Original text preserved. Defects: B should specify FSx for Windows File Server; D 'lo' typo; C 'on- premises' spacing. For implementation verify SMB permissions, AD/NTFS ACL transfer and DataSync agent networking.


### Domain 4 Q212 — single-answer 37/139 (2026-10-29)
- Historical answer **C** verified for **existing** Migration Hub users: Application Discovery Agent collects on-prem physical/VM metrics, running processes, TCP connections; Migration Hub groups applications and generates EC2 sizing recommendations. https://docs.aws.amazon.com/application-discovery/latest/userguide/what-is-appdiscovery.html ; https://docs.aws.amazon.com/migrationhub/latest/ug/ec2-recommendation-prerequisites.html .
- **MAJOR OUTDATED/DEFECTIVE SOURCE**: AWS Migration Hub stopped accepting **new customers Nov 7, 2025**; AWS recommends **AWS Transform** for new migrations. https://docs.aws.amazon.com/migrationhub-strategy/latest/userguide/migrationhub-availability-change.html . None of four options reflects the current new-customer recommendation; preserve historical source C with warning.
- A SSM/Application Manager/Pricing Calculator do not provide complete discovery/sizing pipeline; B Inspector is vulnerability scanning; C historically correct; D CloudWatch agent/Compute Optimizer lack comprehensive migration dependency mapping.
- Independent external technical note corroborates retirement: https://certnotes.cloud/services/migration-transfer/migration-hub/ . No exact external practice-site question match confirmed. Original question/options preserved.


### Domain 4 Q217 — single-answer 38/139 (2026-10-29)
- **Historical source C; defective for new 2026 customers.** Snowball Edge no new customers since 2025-11-07 (https://docs.aws.amazon.com/snowball/latest/developer-guide/snowball-edge-availability-change.html), end of support in commercial Regions 2026-12-31 (https://aws.amazon.com/snowball/).
- C's DMS S3 source requires structured CSV/Parquet and mappings, not raw MySQL backups (https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.S3.html). A Direct Connect 1 Gbps + DMS valid; 60 TB theoretical transfer ~5.6 days before overhead, but provisioning unknown. Cannot prove which option takes least total time without shipping/provisioning estimates.
- B DataSync+MGN does not migrate DB into Aurora; D old Snowball/S3 Adapter + MGN S3->Aurora unsupported. Typos in stem/choices. External exact exam-site match not confirmed. Original wording/key preserved and marked outdated-defective.


### Domain 4 Q218 — single-answer 39/139 (2026-10-29)
- **D verified** by AWS oracle_fdw documentation https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/postgresql-oracle-fdw.html and RDS PostgreSQL extension versions https://docs.aws.amazon.com/AmazonRDS/latest/PostgreSQLReleaseNotes/postgresql-extensions.html . AWS SCT/DMS migrates selected Oracle DBs to RDS PostgreSQL; PostGIS spatial, pg_cron scheduled SQL jobs, oracle_fdw queries retained Oracle tables over Direct Connect.
- Exact third-party matches select **D**: https://www.examtopics.cn/exam-aws-certified-solutions-architect-professional-4 (Q36 No1508) and https://www.certensure.com/amazon-web-services/sap-c02-cert-practice-test.html (Q6).
- A DynamoDB/API Gateway not foreign tables; B SQL Server native replication and Glue crawler cannot create Oracle foreign tables; C MGN not bidirectional database CDC, IGW not foreign tables; D correct with omitted setup.
- **Source caveats:** 'native spatial' needs PostGIS; 'cron on DB instance' means pg_cron SQL jobs not OS crontab; Direct Connect only network path—must install oracle_fdw and configure foreign server, user mapping, foreign table, security/routing. Preserve original wording.


### Domain 4 Q220 — single-answer 40/139 (2026-10-29)
- **Answer A AWS-doc verified**: one VGW attached to VPC, two Site-to-Site VPN connections to separate CGWs, each VPN has two tunnels. AWS https://docs.aws.amazon.com/vpn/latest/s2svpn/vpn-redundant-connection.html and https://docs.aws.amazon.com/vpn/latest/s2svpn/vpn-edit-static-routes.html .
- B: customer gateway cannot attach to VPC; C: invalid two-VGW topology and propagation from CGW; D: same plus incorrectly one tunnel per VPN.
- Source defects: OCR '5ite-to-5ite' and 'Site-to-Slte'; propagation should be on relevant route tables, not all; static VPN requires remote CIDR routes on connections. No exact external practice-site question match confirmed. Original wording preserved.


### Domain 4 Q221 — single-answer 41/139 (2026-10-29)
- **Answer B verified**, including exact independent exam-site match and B key: https://www.p2pexams.com/free-questions/amazon-sap-c02-dumps-by-holden-24-05-2024-12qa-certsdeals.pdf . AWS DMS full load + CDC keeps new-account Aurora MySQL target updated while source remains live. https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Task.CDC.html ; https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html ; AWS cross-account migration https://aws.amazon.com/blogs/database/perform-cross-account-amazon-aurora-mysql-migration-with-minimal-downtime/ .
- A snapshot-only and C AWS Backup snapshot-only cannot capture subsequent writes; D AWS Application Migration Service moves servers, not Aurora DB-to-DB logical CDC.
- Source omissions: B should explicitly require full-load+CDC, row-format MySQL binlogs, DMS permissions, cross-account networking/security groups, replication lag monitoring and coordinated brief write pause at cutover. DMS is asynchronous, not guaranteed real-time. AWS documents same-Region Aurora clone + native binlog replication as a potentially faster alternative absent from options: https://aws.amazon.com/blogs/database/cross-account-amazon-aurora-mysql-migration-with-aurora-cloning-and-binlog-replication-for-reduced-downtime/ . No material outdated service. Original question/options preserved.


### Q221 — Domain 4, position 41/139 (2026-10-29): disputed question cardinality

- **Repo single-answer key:** B, AWS DMS Aurora-to-Aurora full-load and CDC. Technically correct *for a single-answer variant*.
- **Source conflict:** [ExamsVCE single-answer B](https://www.examsvce.com/sap-c02/a-company-wants-to-migrate-an-amazon-question-answer.html) and [P2PExams single-answer B](https://www.p2pexams.com/free-questions/amazon-sap-c02-dumps-by-holden-24-05-2024-12qa-certsdeals.pdf) vs. [exam-tests choose-two variant](https://www.exam-tests.com/SAP-C02-exam/Amazon.SAP-C02.v2026-06-29.q712.html?p=2) and ExamTopics reproductions with A+B. Do not assert proven original single-answer cardinality.
- **AWS validation:** [DMS CDC tasks](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Task.CDC.html) confirms full-load+CDC; [AWS cross-account Aurora blog](https://aws.amazon.com/blogs/database/perform-cross-account-amazon-aurora-mysql-migration-with-minimal-downtime/) expressly advocates snapshot+subsequent replication (AWS DMS or native binlog). A-only snapshot, C-only AWS Backup recovery point, and D server-lift-and-shift do not provide live database change replication.
- **Caveats:** MySQL ROW binlogs, retention, privileges and cross-account network connectivity required. Stop source writes, monitor lag, validate data, then switch DNS. CDC is asynchronous; cannot guarantee zero downtime. Confirm authoritative source question version before considering Q221 a *genuine* single-answer item.


### Q224 — Domain 4, position 42/139 (2026-10-29)

- **Answer:** B (single answer). Create an AWS CloudTrail **organization trail** in the AWS Organizations management account; configure it for all accounts. A delegated administrator is also supported.
- **AWS verification:** [CloudTrail organization trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html) automatically deploys to current and new accounts; [AWS Organizations integration](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-cloudtrail.html) confirms automatic application.
- **External question matches:** [SalesforceExamDumps](https://www.salesforcexamdumps.com/sap-c02-practice-questions/2), [DumpsPedia](https://www.dumpspedia.com/sap-c02-aws-certified-solutions-architect-professional-dumps.html), [P2PExams](https://www.p2pexams.com/free-questions/certsinside-sap-c02-aws-certified-solutions-architect-professional-exam-verified-questions-answers-by-burgess-15-04-2024-12qa.pdf). No Choose TWO/THREE variant identified in checked sources; copied source text is not independent AWS authority.
- **Options:** A daily Lambda/EventBridge job is custom and may leave a delay; B is native, centralized and automatic; C requires per-account manual upkeep; D adds unnecessary SSM Automation/State Manager complexity.
- **Source defects:** Original text contains 'will cost' (likely 'will create'), 'turns on AWS accounts' (likely CloudTrail), 'AYYS', 'dally', 'Automaton'. Original stem/options remain unchanged; annotate rather than silently rewrite.


### Q227 — Domain 4, position 43/139 (2026-10-29)

- **Correct answer: C** (single answer). Use IAM policy on developer IAM identities restricting `ec2:RunInstances` using `ec2:InstanceType`. For strong enforcement add explicit Deny with `StringNotEquals` for unapproved types.
- **AWS documentation:** [EC2 example policies](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ExamplePolicies_EC2.html) explicitly documents allowed instance-type lists; [EC2 console policy examples](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-ec2-console.html).
- **External exact-stem copies:** [ExamsReviews](https://www.examsreviews.com/articles/best-preparations-of-sap-c02-exam-2025-aws-certified-solutions-architect-unlimited-510-questions-q190-q208/), [FreeCram](https://www.freecram.net/Amazon.SAP-C02.v2025-04-03.q227.pdf), [AllFreeDumps](https://www.allfreedumps.com/downloadfile.html?id=23185). No explicit Choose TWO/THREE variant identified in the searched sources; not authoritative proof of original cardinality.
- **Options:** A AWS Config is detective rather than preventative; B launch templates require separate IAM policy enforcement; C IAM conditions prevent unapproved launches; D EC2 Image Builder creates AMIs rather than instance-type controls.
- **Defects:** 'tothe' typo; option C calls members of an IAM group 'IAM accounts' (should be IAM users); original text/options preserved with annotations.


### Q228 — Domain 4, position 44/139 (2026-10-29)

- **Answer: C**, single-choice variant verified on [Pass2Lead](https://www.pass2lead.com/sap-c02.html); exact stem and answer C on [CertEnsure](https://www.certensure.com/amazon-web-services/sap-c02-cert-practice-test.html). No conflicting Choose TWO/THREE version found in checked searches; this does not prove none exists.
- **AWS primary sources:** [AWS IoT Core Firehose rule action](https://docs.aws.amazon.com/iot/latest/developerguide/kinesis-firehose-rule-action.html); [AWS IoT -> Firehose -> Lambda -> S3 reference architecture](https://aws.amazon.com/blogs/iot/ingesting-enriched-iot-data-into-amazon-s3-using-amazon-kinesis-data-firehose/); [Firehose Lambda transform](https://aws.amazon.com/firehose/faqs/); [2024 Firehose rename](https://aws.amazon.com/about-aws/whats-new/2024/02/amazon-data-firehose-formerly-kinesis-data-firehose/).
- **Options:** A EC2 active/standby + DNS is self-managed and incomplete Kafka data durability; B MSK behind NLB is not a complete MQTT-native ingress/transformation/S3 solution; C managed IoT Core MQTT ingestion -> Firehose -> Lambda -> S3; D single EC2 Kafka server recreates a single failure dependency.
- **Source defects:** '10.000', 'on- premises', 'loT', 'NL8' transcription errors; 'Kinesis Data Firehose' renamed 'Amazon Data Firehose' in Feb 2024. External explanation claiming MSK cannot handle 10k sensors is misleading; not an AWS technical limit established by the question.
- **Operational caveat:** QoS, retry, failure destinations, monitoring, and raw record backup matter; best exam choice C does not promise absolute zero data loss. Original stem/options preserved.


### Q238 — Domain 4, position 45/139 (2026-10-29)

- **Correct answer: D** (single answer). ECS EC2 launch type for complex orchestration with host/network control; Aurora MySQL Serverless v2 for relational data; SQS for asynchronous queues.
- **AWS references:** [ECS launch types](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html); [Aurora Serverless v2](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.html); [SQS developer guide](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html); [AWS Schema Conversion Tool](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html).
- **External exact-stem single-answer matches:** [Exam-Tests](https://www.exam-tests.com/SAP-C02-exam/Amazon.SAP-C02.v2024-12-04.q106.html?p=20), [DumpsQuestion](https://examsdocs.dumpsquestion.com/articles/assume-amazon-sap-c02-dumps-pdf-are-going-to-be-the-best-score-q27-q52/), [SalesforceExamDumps](https://www.salesforcexamdumps.com/sap-c02-practice-questions/9), [ExamTopics](https://www.examtopics.com/discussions/amazon/view/126814-exam-aws-certified-solutions-architect-professional-sap-c02-topic-1-question-346-discussion/). No conflicting Choose TWO/THREE variant identified in checked sources.
- **All options:** A App Runner lacks full host control (although RDS SQL Server is relational); B Fargate lacks host control and DynamoDB is nonrelational; C Beanstalk is less appropriate for complex container orchestration, Kafka streaming not MSMQ-like simple queues; D meets host, orchestration, relational and async queue needs.
- **Critical external source defect:** Exam-Tests says Aurora MySQL is 'using the same database engine as SQL Server'; **false**. SQL Server -> Aurora MySQL requires heterogeneous schema/query and application conversion; it is not drop-in engine compatibility. Original stem/options preserved, and answer D remains best among provided choices.


### Q239 — Domain 4, position 46/139 (2026-10-29)

- **Correct answer: B** (single answer). Aurora MySQL + EC2 Auto Scaling behind ALB + ElastiCache for Redis OSS replication group.
- **AWS sources:** [Aurora HA](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraHighAvailability.html), [Redis Multi-AZ failover](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoFailover.html), [Redis replication groups](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Scaling.RedisReplGrps.html).
- **External exact matches:** [FreeCram](https://www.freecram.net/question/Amazon.AWS-Solutions-Architect-Professional.v2024-07-06.q214/an-online-retail-company-hosts-its-stateful-web-based-application-and-mysql-database-in-an-on-premises) and [DumpsTech](https://www.dumpstech.com/free-amazon-web-services/sap-c02-practice-9.html) identify B; [Actual4Exams](https://latestdumps.actual4exams.com/articles/free-sap-c02-pdf-files-with-updated-and-accurate-dumps-training-q188-q213/) shuffles choices and labels same architecture C. No Choose TWO/THREE source variant identified; some PDF text copies split one compound option into multiple pseudo-options, a transcription artifact.
- **All options:** A Neptune is a graph database not a web-session store; B Aurora MySQL + ALB/ASG + Redis replicated session store is best; C DocumentDB is not MySQL relational and Firehose not a session store; D Memcached lacks native replication/auto failover.
- **Important caveat:** Aurora's six-way replicated storage does not by itself guarantee instant DB instance failover. Deploy Aurora reader(s) in separate AZs and enable Redis Multi-AZ automatic failover for highest real-world availability. Option B does not expressly require these settings, so flag the omission rather than claim full HA is guaranteed. Original question/options unchanged.


### Q240 — Domain 4, position 47/139 (2026-10-29)

- **Correct answer: B** (single answer). Deploy SageMaker-trained model and inference component on existing local Linux server using AWS IoT Greengrass V2. Offline inference calls local API.
- **AWS sources:** [Greengrass local ML inference](https://docs.aws.amazon.com/greengrass/v2/developerguide/perform-machine-learning-inference.html), [ML components](https://docs.aws.amazon.com/greengrass/v2/developerguide/machine-learning-components.html), [Monitron availability announcement](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron/).
- **External exact matches B:** [ExamsVCE](https://www.examsvce.com/sap-c02/a-manufacturing-company-is-building-an-inspection-95912-question-answer.html), [FreeCram](https://www.freecram.net/question/Amazon.SAP-C02.v2024-05-06.q201/a-manufacturing-company-is-building-an-inspection-solution-for-its-factory-the-company-has-ip-cameras).
- **Conflicting external answer key:** [Scribd practice collection](https://www.scribd.com/document/921182718/SAP-C02-CSL-09-26-341) reproduces same four-choice question but incorrectly lists D; AWS documentation proves Greengrass B, while Monitron cannot host arbitrary image-inference models. This is an answer-key conflict, **not** a Choose TWO/THREE variant. No multi-answer variant found in searched sources.
- **Options:** A cloud-only Kinesis/SageMaker/Lambda fails offline; B Greengrass local model inference and local API works offline; C Snowball option assumes unsupported conventional SageMaker hosted endpoint and unnecessary hardware; D Monitron condition monitoring is not camera-image inference.
- **Defects:** 'IPcameras' typo; option C missing preposition; Monitron closed to new customers effective October 31, 2024. Model and dependencies must be pre-deployed locally; no assumption of online model downloads during outage. Original question/options preserved.


### Q242 — Domain 4, position 48/139 (2026-10-29)

- **Best intended answer: C** (single answer): AWS Backup cross-Region backup copies for Aurora/DynamoDB; Route 53 failover to secondary Regional API Gateway; use existing CloudFormation and CodePipeline to restore ECS/application and database during DR.
- **AWS documentation:** [DR strategy RPO/RTO cost table](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-database-disaster-recovery/defining.html); [AWS DR backup-and-restore and IaC](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html); [AWS Backup resource cross-Region support](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-feature-availability.html).
- **Exact single-answer external sources:** [FreeCram](https://www.freecram.net/question/Amazon.SAP-C02.v2023-12-13.q142/a-company-implements-a-containerized-application-by-using-amazon-elastic-container-service-amazon-ecs) (C); [ExamTopics](https://www.examtopics.com/discussions/amazon/view/112793-exam-aws-certified-solutions-architect-professional-sap-c02-topic-1-question-296-discussion/); [ExamsReviews](https://www.examsreviews.com/articles/best-preparations-of-sap-c02-exam-2025-aws-certified-solutions-architect-unlimited-510-questions-q190-q208/) (options reordered). No Choose TWO/THREE variant found in checked sources.
- **Options:** A Global DB/table replication costs more and CloudFront origin failover is unsuitable as general API write failover; B custom DMS/Streams/EventBridge/Lambda replication is complex; C least-cost backup and restore, contingent on tested recovery; D global Aurora and DynamoDB replication meets tighter DR but higher cost.
- **Critical defect:** The requirement is **RPO 2h, RTO 4h**, yet AWS describes backup-and-restore full-stack RTO as potentially up to 24h. C is the intended cost-effective exam answer **but does not guarantee four-hour recovery** without backup/copy freshness, data-size and restore-time evidence, and rehearsed CloudFormation/CodePipeline deployment. Route 53 DNS failover cannot restore ECS and DB resources on its own. Flag as conditional rather than unambiguously valid.
- **Other defects:** Missing punctuation and spacing, malformed trailing apostrophe; original stem and choices retained.


### Q244 — Domain 4, position 49/139 (2026-10-29)

- **Correct answer: B** (single-answer). Create Site-to-Site VPN for prompt private connectivity, AWS DMS MySQL source to Aurora target, and select **full load plus CDC** to move 2 TB initial data while capturing hundreds of updates/minute.
- **AWS docs:** [DMS ongoing replication / CDC](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Task.CDC.html), [MySQL CDC binlog prerequisites](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html), [DMS CDC latency caveats](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_BestPractices.html).
- **External source:** [Scribd SAP-C02 Updated Questions](https://www.scribd.com/document/946282982/SAP-C02-Updated-Questions-AWS-Certified-Solutions-Architect-Professional) question 37 reproduces the exact stem with four single-answer choices. No explicit Choose TWO/THREE variant identified in targeted searches; source copies are not official AWS exam records.
- **Options:** A VPN+dump alone misses changes during load; B VPN+DMS full load+CDC meets quick start and short cutover; C new Direct Connect delays start and manual dump adds complexity; D DMS correct but new Direct Connect delays start.
- **Defects:** 'Aurora duster' OCR errors; option D missing punctuation; 'DMS task with ongoing replication' is insufficiently precise for an empty Aurora target (must configure full load plus CDC). 'No data lost' is not an automatic guarantee: configure row-based binlogs, retain logs, monitor lag and validation, briefly pause writes and cut over only when caught up. Preserve original question/options.


### Q258 — Domain 4, position 50/139 (2026-10-29)

- **Source key: C; technical audit: DEFECTIVE / AMBIGUOUS.** C: DocumentDB provisioned instances with primary and replicas in multiple AZs + Java EC2 Auto Scaling across AZs. D: DocumentDB 'on-demand capacity mode' in multiple AZs + Java EC2 ASG across AZs is ALSO plausible in current AWS; on-demand pricing for provisioned DocumentDB and DocumentDB Serverless on-demand auto-scaling both exist.
- **AWS docs:** [DocumentDB production HA practices](https://docs.aws.amazon.com/documentdb/latest/devguide/best_practices.html), [replication and failover](https://docs.aws.amazon.com/documentdb/latest/devguide/replication.html), [DocumentDB Serverless](https://docs.aws.amazon.com/documentdb/latest/devguide/docdb-serverless.html), [DocumentDB on-demand instances](https://docs.aws.amazon.com/documentdb/latest/devguide/limits.html), [MongoDB compatibility caveats](https://docs.aws.amazon.com/documentdb/latest/devguide/compatibility.html).
- **External single-answer variants:** [FreeCram](https://www.freecram.net/question/Amazon.SAP-C02.v2024-05-06.q201/a-company-has-an-on-premises-website-application-that-provides-real-estate-information-for-potential) and [Exam-Tests](https://www.exam-tests.com/SAP-C02-exam/Amazon.SAP-C02.v2025-02-24.q513.html?p=46) key original C, but incorrectly justify by saying 'on-demand capacity mode is DynamoDB only'. [JPNTest](https://www.jpntest.com/blog/2025%E5%B9%B4%E6%9C%80%E6%96%B0%E3%81%AE%E5%AE%9F%E9%9A%9B%E3%81%AB%E5%87%BA%E3%82%8B%E3%81%A8%E7%A2%BA%E8%AA%8D%E3%81%95%E3%82%8C%E3%81%9F-%E7%84%A1%E6%96%99amazon-aws-solutions-architect-professional%E8%A9%A6%E9%A8%93%E5%95%8F%E9%A1%8C-q220-q242/) reorders choices and keys B, which corresponds to original **D**. This is an answer-key conflict, not a multi-select variant. No Choose TWO/THREE exact-stem variant found in checked sources.
- **Option analysis:** A Aurora relational requires application changes; B single-AZ app fails HA; C DocumentDB provisioned replicas + Multi-AZ ASG is intended; D on-demand DocumentDB across AZs also can meet HA, so unique answer is not technically justified.
- **Defects:** 'DocumentD3' OCR typo, 'NOSQL', missing punctuation, and material answer ambiguity. DocumentDB MongoDB compatibility is not 100% feature compatibility: test application/driver usage before claiming no changes required. **Keep original C for source fidelity, mark defective, do not present as unequivocally verified.**


### Q264 — Domain 4, position 51/139 (2026-10-29)

- **Correct answer A (single answer):** Deploy AWS Application Discovery Agent to each on-premises VM. It collects CPU/RAM/disk performance, running-process inventory, and TCP connections needed for EC2 sizing and dependency mapping.
- **AWS primary sources:** [Discovery Agent and collected data](https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-agent.html), [agent versus agentless comparison](https://docs.aws.amazon.com/application-discovery/latest/userguide/what-is-appdiscovery.html), [Nov 8 2024 agentless network connections announcement](https://aws.amazon.com/about-aws/whats-new/2024/11/network-connections-aws-application-discovery-service-agentless-collector/).
- **External exact-stem single-answer sources:** [CertEnsure](https://www.certensure.com/amazon-web-services/sap-c02-cert-practice-test.html) and [Pupuweb](https://pupuweb.com/aws-certified-solutions-architect-professional-sap-c02-actual-exam-question-answer-dumps-5/5/) key A. [Older SOP-C01 answer PDF](https://itpracticetest.online/wp-content/uploads/AWS-Certified-Solutions-Architect-Professional-SOP-C01-Exam-2-Answers.pdf) keys B incorrectly for identical stem/options. This is a conflicting answer key, NOT a multi-select variant. No explicit Choose TWO/THREE variant found in checked sources.
- **Option analysis:** A covers all requested data; B CloudWatch agent metrics/logs lacks complete process/network dependency inventory and CloudWatch Logs is not the normal metrics destination; C agentless gathers utilization and now network connections but not running processes; D console+VPN does not perform discovery without agents/collector.
- **Defects/outdated claims:** Source punctuation 'CPU. memory', 'visualization environment' typo. AWS introduced network-connection discovery in Agentless Collector in November 2024; any older explanation denying ALL agentless network visibility is obsolete. **Running-process inventory remains exclusive to Discovery Agent among these choices.** Cost-efficiency claim is qualitative rather than a measured TCO; original question and options preserved.


### Q266 — Domain 4, position 52/139 (2026-10-29)

- **AWS-verified answer: B (CORRECTED from original source key D).** Import existing on-prem physical and VMware inventory CSV into Migration Hub using supported schema; generate EC2 instance recommendations from CPU/RAM utilization, target Region and pricing model; download ZIP containing EC2InstanceRecommendations CSV with instance types and costs.
- **AWS primary references:** [Migration Hub import supported CSV](https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-import.html); [recommendation prerequisites](https://docs.aws.amazon.com/migrationhub/latest/ug/ec2-recommendation-prerequisites.html); [generate and export EC2 recommendations](https://docs.aws.amazon.com/migrationhub/latest/ug/generating-ec2-recommendations.html); [CSV output and cost fields](https://docs.aws.amazon.com/migrationhub/latest/ug/understanding-ec2-recommendations.html); [Migration Evaluator onboarding](https://aws.amazon.com/migration-evaluator/getting-started/).
- **External source-key conflict:** [Certstopics](https://www.certstopics.com/questions/aws-certified-professional-sap-c02-release-date.html) keys original D; [FreeCram](https://www.freecram.net/question/Amazon.SAP-C02.v2026-03-31.q264/a-company-is-planning-to-migrate-workloads-from-its-on-premises-data-center-to-amazon-ec2-instances) shuffles options and keys A, also original D; [Scribd](https://www.scribd.com/document/946282982/SAP-C02-Updated-Questions-AWS-Certified-Solutions-Architect-Professional) reproduces stem. No Choose TWO/THREE exact-stem variant found in checked sources.
- **Option analysis:** A Compute Optimizer does not directly import arbitrary on-prem inventory CSV; B Migration Hub CSV import+EC2 recommendations+CSV export is explicitly documented; C Agentless Collector is a VMware discovery appliance, not a generic CSV importer and cannot directly ingest physical server CSV; D Migration Evaluator accepts existing inventory and produces Quick Insights plus detailed exports, but the precise automatic S3 bucket import -> Quick Insights -> S3 CSV export described is not documented.
- **Defect:** Source key D is poorly supported and overlooks fully documented B. Original onprem.csv schema unspecified; Migration Hub requires supported CSV fields, possibly mapping/reformatting. **Answer changed D to B; original stem/options retained.**


### Q272 — Domain 4, position 53/139 (2026-10-29)

- **Answer B retained, with caveats.** The original stem/options are preserved. Q268 is Select TWO and was skipped. Exact-stem variants checked were single-answer; no Choose TWO/THREE conflict found.
- **A:** EC2-hosted PostgreSQL without explicit multi-AZ/replication remains a single point of failure; WorkSpaces per end user adds desktop management and cost. **B:** Aurora PostgreSQL plus EC2 Auto Scaling/ALB retains existing VM-style application tiers while AppStream 2.0 can stream the desktop application for a more responsive remote experience. **C:** RDS PostgreSQL Multi-AZ is a valid HA alternative, but ECS/Fargate containerization is a larger change and ElastiCache does not directly fix desktop network latency. **D:** Redshift is a data warehouse, unsuitable as a transparent OLTP PostgreSQL replacement; CloudFront is not a general desktop-protocol acceleration service.
- **High-availability qualification:** B as written omits explicit Aurora failover replica in another AZ, Multi-AZ ASG placement, client compatibility testing, and quantified cost/99.95% SLA evidence. Provision these and validate the end-to-end SLA. Aurora without a standby reader can have downtime while its writer instance recovers.
- **AWS docs:** [Aurora availability](https://docs.aws.amazon.com/rds/latest/auroraextendedcontent/aurora-features-availability.html); [Aurora failover specifics](https://docs.aws.amazon.com/rds/latest/auroraextendedcontent/aurora-faq-availability-and-durability.html); [Aurora replication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Replication.html); [RDS PostgreSQL Multi-AZ](https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-multitenant-managed-postgresql/availability.html).
- **External exact-stem variants:** [FreeCram Q352](https://www.freecram.com/discussions/Amazon/exam-aws-solutions-architect-professional-topic-1-question-352-discussion-p1349665.html); [Actual4Exams Q124](https://latestdumps.actual4exams.com/articles/sap-c02-questions-pass-on-your-first-attempt-dumps-for-aws-certified-solutions-architect-certified-q116-q135/) reorders original B into D. [SOP-C01 answer PDF Q32](https://itpracticetest.online/wp-content/uploads/AWS-Certified-Solutions-Architect-Professional-SOP-C01-Exam-4-Answers.pdf) instead checks original **D (Redshift)**; this is a technically defective legacy key and is **not** a multi-answer variant.
- **Review classification:** Intended B, reviewed with caveats; do not assert an unqualified 99.95% uptime or lowest total cost from the stated options.


### Q278 — Domain 4, position 54/139 (2026-10-29)

- **Best original answer C (single).** Q276 Choose THREE skipped. Preserve original question and options, including OCR typos.
- **A:** CloudFront caching and DynamoDB global tables help but no explicit two-origin CloudFront failover. **B:** S3 same-Region replication fails regional resiliency; DMS CDC unnecessary. **C:** S3 cross-Region replication, CloudFront origin failover and DynamoDB global tables are the most complete combination. **D:** both S3 origins remain in the same Region.
- **AWS docs:** https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_HowItWorks.html ; https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/high_availability_origin_failover.html ; https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html
- **Exact-stem external:** https://www.freepdfdumps.com/Amazon.SAP-C02.v2025-06-02.q210.html?p=29 keys original C; https://www.scribd.com/document/921182718/SAP-C02-CSL-09-26-341 keys C. https://www.freecram.net/question/Amazon.SAP-C02.v2023-03-07.q318/a-company-is-creating-a-sequel-for-a-popular-online-game-a-large-number-of-users-from-all-over-the-world reorders choices and marks C, mapping to original B, an unreliable source key. No verified Choose TWO/THREE exact-stem variant.
- **Caveats:** MREC global tables enable Streams automatically, and MRSC replication does not use Streams; explicit manual enablement wording is dated. CloudFront failover does not apply to all HTTP methods; CRR is asynchronous and regional routing for DynamoDB clients is separate.


### Q281 — Domain 4, position 55/139 (2026-10-29)

- **AWS-verified B:** FSx for Lustre mounted via Lustre client, with S3 data repository association and automatic import/export policies. Original stem/options preserved.
- **A:** DataSync is a transfer task, not a POSIX mounted file system. **B:** native POSIX and S3 automatic import/export. **C:** EFS cannot use FSx-for-Lustre S3 data repository association policies. **D:** S3 File Gateway requires RefreshCache for directly modified S3 objects and lacks the specified managed policy model.
- **AWS primary sources:** https://docs.aws.amazon.com/fsx/latest/LustreGuide/autoimport-data-repo-dra.html ; https://docs.aws.amazon.com/fsx/latest/LustreGuide/autoexport-data-repo-dra.html ; https://docs.aws.amazon.com/fsx/latest/LustreGuide/create-linked-dra.html ; https://docs.aws.amazon.com/filegateway/latest/files3/troubleshooting-file-share-issues.html
- **Caveats:** automatic import requires same Region; export is asynchronous; file content loaded on demand; concurrent writes on S3 and Lustre can conflict; older FSx versions have export limitations.
- **External source verification:** No exact-stem independent external exam copy or Choose TWO/THREE variant confirmed by this limited search. This is a verification gap, not proof that variants do not exist.


### Q286 — Domain 4, position 56/139 (2026-10-29)

- **Answer B confirmed.** ECS Fargate + EFS shared file system; configure EFS Elastic Throughput for unpredictable demand and General Purpose for latency-sensitive access. Original stem/options unchanged.
- **A:** S3 object store requires application changes to replace shared filesystem. **B:** Fargate removes host administration; EFS concurrently mounts across tasks. **C:** Fargate now supports EBS, but ECS task EBS volumes are not a shared cross-task file system. **D:** EC2 + Docker requires host administration.
- **AWS:** https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_data_volumes.html ; https://docs.aws.amazon.com/efs/latest/ug/managing-throughput.html ; https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-volumes.html ; https://docs.aws.amazon.com/us_eg/AmazonECS/latest/bestpracticesguide/storage.html
- **External exact stem:** https://www.freecram.net/question/Amazon.SAP-C02.v2025-07-25.q355/a-company-is-planning-to-migrate-its-on-premises-transaction-processing-application-to-aws-the-applicatio marks **A** because its options are reordered; this is **original B**. No confirmed Choose TWO/THREE exact-stem variant in checked sources.
- **Defects/caveats:** original 'VMS' typo; EFS Elastic Throughput not explicitly selected in choice B; 'low latency' is unquantified and EFS is not guaranteed sub-millisecond latency. Preserve original question and answer.


### Q290 — Domain 4, position 57/139 (2026-10-29)

- **Verified original answer C:** S3 for static videos and CloudFront CDN for video delivery, offloading EC2/ALB/EFS. Original stem/options preserved.
- **A:** EFS Maximum I/O alone is not video CDN and is legacy terminology. **B:** instance store ephemeral and unsuited to shared persistent ASG content. **C:** S3 scalable media storage with CloudFront caching. **D:** CloudFront ALB origin supported but retains EC2/EFS load for cache misses, making it less efficient than separating videos.
- **AWS:** https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorS3Origin.html ; https://repost.aws/knowledge-center/cloudfront-serve-static-website ; https://docs.aws.amazon.com/id_id/whitepapers/latest/amazon-cloudfront-media/cloudfront-configuration-best-practices.html
- **External exact stem:** https://www.freecram.net/question/Amazon.SAP-C02.v2026-07-08.q291/a-company-used-amazon-ec2-instances-to-deploy-a-web-fleet-to-host-a-blog-site-the-ec2-instances-are-behind ; https://certempire.com/demo-files/aws-sap-c02-demo-file.pdf ; https://examguru.io/exams/sap-c02/review — all key C. No conflicting Choose TWO/THREE in checked copies.
- **Source defects:** OCR typos 'Auto ScaSng', 'Moggers', 'Nog', 'win'; EFS Maximum I/O dated terminology. Preserve original question while recording corrections.


### Q291 — Domain 4, position 58/139 (2026-10-29)

- **Best original answer B, CONDITIONAL/AMBIGUOUS.** SES SMTP requires TLS and SES SMTP credentials; B provides STARTTLS plus SMTP credentials, but the stem only says legacy SMTP *server* cannot do TLS. If the application cannot do STARTTLS, no offered choice is complete; a TLS-capable relay/proxy is needed. Preserve original stem/options.
- **A:** TLS Wrapper valid on 465/2465, but EC2 IAM role cannot replace SMTP credentials. **B:** STARTTLS on 25/587/2587 with SES SMTP credentials, valid if client supports it. **C/D:** SES API/SDK not usable by SMTP-only application.
- **AWS:** https://docs.aws.amazon.com/ses/latest/dg/smtp-connect.html ; https://docs.aws.amazon.com/ses/latest/dg/smtp-credentials.html ; https://docs.aws.amazon.com/ses/latest/dg/troubleshoot-smtp.html
- **External exact-stem:** https://pupuweb.com/aws-certified-solutions-architect-professional-sap-c02-actual-exam-question-answer-dumps-1/9/ marks A (defective: IAM role alone lacks SMTP auth); https://quizlet.com/814619921/aws-sa-professional-testing-flash-cards/ marks B; https://cciedump.spoto.net/exam-questions/free-aws-sap-c02-practice-questions-answers-2026-part4 has matching single-answer version. No confirmed Choose TWO/THREE exact-stem variant in checked results.
- **Other caveat:** lifting SES sending limits is not necessarily removal of EC2 port 25 throttling; prefer 587 when possible.


### Q292 — Domain 4, position 59/139 (2026-10-29)

- **Verified A:** EC2 AMI + Auto Scaling/ALB for existing web VMs, Amazon MQ for RabbitMQ to preserve AMQP broker behavior, EKS for managed Kubernetes backend. Preserve original stem/options.
- **A:** lowest changes and managed services. **B:** Lambda/API Gateway custom runtime changes front-end architecture. **C:** self-managed Kubernetes EC2 increases control-plane burden. **D:** SQS not drop-in RabbitMQ/AMQP replacement; app integration changes.
- **AWS:** https://aws.amazon.com/amazon-mq/faqs/ ; https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html ; https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html
- **External exact stem:** https://www.certsmania.com/pdf/practice-session-solution-download-full-version-sap-c02-exam-by-enrique.pdf (A); https://www.examcollection.us/exam/SAP-C02-question-answer-5.html ; https://www.brainscape.com/flashcards/solutions-architect-professional-deck-04-15140182/packs/21889491 (A). Checked variants single answer, no conflicting Choose TWO/THREE identified.
- **Defects:** Missing punctuation around 'VMs RabbitMQ'; creating AMI directly from on-premises VM is shorthand for migration/import; EKS workers still need compute configuration.


### Q293 — Domain 4, position 60/139 (2026-10-29)

- **TECHNICALLY DEFECTIVE; source key A retained as closest, NOT compliant with strict RPO=0.** Aurora cross-Region replicas and Global Database replicate asynchronously, so an unplanned Regional failover can lose committed transactions. Planned Aurora Global Database switchover can achieve zero RPO but does not solve an unexpected Region failure. Preserve original question/options.
- **A:** lowest-overhead cross-Region DR but asynchronous; potential data loss. **B:** DataSync does not replicate Aurora transaction logs. **C:** DMS CDC asynchronous, more overhead, still potential loss. **D:** DLM EBS snapshot/AMI policy does not implement Aurora zero-loss recovery.
- **AWS authoritative:** https://docs.aws.amazon.com/prescriptive-guidance/latest/aurora-replication-options/compare-solutions.html ; https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.html ; https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html
- **External exact stem:** https://www.freecram.net/question/Amazon.SAP-C02.v2026-03-31.q264/a-company-is-running-an-application-in-the-aws-cloud-the-application-runs-on-containers-in-an-amazon (A; incorrect assertion zero loss); https://www.freecram.net/question/Amazon.SAP-C02.v2025-07-25.q355/a-company-is-running-an-application-in-the-aws-cloud-the-application-runs-on-containers-in-an-amazon (A); https://braindumps2go.dumpsmaterials.com/articles/new-sap-c02-dumps-for-preparing-aws-certified-solutions-architect-certified-amazon-exam-well-q56-q76/ reorders Aurora option to B. All checked copies single-answer; no conflicting Choose TWO/THREE variant found.
- **Recommendation:** Rewrite requirement to 'minimize data loss' or add a solution with explicit synchronous cross-Region write-acknowledgment and failure handling; do not claim an Aurora replica alone guarantees RPO=0.


### Q298 — Domain 4, position 61/139 (2026-10-30)

- **Verified B:** migrate simple MySQL user-profile records to DynamoDB with DMS; store 4 GB videos in S3 and keep object key in DynamoDB. Preserve original stem/options and answer B.
- **A:** base64 multi-GB video in Aurora PostgreSQL TEXT incurs major DB overhead and does not isolate media traffic. **B:** AWS-documented DynamoDB + S3 large-object pattern; DynamoDB 400 KB item limit. **C:** Amazon Keyspaces is not an AWS DMS supported target endpoint, and Cassandra migration is unnecessary. **D:** DynamoDB 400 KB item limit makes 4 GB video storage impossible.
- **AWS:** https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-use-s3-too.html ; https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DynamoDB.html ; https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.Targets.html ; https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpu-upload-object.html
- **External exact stem:** https://nerdexam.com/exams/sap-c02/questions/715 keys original B; https://cciedump.spoto.net/exam-questions/free-aws-sap-c02-practice-questions-answers-2026-part4 keys reordered C = original B. No substantive answer conflict and no confirmed Choose TWO/THREE exact-stem variant in checked results.
- **Caveats:** AWS SCT not strictly required for DMS relational-to-DynamoDB object mapping; use multipart upload (and optionally direct client S3 transfer) for 4 GB videos; S3/DynamoDB operations are not atomic, so handle orphaned objects or missing metadata.


### Q300 — Domain 4, position 62/139 (2026-10-30)

- **Verified B:** AWS DataSync on-premises agent with NFS source and separate tasks for S3, EFS and FSx for Windows File Server; initial and incremental copies, encrypted transit and checksum verification. Original stem/options preserved.
- **A:** AWS Application Migration Service/legacy CloudEndure migrates servers, not NFS-to-storage multi-target files. **B:** matches all requirements. **C:** aws s3 sync only S3 and no managed multi-target workflow. **D:** FTP not NFS-to-S3/EFS/FSx migration; plain FTP not encrypted.
- **AWS:** https://aws.amazon.com/datasync/faqs/ ; https://docs.aws.amazon.com/datasync/latest/userguide/create-nfs-location.html ; https://docs.aws.amazon.com/datasync/latest/userguide/configure-data-verification-options.html ; https://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html
- **External exact stem:** https://www.certensure.com/amazon-web-services/sap-c02-cert-practice-test.html ; https://www.dumpspedia.com/sap-c02-aws-certified-solutions-architect-professional-dumps.html ; https://pupuweb.com/aws-certified-solutions-architect-professional-sap-c02-actual-exam-question-answer-dumps-4/4/ ; https://www.scribd.com/document/818710370/AWS-SAP-Questions-and-Answers . Older variants name CloudEndure instead of AWS Application Migration Service in A, while still keying B. No confirmed conflicting Choose TWO/THREE version.
- **Caveats:** configure separate tasks per destination; FSx Windows File Server is Basic-mode-only; use verification settings and plan final incremental cutover.


### Q301 — Domain 4, position 63/139 (2026-10-30)

- **Verified intended answer D:** two physically diverse Direct Connect connections, each transit VIF to one Direct Connect gateway, both Regional TGWs associated with DX gateway, and TGW peering for inter-Region VPC-to-VPC traffic. Preserve original stem/options.
- **A:** private VIF incompatible with TGW DX gateway association. **B:** DX gateways cannot peer; splits path redundancy. **C:** DX gateway cannot route between associated TGWs. **D:** transit VIF + shared DX gateway for hybrid connectivity, TGW peering for inter-Region traffic.
- **AWS:** https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-transit-gateways.html ; https://docs.aws.amazon.com/directconnect/latest/UserGuide/WorkingWithVirtualInterfaces.html ; https://aws.amazon.com/blogs/networking-and-content-delivery/hybrid-cloud-architectures-using-aws-direct-connect-gateway/ ; https://docs.aws.amazon.com/vpc/latest/tgw/tgw-peering.html
- **External exact stem:** https://www.examsvce.com/sap-c02/a-retail-company-has-an-onpremises-data-question-answer.html and https://www.dumps-files.com/downloadfile.html?id=8451 key D. https://www.scribd.com/document/921182718/SAP-C02-CSL-09-26-341 displays incorrect A despite community preference D. No confirmed Choose TWO/THREE exact-stem variant.
- **Caveat:** absolute 'no single points of failure' not fully demonstrated by a single DX gateway and one TGW per Region; option D is best among choices. Configure TGW peering attachment routing, BGP ASNs, allowed prefixes, nonoverlapping VPC CIDRs, and VPC route tables.


### Q306 — Domain 4, position 64/139 (2026-10-30)

- **Verified intended C:** Transfer Family SFTP→S3, event-driven AWS Glue transformation, and completion message to SQS. Preserve dataset's original stem/options, which are abbreviated relative to independently found full-length exam copies.
- **A:** EFS cannot run cron by itself; needs managed compute, SNS not a queue. **B:** EMR operational overhead and SNS not queue. **C:** managed SFTP, object storage, transformation, queue. **D:** scheduled Glue omits post-transformation SQS message and uses EFS rather than event-driven S3.
- **AWS:** https://aws.amazon.com/aws-transfer-family/faqs/ ; https://docs.aws.amazon.com/transfer/latest/userguide/eventbridge.html ; https://docs.aws.amazon.com/glue/latest/dg/about-triggers.html ; https://docs.aws.amazon.com/glue/latest/dg/automating-awsglue-with-cloudwatch-events.html
- **External source:** https://www.certensure.com/amazon-web-services/sap-c02-cert-practice-test.html Q61 full-length keys C; https://www.scribd.com/document/946282982/SAP-C02-Updated-Questions-AWS-Certified-Solutions-Architect-Professional abbreviated variant also C. No confirmed Choose TWO/THREE version.
- **Defects:** dataset question abbreviated: loses explicit queue, 'LEAST operational overhead', full option implementations. S3 event notifications do not invoke Glue jobs directly: use EventBridge/Glue event triggers, Lambda or other orchestration. Transfer Family completed-upload EventBridge event is more precise than generic S3 object-created event when avoiding partial uploads.


### Q308 — Domain 4, position 65/139 (2026-10-30)

- **Verified A (retained):** Two redundant Direct Connect connections, each with a private VIF to a common Direct Connect gateway, plus a VPC-attached virtual private gateway association. Future Regions can associate their own VGWs to the same DX gateway.
- **A:** Correct architecture. Corrected 'interlace' to 'interface' and 'victual' to 'virtual'. 'Connect DX gateway to VPC' means associate with VGW attached to that VPC.
- **B:** Two same-Region direct private VIFs can give VPC redundancy but cannot meet cross-Region expansion as described.
- **C:** Public VIF exposes AWS public services, not a direct private VPC attachment.
- **D:** A private VIF does not connect directly to Transit Gateway; correct TGW implementation needs a transit VIF, Direct Connect gateway, and TGW association.
- **AWS:** https://docs.aws.amazon.com/directconnect/latest/UserGuide/virtualgateways.html ; https://docs.aws.amazon.com/directconnect/latest/UserGuide/WorkingWithVirtualInterfaces.html ; https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-transit-gateways.html ; https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreatePrivateVirtualInterface.html
- **External exact-stem sources:** https://examguru.io/exams/sap-c02/review ; https://www.secexams.com/exams/Amazon/aws-certified-solutions-architect-professional-sap-c02/view/2 ; https://passitexams.com/articles/quizzes/sap-c02-question-7/. All single-answer, A selected/supported; no confirmed Choose TWO/THREE conflicting variant.
- **Caveats:** Provision links on diverse devices/paths and configure/test BGP failover; deleting an existing VIF can interrupt production connectivity. AWS docs, not third-party answer keys, establish technical correctness.


### Q320 — Domain 4, position 66/139 (2026-10-31)

- **Verified C (original key retained):** AWS DataSync on-premises → FSx for NetApp ONTAP → EKS shared volume → DataSync → S3. FSx ONTAP offers NFS/SMB multiprotocol access.
- **A:** EFS is NFS-based, not SMB/NFS multiprotocol; Transfer Family is not direct EFS-to-S3 copy.
- **B:** FSx Lustre is high-performance POSIX storage, not multiprotocol SMB/NFS.
- **C:** Correct; DataSync supports ONTAP as source/destination and S3 as destination.
- **D:** ONTAP correct, but Transfer Family SFTP is not the intended ONTAP-to-S3 transfer mechanism.
- **Official AWS:** https://docs.aws.amazon.com/datasync/latest/userguide/create-ontap-location.html ; https://aws.amazon.com/datasync/faqs/ ; https://aws.amazon.com/fsx/netapp-ontap/features/ ; https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/supported-fsx-clients.html
- **External exact stem:** https://www.p2pexams.com/free-questions/amazon-sap-c02-dumps-by-pearson.pdf Question 11, keys C. No confirmed Choose TWO/THREE variant.
- **Defects/caveats:** Scheduling/event triggering, gating complete output, EKS volume mounting omitted. DataSync ONTAP NFS location supports NFSv3 (not NFSv4), although ONTAP itself supports newer NFS. No answer correction needed.


### Q324 — Domain 4, position 67/139 (2026-10-31)

- **Skip Q321:** explicitly Select THREE, A/D/F.
- **Verified B (retained):** AWS MGN automated VMware rehosting + AWS DataSync on-prem NFS → EFS via existing 10 Gbps Direct Connect.
- **A:** Manual VM export/import and Snowball shipping add elapsed time and operational work.
- **B:** Correct, separates block-level VM migration and file-level NFS transfer.
- **C:** Rebuilding 120 custom VMs is slower; Lustre is not the best general-purpose NFS destination.
- **D:** Offline shipping, import, and staged S3-to-EFS transfer add unnecessary steps.
- **AWS:** https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html ; https://docs.aws.amazon.com/prescriptive-guidance/latest/configuring-storage-offload-vmware-cloud-aws/data-migration.html ; https://aws.amazon.com/datasync/faqs/ ; https://docs.aws.amazon.com/pdfs/mgn/latest/ug/user-guide.pdf
- **External exact stem:** https://www.certensure.com/amazon-web-services/sap-c02-cert-practice-test.html ; https://www.examtopics.com/discussions/amazon/view/124802-exam-aws-certified-solutions-architect-professional-sap-c02-topic-1-question-302-discussion/; single-answer B, no confirmed Choose TWO/THREE variant.
- **Defects:** Original text contains 'VMS', 'AMIS', '10 GbpsAWS', 'isloaded', spacing errors. MGN 'connection/replication job' is loose wording; MGN has agent-based or VMware vCenter agentless workflows. OS support and agentless prerequisites must be checked; MGN does not copy NFS NAS shares, so DataSync is needed. Original options retained verbatim.


### Q327 — Domain 4, position 68/139 (2026-10-31)

- **Skip Q326:** Select THREE C/D/E.
- **Verified A (retained):** App2Container supports containerizing Java-on-Linux apps and deploying to ECS Fargate, reducing code changes and eliminating host administration; ECR + ECS task execution role + ALB complete the solution.
- **A:** Correct, conditional on App2Container-supported Java OS/framework/dependencies.
- **B:** Lambda container image still requires Lambda-compatible execution model and code integration.
- **C:** EKS managed EC2 nodes need more management than ECS Fargate; API Gateway unnecessary.
- **D:** ALB-to-Lambda supported, but Lambda still requires adaptation and runtime constraints.
- **AWS:** https://docs.aws.amazon.com/app2container/ ; https://docs.aws.amazon.com/app2container/latest/UserGuide/a2c-integrations-ecs.html ; https://docs.aws.amazon.com/app2container/latest/UserGuide/config-deployment.html ; https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html
- **External exact stem:** https://www.exam-tests.com/SAP-C02-exam/Amazon.SAP-C02.v2025-02-24.q513.html?p=67 ; https://www.freecram.com/discussions/Amazon/exam-sap-c02-topic-4-question-484-discussion-p1143155.html; single-answer A; no confirmed Choose TWO/THREE conflicting variant.
- **Defects:** 'stable. but' and 'permission 10' are transcription errors. Missing source Java framework/OS details preclude guaranteeing App2Container support. Original options preserved verbatim.


### Q334 — Domain 4, position 69/139 (2026-10-31)

- **Verified intended D (retained):** EKS on Fargate behind ALB, RDS PostgreSQL read replicas, managed Kafka via MSK, static S3 via CloudFront.
- **A:** EC2 maintenance; Kafka-to-Kinesis migration; direct S3 delivery.
- **B:** EC2 and Kinesis drawbacks; Multi-AZ and storage autoscaling are HA/capacity, not read scaling.
- **C:** Self-managed Kubernetes on EC2 increases overhead; Multi-AZ not substitute for read replicas.
- **D:** Best combination for reduced ops and scaling, assuming read traffic is a bottleneck.
- **Official AWS:** https://docs.aws.amazon.com/eks/latest/userguide/fargate.html ; https://docs.aws.amazon.com/msk/latest/developerguide/what-is-msk.html ; https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PostgreSQL.Replication.ReadReplicas.html ; https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html
- **External exact stem:** https://blog.surepassexams.com/2026/10/26/online-sap-c02-test-brain-dump-question-and-test-engine-q89-q105/ ; https://www.certstopics.com/questions/aws-certified-professional-sap-c02-syllabus-exam-questions-answers.html ; https://pupuweb.com/aws-certified-solutions-architect-professional-sap-c02-actual-exam-question-answer-dumps-2/5/; option ordering varies, correct text is EKS Fargate+MSK+RDS read replicas+CloudFront. No confirmed Choose TWO/THREE variant.
- **Defects/caveats:** Option B typo 'theDB'; 'increased orders' does not establish read-heavy DB load. Read replicas do not scale writes. Fargate ALB requires IP targets, HPA/Fargate profiles, MSK networking, and explicit application read routing. Retain D with caveat.


### Q341 — Domain 4, position 70/139 (2026-10-31)

- **Skipped Q337:** explicit Select THREE A/C/E.
- **Verified intended B (retained, caveated):** Route 53 failover policy + health check, CloudWatch alarm → SNS → Lambda to promote cross-Region RDS read replica and raise standby ASG capacity.
- **A:** Latency routing not primary/standby; ALB 5XX alarm incomplete failure detection.
- **B:** Best option, but SNS chain and readiness coordination omitted.
- **C:** Full-size standby costly, latency routing active-active; S3 snapshots not continuous cross-Region RDS replication.
- **D:** Global Accelerator equal weights incompatible with cold standby; ALB 5XX alarm incomplete.
- **AWS:** https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-health-checks.html ; https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html ; https://aws.amazon.com/blogs/networking-and-content-delivery/creating-disaster-recovery-mechanisms-using-amazon-route-53/ ; https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.Promote.html
- **External exact stem:** https://www.examtopics.com/discussions/amazon/view/90943-exam-aws-certified-solutions-architect-professional-sap-c02-topic-1-question-8-discussion/ ; https://www.secexams.com/exams/Amazon/aws-certified-solutions-architect-professional-sap-c02/view/ ; https://www.freecram.net/question/Amazon.SAP-C02.v2024-05-06.q201/a-company-has-a-multi-tier-web-application-that-runs-on-a-fleet-of-amazon-ec2-instances-behind-an-applicat; all single-answer B; no confirmed Choose TWO/THREE variant.
- **Defects:** Route 53 does not directly send SNS; requires CloudWatch alarm. DNS may fail over before replica promotion/ASG readiness; RTO <15 min not guaranteed and needs orchestrated, readiness-gated recovery and test. RDS replica promotion may take minutes+ and asynchronous replication entails RPO. Option C 'Replicationbetween' typo. Preserve original stem/options verbatim.


### Q347 — Domain 4, position 71/139 (2026-10-31)

- **Skipped Q346:** explicit Select THREE despite only 4 options and 2 recorded answers A/D; inconsistent/incomplete source.
- **CORRECTED ANSWER B → C:** External exact-stem source keys B, but B proposes ElastiCache Global Datastore for Memcached, which AWS does not support (only Valkey/Redis OSS). This is a verifiable technical impossibility.
- **A:** RDS separate schemas share DB compute and do not truly isolate session workload.
- **B:** INVALID SERVICE COMBINATION, despite original answer key.
- **C:** Strongest supported performance-focused choice: separate product/session DynamoDB global tables replicate cross-Region; DAX provides regional read cache if DynamoDB data modeling is appropriate.
- **D:** Technically valid RDS product + DynamoDB global session alternative, but lacks DAX read cache; potentially preferable if relational requirements exist.
- **Official AWS:** https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Redis-Global-Datastores-Console.html ; https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.deployment.html ; https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_HowItWorks.html ; https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/dax-config-considerations.html
- **External exact stem (incorrect B key):** https://www.examsvce.com/sap-c02/a-company-wants-to-migrate-its-onpremises-31851-question-answer.html. No confirmed Choose TWO/THREE Q347 variant.
- **Caveats:** 'highest performance' is underspecified without access patterns and relational needs; DAX caches are per-Region and global table replication bypasses DAX, risking stale cached reads. Preserve source punctuation defects in C/D.


### Q355 — Domain 4, position 72/139 (2026-10-31)

- **Skipped Q350:** explicitly Choose two, B/E.
- **Verified C (retained):** EC2 Auto Scaling groups scale existing ALB-backed backend, and DynamoDB auto scaling adjusts provisioned read/write capacity without changing code.
- **A:** Lambda migration adds development; manual DynamoDB capacity increase is not responsive scaling.
- **B:** Lambda rewrite plus DynamoDB global tables (multi-Region replication, not direct single-Region throughput remedy).
- **C:** Best minimal-development architecture.
- **D:** SQS/Lambda introduces asynchronous write integration and does not directly fix read latency.
- **Official AWS:** https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html ; https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.html ; https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/CostOptimization_AutoScalingSettings.html
- **External exact stem:** https://www.exam-tests.com/SAP-C02-exam/Amazon.SAP-C02.v2025-02-24.q513.html?p=19 ; https://www.examcollection.us/exam/SAP-C02-question-answer-4.html ; https://www.shikenpass.com/SAP-C02-shiken.html; correct architecture same despite option reorderings. No confirmed Choose TWO/THREE Q355 variant.
- **Caveats:** DynamoDB auto scaling presumes provisioned capacity mode; on-demand is an alternative outside options. Target-tracking scaling reacts to sustained demand with minutes of CloudWatch evaluation/UpdateTable lag; consider scheduled scaling/pre-warming for seasonal bursts. Original stem/options preserved.


### Q363 — Domain 4, position 73/139 (2026-10-31)

- **Verified B (retained):** VPC Flow Logs → CloudWatch Logs subscription → Amazon Data Firehose → Splunk HEC; near-real-time IP/port connection metadata to on-prem DBs.
- **A:** Periodic CloudWatch export to S3 + Splunk polling is batch/delayed and uses long-lived credentials.
- **B:** Correct streaming pattern; Firehose Lambda preprocessing optional today depending on data format/add-on.
- **C:** Custom per-request logging + Athena/S3/Lambda is slower and requires application changes.
- **D:** Anomaly detection not requested; Kinesis Data Analytics for SQL Applications discontinued January 27 2026.
- **Official AWS:** https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html ; https://docs.aws.amazon.com/firehose/latest/dev/writing-with-cloudwatch-logs.html ; https://aws.amazon.com/blogs/big-data/ingest-vpc-flow-logs-into-splunk-using-amazon-kinesis-data-firehose/ ; https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-firehose.html ; https://docs.aws.amazon.com/kinesisanalytics/latest/dev/
- **External exact stem:** https://www.freecram.net/question/Amazon.SAP-C02.v2026-08-19.q305/a-company-has-developed-a-hybrid-solution-between-its-data-center-and-aws-the-company-uses-amazon-vpc ; https://www.exact2pass.com/sap-c02-aws-certified-solutions-architect-professional-question-9.html; single-answer B, no confirmed Choose TWO/THREE variant.
- **Defects/current guidance:** Stem typo 'application togs'; D 'SOL Applications'. Kinesis Data Firehose renamed Amazon Data Firehose; VPC Flow Logs can publish directly to Firehose, with Splunk HEC and native CloudWatch Logs decompression. Splunk on-prem HEC must be reachable securely. Flow logs are aggregated metadata, not packet payload or SQL statements. Original stem/options preserved.


### Q367 — Domain 4, position 74/139 (2026-10-31)

- **Skipped Q365:** explicit Select TWO A/C.
- **Verified D (retained):** Step Functions/Lambda orchestrate managed Textract OCR/form extraction, optional Comprehend NLP, S3 output, validation and target API integration.
- **A:** Custom OCR and EKS/EC2 operations increase time and maintenance.
- **B:** Step Functions/Lambda good, but self-trained EC2-hosted OCR models add work.
- **C:** Custom SageMaker model and EC2 tier plus ElastiCache unnecessary.
- **D:** Best low-operations managed service workflow.
- **Official AWS:** https://docs.aws.amazon.com/textract/latest/dg/how-it-works-analyzing.html ; https://docs.aws.amazon.com/textract/latest/dg/how-it-works-kvp.html ; https://docs.aws.amazon.com/textract/latest/dg/textract-to-comprehend.html ; https://docs.aws.amazon.com/step-functions/latest/dg/connect-textract.html
- **External exact stem:** https://www.freecram.net/question/Amazon.SAP-C02.v2026-03-31.q264/a-company-has-migrated-its-forms-processing-application-to-aws-when-users-interact-with-the-application ; https://www.freecram.net/question/Amazon.SAP-C02.v2023-03-07.q318/a-company-has-migrated-its-forms-processing-application-to-aws-when-users-interact-with-the-application; Textract architecture D in 2026 variant and B in 2023 variant due to reordered choices. No confirmed Choose TWO/THREE variant.
- **Defects:** Comprehend is NLP, not OCR, despite option D wording; Textract does OCR. Comprehend optional if only key-value form extraction required. Need confidence-based validation and possible human review; async Textract for multipage documents. Option C 'Al/ML' typo. Preserve original stem/options.


### Q374 — Domain 4, position 75/139 (2026-10-31)

- **Verified B (retained):** Aurora PostgreSQL clusters per Region retain raw PII locally; AWS Glue DataBrew can mask/redact data before approved anonymized output is analyzed across Regions in Amazon Redshift Serverless.
- **A:** Outposts is customer-site infrastructure, unnecessary for ordinary Region residency and adds complexity.
- **B:** Correct conceptual managed design, but privacy boundaries need explicit enforcement.
- **C:** Custom Lambda anonymization is possible; PrivateLink/QuickSight alone cannot ensure only anonymized cross-Region datasets are analyzed.
- **D:** Macie detects/classifies sensitive data; it does NOT anonymize it. S3 Block Public Access is not anonymization.
- **Official AWS:** https://docs.aws.amazon.com/databrew/latest/dg/personal-information-protection.html ; https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-datasharing.html ; https://docs.aws.amazon.com/redshift/latest/dg/across-region.html ; https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html
- **External exact stem:** https://www.certensure.com/amazon-web-services/sap-c02-cert-practice-test.html ; https://www.practicetorrent.com/SAP-C02-practice-exam-torrent.html; CertEnsure Question 169 keys B; no confirmed Choose TWO/THREE variant.
- **Defects/caveats:** Require in-Region DataBrew processing, approved anonymized output isolation, permissions to prevent raw PII replication/access, validation against re-identification, and Redshift regional feature availability. DataBrew masking can be reversible and does not automatically establish legal anonymization. Original stem/options preserved.


### Domain 4 Q376 — 76/139 (2026-10-31)

- Eligibility: Q375 skipped (Select THREE). Q376 has four options, one required and one keyed answer. Cross-source exact-stem checks: Pupuweb keys C; GoShiken reorders options and lists the same Outposts + Snowball Edge Compute Optimized solution under D. No confirmed Choose TWO/THREE conflicting version located.
- Correct historical answer: **C** — AWS Outposts at central premises and Snowball Edge Compute Optimized at intermittently connected factories.
- AWS validation: Outposts extends AWS-managed infrastructure/APIs to premises and needs connection to its home Region; Snowball Edge historically supported remote/local compute with limited networking; Wavelength is a carrier 5G edge and Local Zones are AWS-operated sites.
- **High-priority defect — retired service for new customers:** Snowball Edge unavailable to new customers effective Nov 7, 2025, with AWS-advertised commercial-region support ending Dec 31, 2026. Retain C for historical exam context only; do not recommend it for greenfield 2026 infrastructure. Country-specific data-residency requirements require separate verification.
- Sources: https://docs.aws.amazon.com/outposts/latest/userguide/ ; https://docs.aws.amazon.com/outposts/latest/server-userguide/how-outposts-works.html ; https://docs.aws.amazon.com/snowball/latest/developer-guide/snowball-edge-availability-change.html ; https://docs.aws.amazon.com/snowball/latest/developer-guide/doc-history.html ; https://aws.amazon.com/snowball/ ; https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html ; https://pupuweb.com/aws-sap-c02-exam-question-answer-consistent-hybrid-dev-experience/ ; https://www.goshiken.com/blog/goshiken%E3%81%8B%E3%82%89%E3%81%AE%E8%A9%A6%E9%A8%A9%E5%90%88%E6%A0%BC%E6%BA%96%E5%82%99%E3%81%AE%E5%BF%85%E9%9C%80%E5%93%81sap-c02%E8%A9%A6%E5%90%8F%E3%83%88%E3%83%AC%E3%83%BC%E3%83%8B%E3%83%B3%E3%82%B0%E5%95%8F%E9%A1%8C-q527-q543/


### Domain 4 Q377 — 77/139 (2026-10-31)

- Q377: original single-answer item; expected **A — Migration Evaluator**, verified from AWS getting-started and business-case documentation.
- External exact-stem variants: FreeCram labels the same answer D due to shuffled options; ExamTopics.cn labels it A. No verified Choose TWO/THREE variant.
- A: Migration Evaluator collector, scenario, Quick Insights; best answer. B: DMS assessment plus EKS calculator lacks complete TCO. C: MGN migrates servers, not a TCO report. D: Cloud Value Framework does not create a Cost and Usage Report.
- Defect: Quick Insights is a directional infrastructure estimate and does not guarantee detailed EKS managed-node/RDS PostgreSQL TCO; model EKS control plane, nodes, RDS, networking, storage, and operating costs separately.
- References: https://aws.amazon.com/migration-evaluator/getting-started/ ; https://aws.amazon.com/migration-evaluator/features/ ; https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-tools/business-case-migration-evaluator.html ; https://docs.aws.amazon.com/transform/latest/userguide/transform-app-assessments.html ; https://www.freecram.net/question/Amazon.SAP-C02.v2025-07-25.q355/a-company-wants-to-migrate-its-website-to-aws-the-website-uses-containers-that-are-deployed-in-an-on-prem ; https://www.examtopics.cn/exam-aws-certified-solutions-architect-professional-1


### Domain 4 Q385 — 78/139 (2026-10-31)

- Next eligible after Q377: Q381 is Select THREE; Q378-380 and Q382-384 are outside Domain 4. Q385 is single-answer.
- Correct answer **C**: API Gateway REST API + Lambda + DynamoDB on-demand. AWS API Gateway REST API usage plans support API keys, stages, per-client throttling and quotas; Lambda scales business logic and DynamoDB provides low-latency elastic session data access.
- A: NLB and fixed EC2 lack native API Gateway usage plans and elasticity. B: ALB/Lambda/DynamoDB lacks REST API Gateway's API key usage plans. D: AppSync is primarily GraphQL, changing the REST API model; Aurora does not address API key throttling.
- Exact-stem external practice PDF (certsmania, Q67, p.83) keys C as a single-choice question. No substantiated Choose TWO/THREE variant found.
- Caveat: API keys must not be treated as authentication/authorization; usage-plan throttling is best effort. Add an appropriate auth mechanism.
- AWS references: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html ; https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-create-usage-plans.html ; https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-setup-api-keys.html ; https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/on-demand-capacity-mode.html ; https://docs.aws.amazon.com/lambda/latest/dg/lambda-concurrency.html . External: https://www.certsmania.com/pdf/amazon-web-servicesquestion-answer-preparation-changed-sap-c02-questions-by-frederic.pdf


### Domain 4 Q386 — 79/139 (2026-10-31)

- Original single-answer Q386, keyed **A**. AWS VPC DHCP option sets support custom `ntp-servers` and association with a VPC. Existing Direct Connect and appropriate routing/UDP 123 allow access to the on-premises atomic-clock-derived NTP service.
- A correct with OS-specific client verification. B uses Amazon Time Sync rather than the required on-prem source. C introduces an unnecessary third-party relay. D adds VPN complexity and does not set the time client.
- Caveats: DHCP NTP adoption depends on AMI/OS time service configuration; check chrony/ntpd/Windows Time and remove conflicting default sources. Atomic clock is stratum-0 reference; NTP server attached to it generally stratum-1.
- Exact-stem third-party exam-site variant and Choose TWO/THREE conflict **not independently confirmed**; do not claim cross-source verification.
- AWS sources: https://docs.aws.amazon.com/vpc/latest/userguide/DHCPOptionSet.html ; https://docs.aws.amazon.com/vpc/latest/userguide/DHCPOptionSetConcepts.html ; https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateDhcpOptions.html ; https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configure-ec2-ntp.html


### Domain 4 Q395 — 80/139 (2026-10-31)

- Next genuine Domain 4 single-answer after Q386: Q395; Q387–394 belong to other domains. Historical correct answer **A**.
- A: AWS Application Discovery Service Discovery Agent collects server connections; Migration Hub network diagram shows hostnames/IPs/dependencies. Prerequisites require Discovery Agent and permission `discovery:GetNetworkConnectionGraph`.
- B: Agentless Collector has supported network connection discovery since November 2024, but the stated PNG network-diagram export is not established in AWS's documented workflow. C: Application Migration Service agent is for replication/migration, not the specified discovery graph. D: CloudWatch dashboard does not produce dependency topology from a CSV export.
- **HIGH outdated-service warning:** AWS Migration Hub closed to new customers November 7, 2025; preserve historical exam answer A but do not recommend blindly for greenfield 2026 migrations.
- External exact-stem single-choice copies: https://www.examcollection.us/exam/SAP-C02-question-answer-6.html ; https://www.examtopics.com/discussions/amazon/view/132905-exam-aws-certified-solutions-architect-professional-sap-c02-topic-1-question-423-discussion/ . No confirmed Choose TWO/THREE version.
- AWS references: https://docs.aws.amazon.com/migrationhub/latest/ug/network-diagram.html ; https://docs.aws.amazon.com/migrationhub/latest/ug/network-diagram-prerequisites.html ; https://docs.aws.amazon.com/application-discovery/latest/userguide/what-is-appdiscovery.html ; https://aws.amazon.com/about-aws/whats-new/2024/11/network-connections-aws-application-discovery-service-agentless-collector/


### Domain 4 Q409 — 81/139 (2026-10-31)

- Q409 is next genuine single-answer after Q395; Q401 is Select THREE and is skipped. Correct answer **C — AWS DataSync agent, on-prem source, S3 destination, daily scheduled task**.
- AWS docs independently verify NFS/SMB-to-S3 transfers, include/exclude filters, daily scheduling, incremental changed-file copies and task modes.
- A: `CopyObject` copies existing S3 objects, not on-prem VM files. B: AWS Backup plan alone does not provide an arbitrary on-prem VM file-source and directory filters. C: DataSync meets the filtering, schedule, transfer and operational overhead requirements. D: Snowball Edge device adds logistics, with Direct Connect already available; unavailable to new customers since November 7, 2025.
- Caveats: expose VM data via supported NFS/SMB; DataSync transfer/replication is not point-in-time backup retention; consider S3 Versioning/Object Lock; Basic vs Enhanced task mode quotas for ~1 million files. Snowball Edge is outdated for new customers.
- External exam-site exact-stem or Choose TWO/THREE variant not independently confirmed; do not claim third-party corroboration.
- AWS references: https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html ; https://docs.aws.amazon.com/datasync/latest/userguide/task-scheduling.html ; https://docs.aws.amazon.com/datasync/latest/userguide/task-options.html ; https://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html ; https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html ; https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html ; https://docs.aws.amazon.com/snowball/latest/developer-guide/snowball-edge-availability-change.html


### Domain 4 Q413 — 82/139 (2026-10-31)

- Q413 next Domain 4 single-answer after Q409; Q410–Q412 belong to Domain 3. Correct **C — S3 EventBridge Object Created -> EventBridge rule -> Step Functions -> ECS Fargate tasks**.
- A: standard Lambda 15-minute timeout is incompatible with hours-long tasks. B: S3 Event Notifications do not directly invoke Step Functions; EventBridge rule needed. C: Fargate containers plus Step Functions ECS integration support long-running, orchestrated on-demand processing. D: Lambda layers are ZIP-based dependencies, not container images, and standard Lambda timeout still applies.
- Implementation caveats: enable S3 EventBridge delivery; Object Created events can start one execution per uploaded object; use batch-completion marker/idempotency if exactly one nightly run required. Newer Lambda Managed Instances has distinct limits, not specified in the choices.
- AWS verification: https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-cloudwatch-events-s3.html ; https://docs.aws.amazon.com/step-functions/latest/dg/connect-ecs.html ; https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventBridge.html ; https://docs.aws.amazon.com/lambda/latest/dg/configuration-timeout.html ; https://docs.aws.amazon.com/lambda/latest/dg/chapter-layers.html . External exam-site exact-stem and Choose TWO/THREE variants **not independently confirmed**.


### Domain 4 Q414 — 83/139 (2026-10-31)

- Original single-answer Q414; verified **D** from AWS Amplify Hosting, Amplify Storage and AWS Storage Blog documentation, plus exact-stem examsvce and examtopics.cn sources (both single-choice). No confirmed Choose TWO/THREE variant.
- A: EC2 Auto Scaling/ALB retains server management. B: Same EC2 burden, plus IAM Identity Center is less appropriate than Cognito for customer sign-in. C: AppSync/Lambda resolvers add unnecessary API and upload processing complexity. D: Amplify Hosting/CloudFront frontend, Cognito authentication and direct S3 uploads deliver low operational overhead.
- Corrected typo `usersshould` to `users should` in original stem.
- Caveats: explicitly configure Cognito-authorized S3 upload permissions, private storage paths and bucket access. CloudFront serves static assets; direct S3 uploads are a separate path, not automatically accelerated by website CDN.
- AWS references: https://docs.aws.amazon.com/amplify/latest/userguide/deploy-website-from-s3.html ; https://docs.amplify.aws/react/frontend/storage/upload-files/ ; https://aws.amazon.com/blogs/storage/allowing-external-users-to-securely-and-directly-upload-files-to-amazon-s3/ ; https://aws.amazon.com/blogs/networking-and-content-delivery/implementing-secure-file-uploads-to-amazon-s3-at-the-edge-choosing-the-right-pattern/ . External: https://www.examsvce.com/sap-c02/a-company-runs-an-application-in-an-55856-question-answer.html ; https://www.examtopics.cn/exam-aws-certified-solutions-architect-professional-5


### Domain 4 Q416 — 84/139 (2026-10-31)

- Q416 next Domain 4 single-answer after Q414 (Q415 belongs to Domain 3). Verified **D — ECS Fargate with ECS Service Auto Scaling, shared EFS, Aurora MySQL Serverless v2 reader**.
- A: Lambda supports ALB targets but cannot mount EBS as specified. B: Step Functions state machines cannot serve as ALB targets or mount EFS. C: Fargate scaling and RDS MySQL Multi-AZ DB cluster (including readable standby instances) are feasible, but a single EBS volume cannot serve as the common shared file system across independently scaling Fargate tasks. D: resolves scaling, shared file consistency, and read-heavy database pressure.
- Wording fixes applied: `The loads static content` -> `The application loads static content`; `EBSvolume`, `ECS duster`, `MySOL`, missing `for`, and punctuation in option D. Technical intent unchanged.
- External exact-stem SAP-C02 collection found with different option order; map answer by text, not letter. Single-choice source; no independently verified Choose TWO/THREE variant: https://examsdocs.dumpsquestion.com/articles/assume-amazon-sap-c02-dumps-pdf-are-going-to-be-the-best-score-q27-q52/
- AWS references: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/efs-volumes.html ; https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2-administration.html ; https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-loadbalancer.html ; https://repost.aws/knowledge-center/ecs-fargate-mount-efs-containers-tasks
- Caveats: use ALB IP target type for Fargate; tune EFS throughput and Aurora reader endpoint routing. RDS Multi-AZ DB clusters are not invalid solely because of read scaling.


### Domain 4 Q420 — 85/139 (2026-10-31)

- Next eligible Domain 4 single-answer after Q416; Q417–419 belong to other domains. Correct **C**: DMS full-load + CDC on-prem MySQL to Aurora, Aurora Replica for aggregation, ALB -> Lambda collector -> RDS Proxy -> Aurora writer, DNS cutover.
- A invalid: NLB does not directly target Lambda; restarting an Aurora reader as primary is not the specified migration cutover. B leaves reporting on the Aurora writer, perpetuating ingestion/reporting contention. C isolates reads and maintains a customer-facing HTTP endpoint. D: Kinesis stream is not an equivalent customer HTTP endpoint and Firehose does not directly deliver to Aurora MySQL.
- Fixed original punctuation/OCR defects (`Node js`, `endpomts`, `wnte`, `AuroraReplica`, missing periods). Historical exam source answer C preserved.
- **Cutover caveat:** DMS CDC is asynchronous; 'without interruptions' is not guaranteed. Quiesce writes, monitor lag, validate target, account for DNS TTL and client connections, and only then stop DMS after cutover.
- External exact-stem single-answer source: https://cciedump.spoto.net/exam-questions/free-aws-sap-c02-practice-questions-answers-2026-part2 (Q58, C). Additional matching stem: https://pupuweb.com/aws-certified-solutions-architect-professional-sap-c02-actual-exam-question-answer-dumps-2/ . No verified Choose TWO/THREE variant.
- AWS references: https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Task.CDC.html ; https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Endpoints.Reader.html ; https://docs.aws.amazon.com/lambda/latest/dg/services-rds.html ; https://docs.aws.amazon.com/elasticloadbalancing/latest/application/lambda-functions.html


### Domain 4 Q421 — 86/139 (2026-10-31)

- **Duplicate of Q386 (79/139)**: Q421 is a short paraphrase of the same on-premises atomic-clock NTP / EC2 / DHCP options question. Correct **A**. Mark as duplicate, not a new study topic.
- A: VPC DHCP option `ntp-servers` points to the on-premises NTP appliance, with Direct Connect routing and UDP/123. B: Amazon Time Sync is not the on-premises clock. C: Marketplace NTP relay adds maintenance. D: IPsec VPN does not configure EC2 time clients and adds complexity.
- Fixed `on-premisesatomic` and `theleast` spacing. OS NTP client must honor DHCP option; stratum-0 reference is normally served by stratum-1 NTP appliance.
- Full-stem external single-answer matches: https://www.certsmania.com/pdf/amazon-web-services-selected-sap-c02-practice-simulations-questions-answers-by-amit.pdf ; https://www.dumpstech.com/free-amazon-web-services/sap-c02-practice-10.html . No verified Choose TWO/THREE version. Conflicting/wrong explanation favoring AWS Time Sync appears at https://blog.surepassexams.com/2026/10/26/online-sap-c02-test-brain-dump-question-and-test-engine-q89-q105/ ; reject because it fails the required on-premises time source.
- AWS references: https://docs.aws.amazon.com/vpc/latest/userguide/DHCPOptionSet.html ; https://docs.aws.amazon.com/vpc/latest/userguide/DHCPOptionSetConcepts.html ; https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateDhcpOptions.html

- Additional independent single-answer corroboration: https://www.solution2pass.com/Amazon-Web-Services/SAP-C02-question-answers.html ; https://www.dumpsmate.com/SAP-C02-exam.html ; https://www.freecram.net/question/Amazon.SAP-C02.v2026-03-31.q264/a-company-is-planning-to-migrate-its-on-premises-data-analysis-application-to-aws-the-application-is . All favor the DHCP solution (A in those versions).
- **Conflicting external answer key:** https://realexamcollection.examslabs.com/articles/mar-2025-newly-released-sap-c02-exam-questions-for-you-to-pass-q59-q76/ rearranges option labels and identifies the DHCP option as C, yet prints answer A (Amazon Time Sync AMI). This does not meet the explicit on-premises time-source constraint. Flag as defective external key, not evidence for changing the correct solution. No confirmed Choose TWO/THREE variant.
- Current AWS EC2 Amazon Time Sync endpoint reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configure-ec2-ntp.html . Existing Q421 text intentionally abbreviates Q386; full original question and choices remain in Q386.


### Domain 4 Q424 — 87/139 (2026-10-31)

- **Correct C: AWS Global Accelerator** with regional ALB endpoint groups, static anycast IPv4 addresses, and apex-domain A records hosted in the company's existing DNS. Default IPv4 accelerator has **two** addresses, not one; publish both.
- **A:** apex CNAME not allowed, Route 53 migration unnecessary. **B:** CNAME to literal IP and apex CNAME invalid, NLB tier unnecessary. **D:** apex CNAME invalid; API Gateway/Lambda router unnecessary and adds regional dependency.
- AWS: https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoints.html ; https://docs.aws.amazon.com/global-accelerator/latest/dg/dns-addressing-custom-domains.dns-addressing.html ; https://docs.aws.amazon.com/global-accelerator/latest/dg/introduction-how-it-works.html
- Exact-stem third-party single-answer cross-check: https://www.freecram.net/question/Amazon.SAP-C02.v2026-03-31.q264/a-global-media-company-is-planning-a-multi-region-deployment-of-an-application-amazon-dynamodb-global ; https://pupuweb.com/aws-certified-solutions-architect-professional-sap-c02-actual-exam-question-answer-dumps-2/4/ ; https://www.passtest.jp/articles/2023%E5%B9%B410%E6%9C%88-%E6%9B%B4%E6%96%B0%E3%81%AEamazon-sap-c02%E8%A9%A6%E9%A8%93%E5%9F%BA%E6%9C%AC%E5%95%8F%E9%A1%8C%E3%81%AB%E3%81%AF%E8%A7%A3%E7%AD%94%E3%81%8C%E4%BB%98%E3%81%8D%E3%81%BE%E3%81%99-q39-q64/ . PassTest reorders options but chooses Global Accelerator. No verified Choose TWO/THREE variant.


### Domain 4 Q427 — 88/139 (2026-10-31)

- **CORRECTED SOURCE ANSWER B → A**. NLB-backed TCP AWS PrivateLink endpoint service is supported. Standalone ALB-backed endpoint service in B is not supported (NLB/GWLB only).
- A: NLB TCP service published through PrivateLink; route from NLB to on-prem IP targets over DX/VPN; consumers use interface endpoints. B: ALB cannot directly back endpoint service, though NLB can target ALB. C: IGW exposes internet connectivity. D: NAT gateway cannot publish service.
- Fixed OCR and punctuation errors in stem and C/D without changing intent. DX is the hybrid backend path; PrivateLink is the customer-facing private path. No verified Choose TWO/THREE variant.
- AWS documentation: https://docs.aws.amazon.com/vpc/latest/privatelink/create-endpoint-service.html ; https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html ; https://aws.amazon.com/privatelink/faqs/
- External exact-stem single-answer question: https://www.p2pexams.com/free-questions/amazon-sap-c02-dumps-by-espinoza-09-08-2024-10qa-go4braindumps.pdf . Prior B answer contradicted AWS primary docs.


### Domain 4 Q434 — 89/139 (2026-10-31)

- **Verified answer A:** S3 ObjectCreated notifications invoke AWS Lambda; average five-minute runtime fits 15-minute maximum, but worst-case duration must be checked. No idle EC2 and minimal management.
- A correct: direct event-driven Lambda. B: SQS/EC2 Auto Scaling minimum one instance costs more and requires administration. C: EC2 container retains polling and EC2 management. D: ECS Fargate unnecessary; option reverses `RunTask` invocation order.
- Defects: missing punctuation in stem fixed. At-least-once/out-of-order S3 notifications require idempotency. Conflicting Brainscape flashcard keys D, while SPOTO explicitly keys A. Full-stem single-answer copies exist; no confirmed Choose TWO/THREE variant.
- AWS: https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventNotifications.html ; https://docs.aws.amazon.com/lambda/latest/dg/with-s3.html ; https://docs.aws.amazon.com/AmazonS3/latest/userguide/notification-how-to-event-types-and-destinations.html ; https://aws.amazon.com/blogs/storage/manage-event-ordering-and-duplicate-events-with-amazon-s3-event-notifications/
- External: https://cciedump.spoto.net/exam-questions/free-aws-sap-c02-practice-questions-answers-2026-part1 ; https://pupuweb.com/aws-certified-solutions-architect-professional-sap-c02-actual-exam-question-answer-dumps-1/3/ ; https://www.brainscape.com/flashcards/solutions-architect-professional-deck-02-15140066/packs/21889491


### Domain 4 Q437 — 90/139 (2026-10-31)

- **Best answer C:** EKS on Fargate + Aurora Serverless MySQL + Redshift Serverless + EventBridge. Preserves transactional/analytical separation, uses serverless application compute, and enables event routing.
- A: MySQL on EC2 not serverless; Neptune graph database unsuitable for OLAP. B: EC2 ASGs not serverless; Aurora MySQL not analytical warehouse. C: Best architecture, but requires an actual ingestion integration to write events into Redshift. D: AppStream 2.0 desktop streaming and IoT Core do not fit retail microservices.
- **MODERATE DEFECT:** EventBridge does not directly populate Redshift Serverless tables simply by routing events; configure an ingestion pipeline/consumer. EKS on Fargate still needs cluster management.
- External exact-stem single-answer copies: https://www.examtopics.com/discussions/amazon/view/136656-exam-aws-certified-solutions-architect-professional-sap-c02-topic-1-question-474-discussion/ (C) and https://www.pdfdumps.com/articles/real-amazon-sap-c02-exam-questions-study-guide-q217-q242/ (D with rearranged options); both select the same architecture. No independently confirmed Choose TWO/THREE variant.
- AWS: https://aws.amazon.com/eventbridge/faqs/ ; https://docs.aws.amazon.com/eventbridge/latest/ref/events-ref-redshift-serverless.html ; https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-event-notifications-eventbridge.html
