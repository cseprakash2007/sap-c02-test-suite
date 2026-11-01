# Q9 vs Q510 — AWS Elastic Disaster Recovery

Q9 asks for dedicated private replication and explicit 75% throttling; stored A,D,E includes private subnets, Direct Connect, private IP plus throttling.

Q510 asks no public replication, no public application, and not consuming all bandwidth; stored B,D,E. Public staging subnet does not automatically expose recovered application, but private replication and private recovery must be configured independently. Option E selects private IP but does not explicitly throttle. Option A private subnets and NAT is arguably better, yet there is no direct throttle option. **Do not silently change Q510 key; flag ambiguity.**

AWS references:
- https://docs.aws.amazon.com/drs/latest/userguide/data-routing.html
- https://docs.aws.amazon.com/drs/latest/userguide/Network-Requirements.html
- https://docs.aws.amazon.com/drs/latest/userguide/Network-Settings-Preparations.html
