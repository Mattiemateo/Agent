from playwright.sync_api import sync_playwright
from time import sleep
from dotenv import load_dotenv
import os

os.system('cd ../..')

# Load credentials from .env
load_dotenv()
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

# Configuration
HEADLESS = False
TIMEOUT = 30000

path = ""

def bot():
    """Starts the browser and prepares the context and page."""
    global browser, context, page  # Keep them accessible for other functions
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS)
        context = browser.new_context(viewport={"width": 1200, "height": 1000})
        page = context.new_page()
        page.set_default_timeout(TIMEOUT)

        log_in()  # Call login function to start the process
        #sleep(2)
        start_assignment()
        sleep(2.5)
        question_scrape()

        sleep(10000000)  # Keep the browser open

def log_in():
    """Handles the login process."""
    page.goto("https://nl.bettermarks.com/inloggen/")
    print("Waiting for network idle...")

    sleep(3)
    print("Done waiting")

    # Wait for a new tab to open
    with context.expect_page() as new_page_info:
        page.locator("#link_text-595-277").click()
        print("Selected login button")

    global new_page
    new_page = new_page_info.value  # Get the newly opened page
    new_page.bring_to_front()  # Ensure the new tab is active

    print(f"Current URL: {new_page.url}")

    sleep(1)
    new_page.fill("input[name='wayf_search']", "Petrus")
    new_page.press("input[name='wayf_search']", "Enter")

    sleep(4)
    new_page.fill("input[id='username']", USERNAME)
    new_page.press("input[id='username']", "Enter")

    sleep(1)
    new_page.fill("input[id='password']", PASSWORD)
    sleep(1)
    new_page.press("input[id='password']", "Enter")
    
    sleep(2)

    # Navigate to assignments page
    page.goto("https://apps.bettermarks.com/sc/assignments/current")

    sleep(4.5)
    print("Login successful!")
    
def start_assignment():
    new_page.locator(".css-180i3z1").first.click()
    print("Assignment started!")
    
def question_scrape():
    print("scraping questions")
    new_page.screenshot(path="screenshot.png")

    elements = page.locator('[class^="packages-bm-toolbox-src-gizmos-formula-Formula-components-MathML__mrow--W6auF packages-bm-toolbox-src-gizmos-formula-"]').all()
    for element in elements:
        print(element)

# Start the bot
bot()


#https://pypi.org/project/pytesseract/

'''
packages-bm-toolbox-src-gizmos-formula-Formula-components-MathML__mrow--W6auF packages-bm-toolbox-src-gizmos-formula-Formula-components-MathML__is-top-level--yyFJv
'''