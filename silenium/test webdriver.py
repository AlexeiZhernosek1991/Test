from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
from selenium.webdriver.common.by import By
import time

hosts = {'mail': {'domains': ('mail.ru', 'inbox.ru', 'list.ru', 'bk.ru', 'interne3t.ru',),
                  'login_page': 'https://account.mail.ru/login',
                  'input_xpath': "//input[@name='username']",
                  'success_xpath': "//input[@name='password']",
                  'success': "//div[@class='portal-menu']", },

         'yandex': {'domains': ('yandex.ru',),
                    'login_page': 'https://passport.yandex.ru/auth',
                    'input_xpath': "//input[@name='login']",
                    'success_xpath': "//input[@name='passwd']",
                    'success': "//div[@class='Header_navigationScroll__MNM5b']", }}

driver = webdriver.Edge(r"C:\Users\Alex\Desktop\edgedriver_win64\msedgedriver.exe")
email = input('введите email: ')
domen = email.split('@')[1]
for i, b in hosts.items():
    if domen in b['domains']:
        driver.get(b['login_page'])
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, b['input_xpath'])))
        element.send_keys(email)
        try:
            element.send_keys(Keys.ENTER)
            try:
                password_send = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, b['success_xpath'])))
                password = input('введите пароль: ')
                password_send.send_keys(password)
                password_send.send_keys(Keys.ENTER)
                a = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, b['success'])))
                print('Вы авторизовались')
            except:
                print('Пароль не верный')
        except:
            print('Такого логина не существует')
        print('Спасибо что воспользовались нашей программой ')
    else:
        pass

list_ = []
path = "scknfpsjnpfviaebrgvgi"
num_str = 1
driver.get(path)
while True:
    try:
        # СОБРАТЬ ВСЕ ССЫЛКИ >>> список
        # СОХРАНИТЬ list_.extend()
        print(f"отработала {num_str} сираница")
        num_str += 1
        # код прехода на следующую страницу path__
        driver.get(path__)
    except:
        print('конец страниц')
        break
print(list_)
for path_1 in list_:
    driver.get(path_1)
