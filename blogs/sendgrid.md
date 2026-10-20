<!-- Mergetober 2026 Blog Post: SendGrid Integration -->
<!-- Author: Mallikarjun R (@mallikarjunr444-gif) -->
<!-- Pull Request: https://github.com/topoteretes/cognee-community/pull/438 -->
<!-- Issue: https://github.com/topoteretes/cognee/issues/6087 -->

# Giving AI Agents Customer Communication Memory: Building a SendGrid Connector for Cognee

AI agents and automated customer assistants often operate in silos. Without contextual memory, an agent answering user questions has no idea what onboarding emails were delivered, what password resets were triggered, or what marketing templates exist.

To solve this, I built the **SendGrid Data-Source Connector** for [Cognee](https://github.com/topoteretes/cognee) during **Mergetober** (hosted by WeMakeDevs × Cognee).

---

## What Does the SendGrid Connector Do?
The connector plugs directly into the SendGrid v3 REST API to extract:
1. **Dynamic Transactional Email Templates**: Ingests template versions, subject lines, and body content.
2. **Marketing Contact Lists**: Ingests audience segments and subscriber counts.

Rather than treating email data as flat rows, the connector marks the data source with `DOCUMENT_SOURCE_ATTR = "sendgrid"`. This triggers Cognee's **document-mode cognify pipeline**, converting email content into nodes and edges in a knowledge graph with full entity and relationship extraction.

---

## How It Works in Code