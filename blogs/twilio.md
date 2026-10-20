<!-- Mergetober 2026 Blog Post: Twilio Integration -->
<!-- Author: Mallikarjun R (@mallikarjunr444-gif) -->
<!-- Pull Request: https://github.com/topoteretes/cognee-community/tree/feature/twilio-connector -->
<!-- Issue: https://github.com/topoteretes/cognee/issues/6100 -->

# Customer Messaging in AI Memory: Building a Twilio Connector for Cognee

Customer support agents and voice copilots need to know what communications have taken place across SMS and WhatsApp. Without a unified knowledge graph, customer interactions are lost in disconnected communication silos.

During **Mergetober**, I built the **Twilio Data-Source Connector** for [Cognee](https://github.com/topoteretes/cognee).

---

## Features
- **SMS & WhatsApp Ingestion**: Ingests message bodies, senders, recipients, delivery statuses, directions, and timestamps.
- **Document Mode (`DOCUMENT_SOURCE_ATTR = "twilio"`)**: Translates messages into structured Markdown for entity linking and semantic extraction.
- **Full Snapshot + Forget-on-Delete**: Clean synchronization model ensuring deleted or redacted messages prune automatically.
- **Exponential Backoff**: Resilient retry on HTTP 429 rate limit responses.

---

## Example Usage