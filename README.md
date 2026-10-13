# resy-reservation-assistant-# Reservation Availability Assistant

An educational **Python + Playwright** browser-automation project exploring reservation discovery, interface inspection, and time-preference matching.

## Overview

This project began as a reservation-booking workflow prototype. The public portfolio edition demonstrates the core technical ideas without storing personal information, payment credentials, or authenticated sessions. It **does not automatically book reservations**.

## What it demonstrates

- Browser navigation and DOM inspection with Playwright
- Matching preferred times against visible button labels
- Basic input validation and error-safe browser cleanup
- Separation of configuration from code using an environment variable
- Privacy-aware design: no CVV entry, saved browser profile, or checkout submission

## Getting started

Requires Python 3.10+.

```bash
python -m pip install -r requirements.txt
python -m playwright install chromium
python reservation_assistant.py
```

By default the script opens Resy's public homepage once. To inspect a specific public restaurant page, set `RESERVATION_URL` in your shell before running. Only public `resy.com` URLs are accepted.

## How it works

1. Open a public page in Chromium.
2. Read visible button labels from the current page snapshot.
3. Compare them against configured preferred times.
4. Print possible matches for manual review.

A match is **not** confirmation that a table is available. Actual booking, if permitted, must be performed manually through the service.

## Responsible use

This repository is for education and portfolio review. It is not affiliated with or endorsed by Resy. Respect the site's terms, access controls, and request limits. Do not commit login profiles, session cookies, payment information, or private account details.

## Portfolio context

The project showcases workflow modeling, Python scripting, browser interaction, and consideration of privacy and human confirmation in automated experiences.
