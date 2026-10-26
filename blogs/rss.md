# Ingesting the Real-Time Web: Building an RSS & Atom Feeds Connector for Cognee

**Author:** Mallikarjun R (@mallikarjunr444-gif)  
**Hackathon:** Mergetober 2026 (WeMakeDevs x Cognee)  
**Resolves:** [topoteretes/cognee#4804](https://github.com/topoteretes/cognee/issues/4804)  
**Live Article:** [https://mallikarjunr444-gif.github.io/cognee-mergetober-blogs/blogs/rss.html](https://mallikarjunr444-gif.github.io/cognee-mergetober-blogs/blogs/rss.html)

## Summary
Implements a production-ready community data-source connector for RSS and Atom syndication feeds under `packages/connector/rss/` in `cognee-community`.

### Key Features
- Supports both RSS 2.0 (`<item>`) and Atom 1.0 (`<entry>`) feeds.
- Zero extra dependencies, leveraging Python standard library `xml.etree.ElementTree`.
- Routes articles through `DOCUMENT_SOURCE_ATTR = "rss"` for cognitive graph extraction.
- Incremental syncing via publication timestamps.
- 4/4 passing unit tests with mock feeds.
- 100% Ruff lint and format clean, DCO signed.
