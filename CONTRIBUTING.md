# Contributing to Mehdi's Digital Legacy

Thank you for your interest in contributing to **Mehdi's Digital Legacy**.

This repository serves a dual purpose:
1. **A Personal Writing Archive**: Historical writings are preserved authored by Mehdi Akram. We do not accept unsolicited new articles into the personal author collection.
2. **Open-Source Digital Preservation Platform**: The tools, synchronization scripts, database schemas, static website engine, and backup pipelines are fully open-source and welcome contributions!

## How to Contribute to the Preservation Engine

### Reporting Issues
- If you notice formatting anomalies in converted Markdown articles, broken links, or media download issues, please open an issue on GitHub.
- For bugs in the synchronization engine or static website generator, please provide reproducible steps, operating system details, and Python versions.

### Pull Requests
1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/preservation-improvement`).
3. Ensure Python code adheres to PEP 8 style standards.
4. Run all unit tests before submitting:
   ```bash
   pytest
   python scripts/validate.py
   ```
5. Commit your changes with clear messages (`git commit -m 'Add resilience to media fetcher'`).
6. Push to your branch and submit a Pull Request.

### Development Guidelines
- Zero External Server Dependencies: The archive website must always remain fully static and work without server-side compute.
- Deterministic Output: Serialization of JSON, Markdown, and static assets should be idempotent to avoid noisy Git diffs.
- Unicode & Multilingual First: Full support for the Bengali language (বাংলা) script and English script is mandatory across search, formatting, and file systems.
