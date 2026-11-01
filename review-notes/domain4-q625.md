# Domain 4 Q625 — question 131/139

**Verified answer B.** Original full stem and all four choices preserved in questions.json. Reviewed 2026-11-01.

## Scenario
On-premises HTTPS clients access an existing internal ALB over AWS Direct Connect. The ALB terminates TLS and forwards by URL path to EC2 target groups. An on-premises firewall now needs a static destination-IP allow list.

## Correct architecture
Internal **NLB** with a static private IP per enabled Availability Zone; allow-list each NLB IP on the firewall. NLB **TCP 443** listener forwards to an **ALB-type target group** registering the existing internal ALB. Existing ALB continues TLS termination and path-based routing. Update client DNS and verify Direct Connect routing/security.

## Every original option
- **A wrong:** Cannot assign static addresses to ALB nodes; addresses may change.
- **B correct:** NLB static private IPs plus ALB-type target group preserve ALB HTTPS/TLS and Layer 7 rules.
- **C wrong:** NLB does not support path-based routing, and deleting ALB breaks application behavior. Cannot simply move ALB HTTP routing target groups to NLB.
- **D wrong:** GWLB is for transparent network-appliance insertion and does not have an ALB-type target group.

## Implementation caveats
- Use internal NLB for Direct Connect/private client access.
- NLB target type `alb` registers one ALB; AWS requires compatible listener/target ports and same VPC/account. Use TCP pass-through on 443 to keep TLS on ALB.
- NLB static private IP per enabled AZ; allow-list all AZ addresses and ensure DNS, routing and security rules.

## Source defects and variants
- Exact-stem FreeCram SAP-C02 Q137 keys B. No verified Choose TWO/THREE variant.
- B contains `ALAdd` (missing punctuation) and `one static IP addresses`; C has `LNB` and missing punctuation; original wording preserved and flagged.

## AWS official references
- https://docs.aws.amazon.com/elasticloadbalancing/latest/network/application-load-balancer-target.html
- https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancers.html
- https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html

## External exact-stem source
- https://www.freecram.net/question/Amazon.SAP-C02.v2023-09-11.q137/a-telecommunications-company-is-running-an-application-on-aws-the-company-has-set-up-an-aws-direct-connec
