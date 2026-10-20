<!-- Mergetober 2026 Blog Post: Linear Integration -->
<!-- Author: Mallikarjun R (@mallikarjunr444-gif) -->
<!-- Pull Request: https://github.com/topoteretes/cognee-community/tree/feature/linear-connector -->
<!-- Issue: https://github.com/topoteretes/cognee/issues/6100 -->

# Giving AI Agents Engineering Roadmap Memory: Building a Linear Connector for Cognee

Engineering teams live and breathe in Linear. From sprint cycles and critical bug triage to roadmap milestones, Linear holds the source of truth for technical development. However, developer AI agents often lack real-time visibility into these issues.

During **Mergetober** (hosted by WeMakeDevs × Cognee), I built the **Linear Data-Source Connector** for [Cognee](https://github.com/topoteretes/cognee) to turn issues, priorities, and sprint roadmaps into cognitive knowledge graphs.

---

## Features
- **Issue & Task Ingestion**: Ingests issue identifiers (`ENG-123`), titles, descriptions, priorities, assignees, and labels via Linear's GraphQL API.
- **Document Mode (`DOCUMENT_SOURCE_ATTR = "linear"`)**: Converts issues into structured Markdown for entity and relationship extraction.
- **Full Snapshot with Forget-on-Delete**: Syncs with `write_disposition="replace"`. Canceled or deleted tasks automatically prune via Cognee's `orphan_cleanup`.
- **Resilient GraphQL Transport**: Automatically handles HTTP 429 rate limits with exponential backoff.

---

## Example Usage