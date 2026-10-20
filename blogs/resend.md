# Transactional Email as Continuous Context: Building a Resend Connector for Cognee

Customer interactions frequently happen over transactional emails—order receipts, password resets, onboarding tips, and notifications. For AI assistants, having access to these emails means knowing exactly what communications a customer has already received.

During Mergetober 2026, I built the **Resend Data-Source Connector** for [Cognee](https://github.com/topoteretes/cognee).

## How It Works
- **Sent Email Ingestion**: Extracts recipient, sender, subject, delivery status, and full HTML/text content.
- **Audience & Contact Tracking**: Ingests audience segments and subscriber counts into Cognee's cognitive graph.
- **Document Mode**: Emits `DOCUMENT_SOURCE_ATTR = "resend"` so Cognee extracts entities and relationships.
- **Resilient Transport**: Automatic retry on HTTP 429 rate limit responses with backoff.

Author: Mallikarjun R (@mallikarjunr444-gif)
