import gspread
from bs4 import BeautifulSoup
import time
import requests
from requests import get

url = 'https://afisha.relax.by/kino/minsk/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

# shed_list = soup.find_all("div", class_="schedule__list")
cinema_name = ''
date_film_list = []
row_list = []
for shed_list in soup.find_all("div", class_="schedule__list"):
    date_ = shed_list.find("h5").text.strip().replace("  ", "").replace("\n", "")
    date_ = date_[:date_.find(",")].replace("марта", " 3").replace("апреля", " 4").replace("мая", " 5")
    films = shed_list.find_all("div", class_="schedule__table--movie__item")
    for film in films:
        row_list = []
        # Получаем название фильма
        try:
            name_film = film.find("a", class_="schedule__event-link link").text.strip().replace("  ", "")
            row_list.append(name_film)
        except:
            pass
        # Получаем название кинотеатра
        try:
            cinema_name = film.find("a", class_="schedule__place-link link").text.strip().replace("  ", "")
            row_list.append(cinema_name)
        except:
            row_list.append(cinema_name)
        # Получаем время сеансов
        try:
            time_film = film.find_all("div", class_="schedule__seance-wrap")
            seans_time = []
            for time_ in time_film:
                time_ = time_.text.replace(' ', '').replace('\n', '')
                time_ = time_[:5]
                time_ = time_ + ' ' + date_ + ' 2023'
                time_ = time.strptime(time_, '%H:%M %d %m %Y')
                time_ = time.mktime(time_)
                seans_time.append(time_)
            row_list.append(str(seans_time))
        except:
            pass
        # Получаем ссылку на фильм
        try:
            hhh_film = film.find("a", class_="schedule__event-link link").get("href")
            row_list.append(hhh_film)
        except:
            pass
        # Добавляем строку в список
        try:
            date_film_list.append(row_list)
        except:
            pass

print(date_film_list[0])
date_film_list2 = []
for url in set([x[-1] for x in date_film_list]):
    row_list2 = []
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    # Получаем название фильма
    try:
        name_film = soup.find("h1", class_="b-afisha-layout-theater_movie-title").text.strip().replace("  ", "")
        row_list2.append(name_film)
    except:
        pass
    # Получаем описание фильма
    try:
        description_film = soup.find("div", class_="b-afisha_cinema_description_text").find_all("p")
        text_description_fil = ''
        for text_ in description_film:
            text_description_fil += text_.text.strip().replace("  ", "")
        row_list2.append(text_description_fil)
    except:
        pass
    # Получаем оригинальное название фильма
    try:
        all_info = soup.find("div", class_="b-ps-features").find_all("li")
        if len(all_info) < 8:
            row_list2.append(' ')
        else:
            pass
        for info in all_info:
            info_list = info.find_all("span")
            text_info = ''
            for info_ in info_list:
                text_info += info_.text.strip().replace("  ", "").replace('\t', '')
            row_list2.append(text_info)
    except:
        pass
    date_film_list2.append(row_list2)

print(date_film_list2[0])

gc = gspread.service_account(filename="credentials.json")
# авторизуемся


sht2 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1XhJFGQNSMg7-9z7PeaojIZ-J4NYfuiJ8GI1uCMMj9TM/edit#gid=0')
# законнектились с табличкой


worksheet = sht2.get_worksheet(0)
# worksheet - объект первого листа (снизу поиск по индексу и имени)

print(len(date_film_list))
worksheet.update('A1:Z' + str(len(date_film_list)), date_film_list)

worksheet2 = sht2.get_worksheet(1)
worksheet2.update('A1:Z' + str(len(date_film_list2)), date_film_list2)
# изменяем значения листа на 2хмерный список (list_of_lists)

# worksheet = sh.worksheet("Январь")
