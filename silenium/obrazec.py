from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
from selenium.webdriver.common.by import By
import time


driver = webdriver.Edge(r"C:\Users\miron\Desktop\edgedriver_win64\msedgedriver.exe")
driver.get("https://account.mail.ru/login")
element = driver.find_element(By.XPATH,"//input[@name='username']")
element.send_keys("qweewq")
element.send_keys(Keys.ENTER)



#a = mironenko.de@yandex.ru
# yandex.ru -> https://passport.yandex.ru/auth
# xpath -> водишь почту
# есть > пароль/нет  > ну сорян
# если пароль верный > ок / не верный сорян


"""
пригодится
'mail.ru', 'inbox.ru', 'list.ru', 'bk.ru', 'internet.ru' - https://account.mail.ru/login
'yandex.ru','ya.ru' - https://passport.yandex.ru/auth
"""





#суть: человек вводит почту, если такая почта существует/нет его об этом уведомляет программа
#если почта существует предлагает ввести пароль, если подходит/нет программа также уведомляет человека


#словарь с путями !!!
#чтобы если надо было добавить еще домен тебе нужно было просто дописать в словарик пути)
#



#как найти элемент?

#<input type="text" name="passwd" id="passwd-id" />
#element = driver.find_element_by_id("passwd-id")
#element = driver.find_element_by_name("passwd")
#element = driver.find_element_by_xpath("//input[@id='passwd-id']")
#element = driver.find_element_by_xpath("//div[@class="asdasd",text()='текст внутри строчки']")
""" ВСЕ КРОМЕ ID ВЕРНЕТ СПИСОК
find_element_by_id
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector
"""


#ввод
#element.send_keys("some text")
#element.sendKeys(Keys.ENTER)
#driver.findElement(By.id("Value")).sendKeys(Keys.ENTER)


#клик
#element = driver.find_element_by_id("submit")
#element.click()


#вперед назад
#driver.forward()
#driver.back()


#найти значение
#element.get_attribute("value")
#взять текст
#text = driver.find_element_by_class_name("class").getText("my text")



#окна
#driver.switch_to_window("windowName")
#alert = driver.switch_to_alert()


#https://habr.com/ru/post/248559/



