<!-- Mergetober 2026 Blog Post: Umami Integration -->
<!-- Author: Mallikarjun R (@mallikarjunr444-gif) -->
<!-- Pull Request: https://github.com/topoteretes/cognee-community/pull/442 -->
<!-- Issue: https://github.com/topoteretes/cognee/issues/6093 -->

# Giving AI Agents Web Analytics Context: Building an Umami Connector for Cognee

Umami is the leading privacy-preserving open-source web analytics platform. When building intelligent product assistants or growth agents, having real-time context on website visitors, bounce rates, and top pages empowers the agent to answer questions accurately without human intervention.

During Mergetober, I built the **Umami Data-Source Connector** for [Cognee](https://github.com/topoteretes/cognee) to turn website traffic trends into searchable knowledge graph memory.

---

## Features
- **Traffic Ingestion**: Ingests unique visitors, pageview totals, visit counts, average session durations, and bounce rates.
- **Top Path Analysis**: Extracts the top visited pages and paths for each website.
- **Document Mode (`DOCUMENT_SOURCE_ATTR = "umami"`)**: Converts web analytics reports into structured Markdown for semantic entity extraction.
- **Self-Hosted & Cloud Support**: Configurable with custom endpoints (`base_url`).

---

## Example Usage