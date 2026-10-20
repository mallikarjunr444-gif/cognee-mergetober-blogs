<!-- Mergetober 2026 Blog Post: Postmark Integration -->
<!-- Author: Mallikarjun R (@mallikarjunr444-gif) -->
<!-- Pull Request: https://github.com/topoteretes/cognee-community/pull/440 -->
<!-- Issue: https://github.com/topoteretes/cognee/issues/6090 -->

# Giving AI Agents Transactional Email Memory: Building a Postmark Connector for Cognee

Postmark (by ActiveCampaign) is the backbone of transactional messaging for modern software products. Transactional emails contain vital product notifications: invoices, security verification alerts, subscription confirmations, and receipts.

During Mergetober, I built the **Postmark Data-Source Connector** for [Cognee](https://github.com/topoteretes/cognee) to give AI agents access to transactional email templates and delivery logs.

---

## Features
- **Template Ingestion**: Extracts template names, aliases, layouts, subjects, and text/HTML bodies.
- **Document Mode (`DOCUMENT_SOURCE_ATTR = "postmark"`)**: Bypasses flat row indexing and passes templates directly to Cognee's cognify engine to construct an entity knowledge graph.
- **Forget-on-Delete**: Syncs with `write_disposition="replace"`, automatically pruning removed templates via Cognee's `orphan_cleanup`.

---

## Example Usage