from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
PATH = 'C:\Program Files (x86)\chromedriver.exe'

user_card = input('Enter a card number: ')

driver = webdriver.Chrome(PATH)

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