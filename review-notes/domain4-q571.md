# Domain 4 Q571 — single-answer question 122/139

**Original source D. Best modern literal design A with explicit viewer-response trigger; item is ambiguous/non-unique.** Full original stem and choices retained in questions.json.

## Independent AWS verification
CloudFront Functions on the **viewer-response** event receive both `event.request.headers` (including User-Agent) and `event.response.headers`; they can delete a response header selectively for legacy clients. AWS documents `var request=event.request; var response=event.response; ... return response` at https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/function-code-choose-purpose.html . Lambda@Edge **viewer-response** can also perform this task. Lambda@Edge **viewer-request** cannot edit the eventual origin response.

## All options
- **A best with clarification:** CloudFront -> ALB Lambda target; CloudFront Function **viewer-response** can inspect request User-Agent and remove selected response headers. Option omits explicit event phase.
- **B wrong:** REST API default gateway responses cover API Gateway-generated errors, not general successful Lambda integration responses.
- **C wrong as written:** HTTP APIs support response **parameter mapping**, not VTL response **mapping templates**; the option doesn't establish conditional per-User-Agent removal.
- **D ambiguous:** If 'in response to viewer requests' refers to a viewer-request trigger, impossible because response is not available. If it describes a Lambda@Edge viewer-response function for each request, it also works. No unique correct option under this reading.

## External check
Exact-stem FreeCram Q243/305 keys **D**, matching original source key. Other practice copies exist. No confirmed Choose TWO/THREE variant. Flag as defective/non-unique rather than confidently rejecting a valid viewer-response Lambda@Edge design.

## References
- https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/function-code-choose-purpose.html
- https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/functions-event-structure.html
- https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-event-structure.html
- https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-functions.html
- https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html
- https://www.freecram.net/question/Amazon.SAP-C02.v2026-08-19.q305/a-company-uses-a-service-to-collect-metadata-from-applications-that-the-company-hosts-on-premises-consumer

Reviewed 2026-11-01.