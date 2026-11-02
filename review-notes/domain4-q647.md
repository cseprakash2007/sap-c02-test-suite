# Domain 4 Q647 — question 136/139

**Verified answer C with current AWS naming and authentication caveats.** Reviewed 2026-11-01. Original stem and all options preserved in questions.json.

## Scenario
Existing Windows desktop app must serve acquired Linux employees and existing Windows employees, authenticated, with least application development effort.

## Option-by-option
- **A incorrect:** Amazon WorkSpaces Personal provides whole virtual desktops rather than application streaming; Cognito identity pools are not the WorkSpaces desktop sign-in mechanism.
- **B incorrect:** Self-managed Windows EC2/RDP access and Active Directory join can work but require more operational setup, remote access security, and fleet management.
- **C correct:** AppStream 2.0 (current name Amazon WorkSpaces Applications) image builder packages Windows app; On-Demand fleet and auto scaling serve Linux and Windows users via web browser without application rewrite; built-in user pool authenticates users.
- **D incorrect:** Refactoring desktop app into web application on ECS Fargate is substantial development effort.

## Important nuances
- **Service rename:** Amazon AppStream 2.0 is now **Amazon WorkSpaces Applications**, not retired.
- **Identity:** User pools are independent of on-prem AD. If existing AD sign-in is a strict requirement, SAML 2.0 federation with AD-backed IdP is more suitable; domain-joined fleets require SAML federation.
- **Fleet:** On-Demand fleet can add 1-2 minutes startup; not relevant to least development effort.
- **OCR defects:** 'lo AWS', '(or all', 'Auto Scarlet', 'Ama7on', 'starling browse'' and capitalization errors. Original wording preserved.

## External cross-check and variants
- CertEnsure SAP-C02: answer **C**, exact architecture.
- P2PExams SAP-C02 Foster PDF: answer **C**, exact stem.
- PassTest SAP-C02 Q22-Q38: answer **B**, equivalent to repo **C** with options reordered.
- No confirmed Choose TWO/THREE variant.

## AWS documentation
- https://aws.amazon.com/workspaces/applications/
- https://docs.aws.amazon.com/appstream2/latest/developerguide/accessing-as-user.html
- https://docs.aws.amazon.com/appstream2/latest/developerguide/fleet-type.html
- https://docs.aws.amazon.com/appstream2/latest/developerguide/autoscaling.html

## External sites
- https://www.certensure.com/amazon-web-services/sap-c02-cert-practice-test.html
- https://www.p2pexams.com/free-questions/amazon-sap-c02-dumps-by-foster-09-08-2024-12qa-vceexamstest.pdf
- https://www.passtest.jp/articles/%E8%A9%A6%E9%A8%93%E6%BA%96%E5%82%99%E3%81%AB%E3%81%AF%E6%AC%A0%E3%81%8B%E3%81%95%E3%81%AA%E3%81%84-sap-c02%E5%95%8F%E9%A1%8C%E8%A7%A3%E7%AD%94%E3%81%A7sap-c02%E8%A9%A6%E9%A8%93%E5%95%8F%E9%A1%8C%E9%9B%86-q22-q38/
