from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get(f'https://ilmina.com/#/ADVANCED_SEARCH/%7B%22splitMainSubAttribute%22%3Atrue%2C%22mainAttributes%22%3A%7B%22Light%22%3Atrue%7D%2C%22awakeningsSelected%22%3A%7B%220%22%3A48%2C%221%22%3A48%2C%222%22%3A48%2C%223%22%3A48%7D%7D')

here = ['hi']

try:
    to_find = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@href, '#/CARD')]"))
    )
    time.sleep(5)
    print('found')
    for card in to_find:
        print(card.get_attribute("title"))
except:
    driver.quit()

for i in here:
    print(i)