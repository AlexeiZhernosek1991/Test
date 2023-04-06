import os

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import selenium.common.exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import requests
from requests import get
import ssl
import urllib.request
import json
from bs4 import BeautifulSoup

company_list = os.listdir('company')
all_cart_list = set()
driver = webdriver.Edge(r"C:\Users\Alex\Desktop\edgedriver_win64\msedgedriver.exe")
path = 'https://www.kufar.by/l/r~minsk-partizanskij?cmp=1&sort=lst.d'
num_str = 1
driver.get(path)
time.sleep(1)
all_str = driver.find_elements(By.XPATH, "//a[@class='styles_link__3MFs4']")[-1].text
print(all_str)
while True:
    if all_str == driver.find_elements(By.XPATH, "//a[@class='styles_link__3MFs4']")[-1].text:
        print(f'парсинг {num_str} страницы')
        page = requests.get(path)
        soup = BeautifulSoup(page.text, 'html.parser')
        cart_list = [x.get('href') for x in soup.find_all("a", class_="styles_wrapper__yaLfq")]
        all_cart_list = all_cart_list.union(set(cart_list))
        print(f'конец парсинга {num_str} страницы')
        driver.get(path)
        time.sleep(1)
        path = driver.find_elements(By.XPATH, "//a[@class='styles_link__3MFs4 styles_arrow__r6dv_']")[-1].get_attribute(
            'href')
        num_str += 1
    else:
        break
with open(f'konfig.json', 'w', encoding='utf-8') as file:
    json.dump(list(all_cart_list), file, ensure_ascii=False)
with open(f'konfig.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
all_cart_list = data
num_cart = 0
for cart_path in all_cart_list:
    cart_dict = {}
    num_cart += 1
    print(f'обрабатывается {num_cart} карточка')
    driver.get(cart_path)
    name = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='styles_seller-block__top-right-name__Uktxe']"))).text
    if f'{name}.json' in company_list:
        print('такая компания есть')
        pass
    else:
        company_list.append(name)
        cart_dict.setdefault('name', name)
        unp = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='styles_seller-block__bottom-business-info__iDaAc']//p"))).text.replace(':',
                                                                                                                 '').split(
            ' ')
        cart_dict.setdefault(unp[0], unp[1])
        driver.get(WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@data-name='seller-block']//a"))).get_attribute('href'))
        text_info_list = []
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@data-type='shop_about']"))).click()
            clic_divs = driver.find_elements(By.XPATH, "//div[@class='styles_company-about__content__0kLfb']//div")
            for div in clic_divs:
                try:
                    div.find_elements(By.XPATH, "//p[@class='styles_section__title__L92_l']")[0].click()
                    info_text = div.text.replace('\n', ', ')
                    text_info_list.append(info_text)
                    cart_dict.setdefault('info', text_info_list)
                    with open(f'company/{name}.json', 'w', encoding='utf-8') as file:
                        json.dump(cart_dict, file, ensure_ascii=False)
                except:
                    pass
        except:
            try:
                WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, "//div[@class='styles_tab__5xOlg']"))).click()
                info_text = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, "//div[@class='styles_tabs_body__XjKa9']"))).text.replace(
                    '\n', '')
                text_info_list.append(info_text)
                cart_dict.setdefault('info', text_info_list)
                with open(f'company/{name}.json', 'w', encoding='utf-8') as file:
                    json.dump(cart_dict, file, ensure_ascii=False)
            except:
                path_error = []
                with open(f'path.json', 'r+', encoding='utf-8') as file:
                    try:
                        path_error = json.load(file)
                    except:
                        pass
                    list(path_error).append(cart_path)
                    json.dump(path_error, file, ensure_ascii=False)
                pass

# except:
#     print('парсинг закончен')
#     break
# print(all_cart_list[0][:2], all_cart_list[1][:2], all_cart_list[2][:2], all_cart_list[3][:2], all_cart_list[4][:2])
