# Domain 4 Q626 — question 132/139

**Status: DISPUTED SOURCE KEY.** Source answer **D** retained for traceability, but **C** is arguably more cost-effective for users on the company's network. Reviewed 2026-11-01.

## Original scenario
Secure RDP to EC2 Windows, centralized on-prem AD, internet connectivity, and existing hardware capable of AWS Site-to-Site VPN. Asks MOST cost-effectively.

## All options
- **A:** AWS Managed Microsoft AD trust plus EC2 bastion. Works but adds managed directory and bastion infrastructure.
- **B:** IAM Identity Center + AD Connector + Systems Manager Fleet Manager. Browser-based RDP possible without inbound RDP, but permissions, managed-node requirements, identity mapping and authentication semantics require care.
- **C:** Site-to-Site VPN + existing on-prem AD + private RDP. Reuses AD and existing VPN hardware, avoiding managed AD and gateway compute. Likely lowest cost for users connecting **from the company's on-premises network**. Site-to-Site VPN does not independently connect arbitrary remote users.
- **D (published source key):** Managed AWS Microsoft AD trust plus Remote Desktop Gateway. Valid secure access pattern and preferred by several exam sites, but incurs recurring directory and gateway costs. Could be justified for users connecting from outside the company network.

## Independent source comparison
- FreeCram SAP-C02 q171: keys **B**, equivalent to repo **D**.
- DumpsTech SAP-C02 practice 9: keys **D**, equivalent to repo **D**.
- JPNTest SAP-C02 Q455: keys **B**, equivalent to repo **D**.
- No confirmed Choose TWO/THREE version.

## Why the question is ambiguous
The explicit available VPN hardware and 'MOST cost-effectively' wording strongly support C if users access from the corporate network. D is a valid design for distributed remote users but the stem does not explicitly say users are outside the corporate network. Do not treat exam-site agreement as proof of cost optimality. Keep original D source key but mark `answerStatus: source-key-disputed` and `review.status: disputed-source-key-cost-vs-remote-access-ambiguity`.

## Source transcription defects
Missing spaces: `Active Directory.Deploy`, `MicrosoftActive`, `toaccess`, `on- premises`. Preserve original wording.

## Official AWS sources
- https://docs.aws.amazon.com/vpn/latest/s2svpn/customer-gateway-device-windows.html
- https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-network-access-options/options-onprem.html
- https://docs.aws.amazon.com/us_en/systems-manager/latest/userguide/fleet-manager-remote-desktop-connections.html
- https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_join_instance.html

## Exam sites
- https://www.freecram.net/question/Amazon.SAP-C02.v2024-03-21.q171/a-company-s-solutions-architect-needs-to-provide-secure-remote-desktop-connectivity-to-users-for-amazon
- https://www.dumpstech.com/free-amazon-web-services/sap-c02-practice-9.html
- https://www.jpntest.com/blog/2026%E5%B9%B409%E6%9C%88-%E6%9B%B4%E6%96%B0%E3%81%AE... (Q455; full URL available from search)
