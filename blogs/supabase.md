# Relational Postgres as Cognitive Memory: Building a Supabase Connector for Cognee

Modern applications store critical business records—user profiles, transactions, tenant configs, and inventory—in Supabase (PostgreSQL). By providing AI agents with direct access to Supabase tables, they can reason about structured relational state without manual SQL exports.

During Mergetober 2026, I built the **Supabase Data-Source Connector** for [Cognee](https://github.com/topoteretes/cognee).

## How It Works
- **PostgREST Table Ingestion**: Connects to the Supabase REST API endpoint to extract rows with pagination support.
- **Cognitive Document Mode**: Emits `DOCUMENT_SOURCE_ATTR = "supabase"`.
- **Automatic Backoff**: Retries automatically on transient HTTP errors and rate limits.

Author: Mallikarjun R (@mallikarjunr444-gif)
