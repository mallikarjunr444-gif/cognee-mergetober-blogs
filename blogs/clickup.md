<!-- Mergetober 2026 Blog Post: ClickUp Integration -->
<!-- Author: Mallikarjun R (@mallikarjunr444-gif) -->
<!-- Pull Request: https://github.com/topoteretes/cognee-community/pull/439 -->
<!-- Issue: https://github.com/topoteretes/cognee/issues/4701 -->

# Supercharging AI Agent Memory: Building a ClickUp Connector for Cognee

Engineering and product teams live in ClickUp. Between sprint backlogs, feature requests, bug trackers, and checklist tasks, a massive amount of organizational context is stored in ClickUp tasks.

For Mergetober, I built the **ClickUp Data-Source Connector** for [Cognee](https://github.com/topoteretes/cognee) to turn any ClickUp workspace into an active knowledge graph for AI companions.

---

## Features
- **Document Mode**: Ingests task titles, descriptions, checklists, and assignees formatted as Markdown (`DOCUMENT_SOURCE_ATTR = "clickup"`).
- **Workspace & Scoped Sync**: Sync across entire workspaces or restrict to specific Space IDs (`space_ids=[...]`) or List IDs (`list_ids=[...]`).
- **Forget-on-Delete**: Full snapshot with `write_disposition="replace"`, ensuring closed, moved, or deleted tasks are cleanly pruned from memory.

---

## Example Usage