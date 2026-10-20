# Connecting Open Scheduling Infrastructure to Agent Memory: Building a Cal.com Connector for Cognee

Executive AI assistants must know what meetings are scheduled, who attendees are, and what event types are available. The Cal.com connector brings calendar bookings directly into Cognee's knowledge graph.

## How It Works
- **Bookings & Attendees**: Ingests upcoming and past meetings, attendee names, emails, and meeting links.
- **Event Types**: Maps available meeting slots, durations, and booking slugs.
- **Document Mode**: Emits `DOCUMENT_SOURCE_ATTR = "calcom"`.

Author: Mallikarjun R (@mallikarjunr444-gif)
