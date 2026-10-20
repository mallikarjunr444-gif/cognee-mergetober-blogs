<!-- Mergetober 2026 Blog Post: Dub.co Integration -->
<!-- Author: Mallikarjun R (@mallikarjunr444-gif) -->
<!-- Pull Request: https://github.com/topoteretes/cognee-community/pull/441 -->
<!-- Issue: https://github.com/topoteretes/cognee/issues/6091 -->

# Linking AI Agents to Conversion Funnels: Building a Dub.co Connector for Cognee

Dub.co is the leading modern link management platform. For AI agents interacting with marketing campaigns, knowing what links exist, where they redirect, and how many clicks they drive is essential context.

During Mergetober, I built the **Dub.co Data-Source Connector** for [Cognee](https://github.com/topoteretes/cognee) to connect short URLs and click analytics into Cognee's AI memory.

---

## Features
- **Link & Metric Ingestion**: Ingests keys, short URLs, destination targets, click counts, campaign tags, and comments.
- **Document Mode (`DOCUMENT_SOURCE_ATTR = "dub"`)**: Renders links into Markdown documents for knowledge graph entity extraction.
- **Forget-on-Delete**: Syncs with `write_disposition="replace"`, pruning archived or removed links automatically.

---

## Example Usage