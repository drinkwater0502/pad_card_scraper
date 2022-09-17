from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time
import json

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get(f'https://ilmina.com/#/ADVANCED_SEARCH/%7B%22awakeningsSelected%22%3A%7B%220%22%3A61%2C%221%22%3A61%2C%222%22%3A61%7D%7D')

raw_titles = []
no_skill_card_arr = []

try:
    to_find = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@href, '#/CARD')]"))
    )
    time.sleep(5)
    print('found')
    for card in to_find:
        # print(card.get_attribute("title"))
        raw_titles.append(card.get_attribute("title"))
except:
    driver.quit()

def to_dict_no_skill(card_base):
    card_dict_no_skill = {}
    num_name_arr = card_base.split(' - ', 1)
    card_dict_no_skill['card_no'] = num_name_arr[0]
    card_dict_no_skill['card_name'] = num_name_arr[1]
    return card_dict_no_skill

for i in raw_titles:
    no_skill_card_arr.append(to_dict_no_skill(i))

for card_dict in no_skill_card_arr:
    card_num = card_dict['card_no']
    driver.get(f'https://ilmina.com/#/CARD/{card_num}')
    try:
        to_find = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(@data-bind, "html: getActiveSkillDescription()")]'))
        )
        card_dict['Active Skill'] = to_find.text
    except:
        driver.quit()

for card_dict in no_skill_card_arr:
    print(card_dict)

with open('cards.json', 'w') as w:
    json.dump(no_skill_card_arr, w)