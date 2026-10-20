# Product-Led Email Context as Cognitive Memory: Building a Loops.so Connector for Cognee

Loops.so is the modern email platform built for SaaS companies and software developers. Product teams trigger transactional messages and segment users based on in-app events. Giving AI agents access to Loops data lets them personalize conversations based on real subscriber properties.

During Mergetober 2026, I built the **Loops.so Data-Source Connector** for [Cognee](https://github.com/topoteretes/cognee).

## How It Works
- **Contact Ingestion**: Ingests email addresses, user groups, custom properties, and subscription status into Cognee's cognitive graph.
- **Transactional Campaigns**: Ingests published transactional email definitions.
- **Document Mode**: Emits `DOCUMENT_SOURCE_ATTR = "loops"`.
- **Automatic Backoff**: Retries automatically on rate limits.

Author: Mallikarjun R (@mallikarjunr444-gif)
