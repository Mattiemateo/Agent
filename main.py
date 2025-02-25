from playwright.sync_api import sync_playwright
import time
import threading

Headless = False
timeout = 30000

def log_in():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=Headless)
        context = browser.new_context(viewport={"width": 800, "height": 600})
        
        page = context.new_page()
        page.set_default_timeout(timeout)
        # Visit Blooket
        page.goto("https://play.blooket.com/play")

        print("waiting networkidle")

        # Wait for the page to load
        page.wait_for_load_state("networkidle")
        
        time.sleep(100000)


log_in()