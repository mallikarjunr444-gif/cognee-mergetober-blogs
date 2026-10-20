# Privacy-Preserving Web Analytics in Long-Term Memory: Building a Plausible Connector for Cognee

Plausible Analytics provides clean, lightweight web analytics without tracking personal data. By feeding Plausible metrics into Cognee's knowledge graph, marketing and product agents can recall site performance, top pages, and traffic referrals.

## How It Works
- **Aggregate Metrics**: Ingests 30-day visitors, pageviews, bounce rates, and visit duration.
- **Breakdown Tracking**: Ingests top pages (`event:page`) and referrers (`visit:source`).
- **Realtime Traffic**: Ingests active visitor counts for instant reasoning.
- **Document Mode**: Emits `DOCUMENT_SOURCE_ATTR = "plausible"`.

Author: Mallikarjun R (@mallikarjunr444-gif)
