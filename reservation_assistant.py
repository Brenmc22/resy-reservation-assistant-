"""Educational reservation availability assistant.

No payment details are collected, no booking is submitted, and no login
session is included in the repository. Respect website terms and rate limits.
"""
import os
from datetime import datetime
from urllib.parse import urlparse
from playwright.sync_api import sync_playwright

# Set a restaurant's public page URL locally; do not commit personal account links.
TARGET_URL = os.getenv('RESERVATION_URL', 'https://resy.com/')
PREFERRED_TIMES = ['19:00', '19:30', '20:00']
HEADLESS = False


def preferred_labels(times):
    """Convert 24-hour preferred times into visible 12-hour labels."""
    labels = []
    for value in times:
        labels.append(datetime.strptime(value, '%H:%M').strftime('%I:%M %p').lstrip('0'))
    return labels


def find_matching_times(button_texts, preferred_times):
    """Return preferred times visible in the supplied button labels."""
    labels = preferred_labels(preferred_times)
    return [label for label in labels if any(label.lower() in text.lower() for text in button_texts)]


def run():
    if urlparse(TARGET_URL).hostname not in {'resy.com', 'www.resy.com'}:
        raise ValueError('Only public resy.com URLs are accepted in this example.')

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=HEADLESS)
        page = browser.new_page(viewport={'width': 1280, 'height': 800})
        try:
            page.goto(TARGET_URL, wait_until='domcontentloaded', timeout=30000)
            button_texts = page.locator('button').all_inner_texts()
            matches = find_matching_times(button_texts, PREFERRED_TIMES)
            if matches:
                print('Potential matching time(s): ' + ', '.join(matches))
                print('Review availability and complete any reservation manually in your browser.')
            else:
                print('No preferred time labels found in this page snapshot.')
            print('This script does not log in, reserve, pay, or repeatedly refresh.')
        finally:
            browser.close()


if __name__ == '__main__':
    run()
