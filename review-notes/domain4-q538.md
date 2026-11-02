# Domain 4 Q538 — question 118/139

**Source answer A is defective. Best available answer D, with caveats.** Original question and option texts retained in `src/data/questions.json`; corrected answer and detailed audit metadata saved there.

## Independent AWS verification
AWS Direct Connect MACsec supports dedicated **10, 100, and 400 Gbps** connections, **not 1 Gbps**. Thus A and B require unsupported MACsec. A's private IP VPN is transported over Direct Connect transit VIF to Transit Gateway; when the single underlying DX fails, so does this VPN. B's second DX can offer redundancy but is more expensive and still cannot use MACsec at 1 Gbps. C's multiple VIFs share one physical DX failure domain and do not encrypt. D's internet-based IPsec VPN can provide independent backup at lower cost, but **static routing** requires careful configuration and is less robust than dynamic BGP routing, which is missing from the choices. AWS specifically describes Site-to-Site VPN backup for DX connections <=1 Gbps.

## External source conflict
P2PExams SAP-C02 PDF Question 1 reproduces exact stem/options and answers **A**, incorrectly asserting MACsec on 1 Gbps DX. CertEnsure SAP-C02 Q167 reproduces exact question/options. No verified Choose TWO/THREE version. Treat external answer keys as unreliable when inconsistent with official AWS prerequisites.

## Wording defects
OCR: `tor` -> `for`; `win` -> `will`; `Direct Conned` and `Dried Conned` -> `Direct Connect`; stray hyphens in `on- premises`.

## References
- https://docs.aws.amazon.com/directconnect/latest/UserGuide/MACsec.html
- https://aws.amazon.com/vpn/faqs/
- https://aws.amazon.com/directconnect/resiliency-recommendation/
- https://docs.aws.amazon.com/vpn/latest/s2svpn/vpn-static-dynamic.html
- https://aws.amazon.com/directconnect/faqs/
- https://www.p2pexams.com/free-questions/amazon-sap-c02-dumps-by-foster-09-08-2024-12qa-vceexamstest.pdf
- https://www.certensure.com/amazon-web-services/sap-c02-cert-practice-test.html

Reviewed 2026-11-01.