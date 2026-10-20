# Developer Sentiment & Tech Trend Memory: Building a Hacker News Connector for Cognee

Hacker News is the pulse of the tech industry. By piping top stories and Ask HN discussions into Cognee, agents can stay updated on emerging technologies, community sentiment, and breaking announcements.

## How It Works
- **Zero-Auth Access**: Queries the official Hacker News Firebase REST API directly.
- **Top Stories & Ask HN**: Ingests titles, scores, authors, comments, and external URLs into graph memory.
- **Document Mode**: Emits `DOCUMENT_SOURCE_ATTR = "hackernews"`.

Author: Mallikarjun R (@mallikarjunr444-gif)
