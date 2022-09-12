from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# PATH = 'C:\Program Files (x86)\chromedriver.exe'

# driver = webdriver.Chrome(PATH)

CHROME_PATH = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
CHROMEDRIVER_PATH = 'C:\Program Files (x86)\chromedriver.exe'
WINDOW_SIZE = "1920,1080"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.binary_location = CHROME_PATH

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options, service=Service(ChromeDriverManager().install()))

user_card = input('Enter a card number: ')

driver.get(f'https://ilmina.com/#/CARD/{user_card}')

card_data = []


stuff = ["card-title-name", "card-title-no"]
for i in stuff:
    try:
        to_find = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, i))
        )
        card_data.append(to_find.text)
    except:
        driver.quit()

try:
    to_find = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[contains(@data-bind, "html: getActiveSkillDescription()")]'))
    )
    card_data.append(to_find.text)
except:
    driver.quit()

for i in card_data:
    print(i)