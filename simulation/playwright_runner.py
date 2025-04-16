from playwright.sync_api import sync_playwright
import time

def run_simulation(url, count):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        for i in range(count):
            try:
                page = browser.new_page()
                page.goto(url, timeout=60000)
                time.sleep(2)
                print(f"Visited {url} ({i + 1}/{count})")
                page.close()
            except Exception as e:
                print(f"Error: {e}")
        browser.close()