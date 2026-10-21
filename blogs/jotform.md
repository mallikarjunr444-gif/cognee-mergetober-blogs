# Giving AI Agents Operational Intake Memory: Building a Jotform Connector for Cognee

**Author:** Mallikarjun R (@mallikarjunr444-gif)  
**Target:** `topoteretes/cognee-community`  
**Resolves:** [cognee#5968](https://github.com/topoteretes/cognee/issues/5968)  

## Summary
Adds an official production-ready community data-source connector for Jotform form submissions and operational memory.

- Extracts forms and submissions via official Jotform REST API.
- Resolves question IDs into human-readable field titles.
- Full snapshot with `write_disposition="replace"` for clean forget-on-delete.
- 4/4 pytest passing, 0 Ruff errors, DCO signed.
