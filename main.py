from playwright.sync_api import sync_playwright
from time import sleep
from dotenv import load_dotenv
import os
from PIL import Image

# Load credentials from .env
load_dotenv("/Users/mateodevos/Code/secrets/.env")
nummer = os.getenv("nummer")
PW = os.getenv("PW")

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
        start_assignment()
        sleep(10)
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

    sleep(3)
    new_page.fill("input[name='wayf_search']", "Petrus")
    new_page.press("input[name='wayf_search']", "Enter")

    sleep(4)
    new_page.fill("input[id='username']", nummer)
    new_page.press("input[id='username']", "Enter")

    sleep(1)
    new_page.fill("input[id='password']", PW)
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
    im = Image.open(r"equation.png")
    left = 0
    top = 0
    right = 850
    bottom = 400
    im1 = im.crop((left, top, right, bottom))
    im1.save("cropped.png")
    


    '''

    elements = page.locator('[class^="packages-bm-toolbox-src-gizmos-formula-Formula-component"]').all()
    print(elements)
    for element in elements:  #proberen? ja. opnieuw?. Pak even de class van een element bij jou. Zullen we alle svg's met if statments doen? nee, eerst text doen ma
        print(element)        #probeer de screenshot even met llama vision. .ik moest even all mijn apps sluiten voor RAM... haha
        print('iets')         #hoe moet ik nu opzoeken hoe ik hem moet prompten
                              # promt: extract the equation from this image. /imagepath
                              #maar die image staat op jouw computer, mischien in dropbox zetten? gedaan
                              #en hoe moet ik hem prompten bedoel ik mee, hoe geef ik hem de imagepath finder -> rightclick -> path ofzo
                              #extract the eqaution form this image /Users/klaas/Library/CloudStorage/Dropb
                                ./Dropbox/Mateo&klaas/cropped.png
                                I don't see an image. Please provide the text of the equation, and I'll be
                                happy to help you extract it.
                                # hij werkt! Dank je well finder yay! Well erg sloom j
                                a

                                The equation in the image is:

10^(-2) = 0.01
10^(-3) = 0.001
10^(-1) = 0.1
10^(0) = 1
10^(1) = 10
10^(2) = 100
10^(3) = 1000

JAAAA dat is goed!
Hoe gaan we die blokjes rond sluren?


mischien kan een 3060 12gb dit sneller Ja, maar AMD werkt ook met Ollama. Dat is wel mooi van ollama. Ja, Ik test het thuis wel zo.  check signal!
afspreken? ja kan wel., 16:15 ben ik thuis.. is 16:30 goed? Kort 2 uurtjes ofzo ja, maar is wel genoeg toch. hoe bedoel je oke? ja donderdag ben ik heel vroeeg uit. Hoe vroeg?


         run? wel lange sleep time asangimeint started. Yes sometimes very slow loading.
        haha I will run again. again. ok
         The page locator works really bad
        mischien xpath of zo iets  ? was dat.
        
        hieronder   \/
    '''
    
'''
class="packages-bm-toolbox-src-gizmos-formula-Formula-components-MToken-tokens__mn--PziAM"
data-testid="mn"
'''

# Start the bot
bot()

#HiHi

#https://pypi.org/project/pytesseract/

'''
packages-bm-toolbox-src-gizmos-formula-Formula-components-MathML__mrow--W6auF packages-bm-toolbox-src-gizmos-formula-Formula-components-MathML__is-top-level--yyFJv
'''