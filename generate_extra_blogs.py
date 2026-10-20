import os
import re

extra_articles = [
    {
        "slug": "resend",
        "name": "Resend",
        "title": "Transactional Email as Continuous Context: Building a Resend Connector for Cognee",
        "pr": "https://github.com/mallikarjunr444-gif/cognee-community/tree/feature/resend-connector",
        "issue": "https://github.com/topoteretes/cognee/issues/6087",
        "content": """# Transactional Email as Continuous Context: Building a Resend Connector for Cognee

Customer interactions frequently happen over transactional emails—order receipts, password resets, onboarding tips, and notifications. For AI assistants, having access to these emails means knowing exactly what communications a customer has already received.

During Mergetober 2026, I built the **Resend Data-Source Connector** for [Cognee](https://github.com/topoteretes/cognee).

## How It Works
- **Sent Email Ingestion**: Extracts recipient, sender, subject, delivery status, and full HTML/text content.
- **Audience & Contact Tracking**: Ingests audience segments and subscriber counts into Cognee's cognitive graph.
- **Document Mode**: Emits `DOCUMENT_SOURCE_ATTR = "resend"` so Cognee extracts entities and relationships.
- **Resilient Transport**: Automatic retry on HTTP 429 rate limit responses with backoff.

Author: Mallikarjun R (@mallikarjunr444-gif)
"""
    },
    {
        "slug": "plausible",
        "name": "Plausible",
        "title": "Privacy-Preserving Web Analytics in Long-Term Memory: Building a Plausible Connector for Cognee",
        "pr": "https://github.com/mallikarjunr444-gif/cognee-community/tree/feature/plausible-connector",
        "issue": "https://github.com/topoteretes/cognee/issues/6093",
        "content": """# Privacy-Preserving Web Analytics in Long-Term Memory: Building a Plausible Connector for Cognee

Plausible Analytics provides clean, lightweight web analytics without tracking personal data. By feeding Plausible metrics into Cognee's knowledge graph, marketing and product agents can recall site performance, top pages, and traffic referrals.

## How It Works
- **Aggregate Metrics**: Ingests 30-day visitors, pageviews, bounce rates, and visit duration.
- **Breakdown Tracking**: Ingests top pages (`event:page`) and referrers (`visit:source`).
- **Realtime Traffic**: Ingests active visitor counts for instant reasoning.
- **Document Mode**: Emits `DOCUMENT_SOURCE_ATTR = "plausible"`.

Author: Mallikarjun R (@mallikarjunr444-gif)
"""
    },
    {
        "slug": "calcom",
        "name": "Cal.com",
        "title": "Connecting Open Scheduling Infrastructure to Agent Memory: Building a Cal.com Connector for Cognee",
        "pr": "https://github.com/mallikarjunr444-gif/cognee-community/tree/feature/calcom-connector",
        "issue": "https://github.com/topoteretes/cognee/issues/4816",
        "content": """# Connecting Open Scheduling Infrastructure to Agent Memory: Building a Cal.com Connector for Cognee

Executive AI assistants must know what meetings are scheduled, who attendees are, and what event types are available. The Cal.com connector brings calendar bookings directly into Cognee's knowledge graph.

## How It Works
- **Bookings & Attendees**: Ingests upcoming and past meetings, attendee names, emails, and meeting links.
- **Event Types**: Maps available meeting slots, durations, and booking slugs.
- **Document Mode**: Emits `DOCUMENT_SOURCE_ATTR = "calcom"`.

Author: Mallikarjun R (@mallikarjunr444-gif)
"""
    },
    {
        "slug": "hackernews",
        "name": "Hacker News",
        "title": "Developer Sentiment & Tech Trend Memory: Building a Hacker News Connector for Cognee",
        "pr": "https://github.com/mallikarjunr444-gif/cognee-community/tree/feature/hackernews-connector",
        "issue": "https://github.com/topoteretes/cognee/issues/4805",
        "content": """# Developer Sentiment & Tech Trend Memory: Building a Hacker News Connector for Cognee

Hacker News is the pulse of the tech industry. By piping top stories and Ask HN discussions into Cognee, agents can stay updated on emerging technologies, community sentiment, and breaking announcements.

## How It Works
- **Zero-Auth Access**: Queries the official Hacker News Firebase REST API directly.
- **Top Stories & Ask HN**: Ingests titles, scores, authors, comments, and external URLs into graph memory.
- **Document Mode**: Emits `DOCUMENT_SOURCE_ATTR = "hackernews"`.

Author: Mallikarjun R (@mallikarjunr444-gif)
"""
    }
]

blogs_dir = "/Users/malikarjunr/.gemini/antigravity-ide/scratch/cognee-mergetober-blogs/blogs"

for a in extra_articles:
    md_path = os.path.join(blogs_dir, f"{a['slug']}.md")
    with open(md_path, "w") as f:
        f.write(a["content"])
    print(f"Wrote {md_path}")
