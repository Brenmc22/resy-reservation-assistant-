# Reservation Availability Assistant

**Python + Playwright | Browser Automation | Responsible UX**

An educational reservation-availability assistant demonstrating browser navigation, interface inspection, and preferred-time matching.

## Project overview

This project began as a reservation-booking workflow prototype. Its public portfolio edition focuses on the technical and UX principles of finding preferred reservation times while protecting account and payment details. **It does not automatically book or pay for reservations.**

## What it demonstrates

- **Browser automation:** Open a public restaurant page using Playwright and Chromium.
- **DOM inspection:** Collect button labels to identify times visible on the page.
- **Preference matching:** Compare visible labels with a configurable list of preferred times.
- **Input validation:** Accept only public `resy.com` URLs in the example.
- **Privacy by design:** Avoid storing credentials, card details, CVV, cookies, or login sessions.
- **Human confirmation:** Leave any actual reservation decision and submission to the person using the service.

## Technology

- Python 3.10+
- Playwright for Python
- Chromium

## How it works

1. Open a public page in Chromium.
2. Read visible button labels once.
3. Convert preferred times from 24-hour format to 12-hour labels.
4. Display potential matches for manual review.

A matching label does **not** guarantee an available table.

## Run locally

```bash
python -m pip install -r requirements.txt
python -m playwright install chromium
python reservation_assistant.py
```

By default, the script opens the Resy homepage. You can optionally set a public restaurant URL:

```bash
export RESERVATION_URL="https://resy.com/"
python reservation_assistant.py
```

## Privacy and responsible use

This project is for educational purposes and portfolio review. It is not affiliated with or endorsed by Resy. Respect the website's terms and request limits. The script does not repeatedly poll, sign in, enter payment information, or submit reservations. Never commit account profiles, access tokens, session cookies, or payment information.

## Portfolio relevance

The project showcases workflow thinking, automation prototyping, interface parsing, responsible design constraints, and translating a practical user goal into a small, inspectable software tool.
