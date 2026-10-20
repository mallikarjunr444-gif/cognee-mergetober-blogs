# Financial Transactions in Agent Memory: Building a Stripe Connector for Cognee

Financial and billing context is essential for revenue operations and customer support copilots. Without real-time access to customer subscriptions and charges, AI agents cannot answer critical account status questions.

During Mergetober 2026, I built the **Stripe Data-Source Connector** for [Cognee](https://github.com/topoteretes/cognee).

## How It Works
- **Charge Ingestion**: Ingests charge amounts, currencies, customer IDs, and payment status into Cognee's knowledge graph.
- **Subscription Tracking**: Ingests active subscriptions, billing period intervals, and renewal status.
- **Document Mode**: Emits `DOCUMENT_SOURCE_ATTR = "stripe"`.
- **Automatic Backoff**: Retries automatically on HTTP 429 rate limits.

Author: Mallikarjun R (@mallikarjunr444-gif)
