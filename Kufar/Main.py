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

# конфиг
company_list = []
konfig = {'last_path': '',
          'company_list': []}

driver = webdriver.Edge(r"C:\Users\Alex\Desktop\edgedriver_win64\msedgedriver.exe")
path = 'https://www.kufar.by/l/r~minsk-partizanskij?cmp=1&sort=lst.d'
driver.get(path)
while True:
    time.sleep(5)
    element = driver.find_elements(By.XPATH, "//div[@class='styles_cards___qpff']//a[@class='styles_wrapper__yaLfq']")
    print(len(element))
    num_cart = 0
    # Взял один элемент для просмотра перехода с страницы на страницу
    for cart in element[:1]:
        num_cart += 1
        print(num_cart)
        print(cart)
        cart_dict = {}
        cart.click()
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(1)
        name = driver.find_elements(By.XPATH, "//div[@class='styles_seller-block__top-right-name__Uktxe']")[
            0].text
        if name in company_list:
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

        else:
            company_list.append(name)
            cart_dict.setdefault('name', name)
            unp = driver.find_elements(By.XPATH, "//div[@class='styles_seller-block__bottom-business-info__iDaAc']//p")[
                0].text.replace(':', '').split(' ')
            cart_dict.setdefault(unp[0], unp[1])
            driver.get(
                driver.find_elements(By.XPATH, "//div[@data-name='seller-block']//a")[0].get_attribute('href'))
            time.sleep(5)
            driver.find_elements(By.XPATH, "//div[@data-type='shop_about']")[0].click()
            clic_divs = driver.find_elements(By.XPATH, "//div[@class='styles_company-about__content__0kLfb']//div")
            text_info_list = []
            for div in clic_divs:
                try:
                    div.find_elements(By.XPATH, "//p[@class='styles_section__title__L92_l']")[0].click()
                    info_text = div.text.replace('\n', ', ')
                    text_info_list.append(info_text)
                except:
                    pass
            cart_dict.setdefault('info', text_info_list)
            print(cart_dict)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            with open(f'company/{name}.json', 'w', encoding='utf-8') as file:
                json.dump(cart_dict, file, ensure_ascii=False)
            print(company_list)
    try:
        new_path_next = driver.find_elements(By.XPATH, "//div[@class='styles_links__inner__4x5Qj']")
        last_path = new_path_next[0].find_elements(By.XPATH, "//a[@class='styles_link__3MFs4 styles_arrow__r6dv_']")[
            -1].get_attribute('href')
        konfig['last_path'] = last_path
        konfig['company_list'] = company_list
        with open('konfig.json', 'w', encoding='utf-8') as file:
            json.dump(konfig, file, ensure_ascii=False)
        driver.get(last_path)
    except:
        break
