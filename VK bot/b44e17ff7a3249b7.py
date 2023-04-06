from vk_api import VkApi
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import json
import array
import gspread

GROUP_ID = '219364665'
GROUP_TOKEN = 'vk1.a.Udr_3z5uGE0H0VcDsiUrnxXt8YXuiYaQZPdLIYC1YrzbFTxRZvvelbhTEFiB0-0cdRJ21Xy2M31lVbaXR3HWI0AWBQz74S0p8cjDs1A2BM6DGzIcirs90Jw0kyp2sbFuDkecVixcmfEY4FbN01pD7MR6520v-GN5Zfzm8GpP4xbaDPsC7IBlszgiaLxLo65XLAzAAp4Efm-tBI-N4n9mbQ'
API_VERSION = '5.120'
Nullm = []
Mass_of_c = []


def statreset():
    Mass_of_c = Nullm
    i = 0
    x = 1
    while i < LLL:
        Mass_of_c.append(x)
        i = i + 1
    return Mass_of_c


def text_stat(m):
    i = 0
    l = len(m) - 1
    text = ""
    while i < l:
        text = text + str(m[i]) + " " + list_of_lists[i][0] + "\n"
        i = i + 1
    return text


Statist1 = []
Statist1.append(10)
Statist2 = 0


def massel(mass, ind):
    q = 0
    i = 0
    j = len(mass) - 1
    while i < j:
        if mass[i] == ind:
            q = 1
        i = i + 1
    if q == 0:
        mass.append(ind)
    return mass


gc = gspread.service_account(filename="credentials.json")
sht2 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1Ce5d0HTVVaY6A41SREJDa4yN4lJGYRRL0N1r_CvLsKs/edit#gid=0')
worksheet = sht2.sheet1
list_of_lists = worksheet.get_all_values()
LLL = (len(list_of_lists)) - 1

Mass_of_c = statreset()

CALLBACK_TYPES = ('show_snackbar', 'open_link', 'open_app', 'text')

# Запускаем бот
vk_session = VkApi(token=GROUP_TOKEN, api_version=API_VERSION)
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, group_id=GROUP_ID)

settings = dict(one_time=False, inline=False)
settings2 = dict(one_time=False, inline=True)

# Основное меню
keyboard_1 = VkKeyboard(**settings)

keyboard_1.add_callback_button(label='Таблица со всеми промокодами!', color=VkKeyboardColor.POSITIVE,
                               payload={"type": "open_link",
                                        "link": "https://docs.google.com/spreadsheets/d/1FhYGE5IODqbtXSfQGBs0BGUaUJYAWBGAC2SRWqYzf6M"})
keyboard_1.add_line()

keyboard_1.add_button(label='Запустить бота!', color=VkKeyboardColor.NEGATIVE, payload={"type": "text"})
keyboard_1.add_line()

keyboard_1.add_callback_button(label='Мы в Телеграме!', color=VkKeyboardColor.PRIMARY,
                               payload={"type": "open_link", "link": "https://t.me/skidkinezagorami"})

keyboard_3 = VkKeyboard(**settings)

keyboard_3.add_callback_button(label='Таблица со всеми промокодами!', color=VkKeyboardColor.POSITIVE,
                               payload={"type": "open_link",
                                        "link": "https://docs.google.com/spreadsheets/d/1FhYGE5IODqbtXSfQGBs0BGUaUJYAWBGAC2SRWqYzf6M"})
keyboard_3.add_line()

keyboard_3.add_button(label='Меню!', color=VkKeyboardColor.NEGATIVE, payload={"type": "text"})
keyboard_3.add_line()

keyboard_3.add_callback_button(label='Мы в Телеграме!', color=VkKeyboardColor.PRIMARY,
                               payload={"type": "open_link", "link": "https://t.me/skidkinezagorami"})

keyboard_menu_1 = VkKeyboard(**settings2)
keyboard_menu_2 = VkKeyboard(**settings2)
keyboard_menu_3 = VkKeyboard(**settings2)


# ген

def K_G(s):
    keyboard_2 = VkKeyboard(**settings2)
    keyboard_2.add_button(label=case, color=VkKeyboardColor.PRIMARY, payload={"type": "text"})
    keyboard_2.add.line()
    keyboard_2.add_button(label="Меню!", color=VkKeyboardColor.POSITIVE, payload={"type": "text"})
    return keyboard_2


# stat

keyboard_2 = VkKeyboard(**settings2)
keyboard_2.add_button(label="Меню!", color=VkKeyboardColor.PRIMARY, payload={"type": "text"})

keyboard_menu_1.add_button(label="Маркетплейс", color=VkKeyboardColor.SECONDARY, payload={"type": "text"})
keyboard_menu_1.add_line()
keyboard_menu_1.add_button(label="Бонусы от банков", color=VkKeyboardColor.SECONDARY, payload={"type": "text"})
keyboard_menu_1.add_line()
keyboard_menu_1.add_button(label="Доставка/продукты", color=VkKeyboardColor.SECONDARY, payload={"type": "text"})
keyboard_menu_1.add_line()
keyboard_menu_1.add_button(label="Аптеки/здоровье", color=VkKeyboardColor.SECONDARY, payload={"type": "text"})
keyboard_menu_1.add_line()
keyboard_menu_1.add_button(label="Кафе/Рестораны", color=VkKeyboardColor.SECONDARY, payload={"type": "text"})
keyboard_menu_1.add_line()
keyboard_menu_1.add_callback_button(label='Далее', color=VkKeyboardColor.PRIMARY, payload={"type": "2"})

keyboard_menu_2.add_button(label="Онлайн сервис/подписка", color=VkKeyboardColor.SECONDARY, payload={"type": "text"})
keyboard_menu_2.add_line()
keyboard_menu_2.add_button(label="Жилье", color=VkKeyboardColor.SECONDARY, payload={"type": "text"})
keyboard_menu_2.add_line()
keyboard_menu_2.add_button(label="Такси", color=VkKeyboardColor.SECONDARY, payload={"type": "text"})
keyboard_menu_2.add_line()
keyboard_menu_2.add_button(label="Обувь/одежда", color=VkKeyboardColor.SECONDARY, payload={"type": "text"})
keyboard_menu_2.add_line()
keyboard_menu_2.add_button(label="Косметика/парфюмерия", color=VkKeyboardColor.SECONDARY, payload={"type": "text"})
keyboard_menu_2.add_line()
keyboard_menu_2.add_callback_button(label='Назад', color=VkKeyboardColor.PRIMARY, payload={"type": "1"})
keyboard_menu_2.add_callback_button(label='Далее', color=VkKeyboardColor.PRIMARY, payload={"type": "3"})

keyboard_menu_3.add_button(label="Страхование", color=VkKeyboardColor.SECONDARY, payload={"type": "text"})
keyboard_menu_3.add_line()
keyboard_menu_3.add_button(label="Услуги", color=VkKeyboardColor.SECONDARY, payload={"type": "text"})
keyboard_menu_3.add_line()
keyboard_menu_3.add_callback_button(label='Назад', color=VkKeyboardColor.PRIMARY, payload={"type": "2"})


def texting2(st, object_, num):
    i = 0
    global Mass_of_c

    text1 = """"""
    while i < LLL:

        i = i + 1
        if list_of_lists[i][9] != None:
            if list_of_lists[i][0] == st:
                Mass_of_c[i] = Mass_of_c[i] + 1
                text = ""
                if list_of_lists[i][0] != None:
                    text = text + "Название: " + "*" + list_of_lists[i][0] + "*"

                if list_of_lists[i][3] != None:
                    text = text + ("\nСкидка: " + list_of_lists[i][3])

                if list_of_lists[i][7] != None:
                    text = text + ("\nОписание: " + list_of_lists[i][7])

                if list_of_lists[i][5] != None:
                    text = text + ("\nДействует до: " + list_of_lists[i][5])

                if list_of_lists[i][6] != None:
                    text = text + ("\nРегион: " + list_of_lists[i][6])

                if list_of_lists[i][4] != None:
                    text = text + ("\nСсылка: \n" + list_of_lists[i][4])

                if list_of_lists[i][2] != None and list_of_lists[i][2] != "":
                    text = text + ("\nПромокод ниже👇")
                    bottext(text, object_)
                    text = list_of_lists[i][2]
                    bottext(text, object_)
                else:
                    text = text + ("\nДействует только по ссылке")
                    bottext(text, object_)
    bottext2("Куда отправимся за скидками дальше?", object_, num)


def punctGen():
    i = 0
    # j = 0

    mark_list = []
    text = ""
    next_s = "\n"
    while i < LLL:
        i = i + 1
        if list_of_lists[i][0] != None:
            if list_of_lists[i][0] != "":
                mark_list.append(list_of_lists[i][0])

    return mark_list


def unicF(mass=[]):
    temp = []
    for x in mass:
        if x not in temp:
            temp.append(x)
    return temp


text_inst = """
1. Для начала работы нажмите : "запустить бота"
2. Выберите нужную Вам  категорию, если не нашли на первой странице, нажмите : "далее"
Затем введите номер нужной услуги и отправьте сообщением боту. 
3. Также вы всегда можете найти актуальный перечень всех акций и предложений нажав кнопку : "таблица со всеми промокодами"
4. Чтобы всегда оставаться на связи, подпишитесь на нас в телеграмм канале, нажав кнопку : "Мы в Телеграме"
"""


def bottext(case, obj):
    vk.messages.send(
        user_id=obj['from_id'],
        random_id=get_random_id(),
        peer_id=obj['from_id'],

        message=case

    )


def bottext2(case, obj, num):
    keyboard_menu_0 = VkKeyboard(**settings2)
    keyboard_menu_0.add_button(label=SSS[num], color=VkKeyboardColor.SECONDARY, payload={"type": "text"})
    keyboard_menu_0.add_line()
    keyboard_menu_0.add_button(label="Меню!", color=VkKeyboardColor.PRIMARY, payload={"type": "text"})
    vk.messages.send(
        user_id=obj['from_id'],
        random_id=get_random_id(),
        peer_id=obj['from_id'],
        keyboard=keyboard_menu_0.get_keyboard(),
        message=case

    )


def marking():
    i = 0
    # j = 0

    mark_list = []
    text = ""
    next_s = "\n"
    while i < LLL:
        i = i + 1
        if list_of_lists[i][8] != None:
            if list_of_lists[i][8] != "":
                mark_list.append(list_of_lists[i][8])

    temp = []
    for x in mark_list:
        if x not in temp:
            temp.append(x)
    mark_list = temp

    return mark_list


# Список категорий
List_of_M = marking()

# список пунктов
List_of_P = punctGen()

# список уникальных пунктов
List_of_U_P = unicF(List_of_P)


# массив категорий к пунктам

def S(mass=[]):
    mark = []
    i = 0
    j = 0
    L = len(mass) - 1
    while i < L:
        while j < LLL:
            if mass[i] == list_of_lists[j][0]:
                mark.append(list_of_lists[j][8])
                break
            j = j + 1
        i = i + 1

    return mark


SSS = S(List_of_U_P)


def T0(case):
    # case атегория
    text = ""
    text = text + "Наберите номер магазина!"
    i = 0
    while i < (len(List_of_U_P) - 1):
        if SSS[i] == case:
            text = text + "\n" + str(i) + ". " + List_of_U_P[i]
        i = i + 1
    return text


HI = []
HI.append("start")
HI.append("Start")
HI.append("начать")
HI.append("Начало")
HI.append("Начать")
HI.append("начало")
HI.append("Бот")
HI.append("бот")
HI.append("Старт")
HI.append("старт")
HI.append("скидки")
HI.append("Скидки")

print("Ready")

for event in longpoll.listen():

    if event.type == VkBotEventType.MESSAGE_NEW:

        if event.obj.message['text'] != '':

            if event.from_user:

                if event.obj.message['text'] == 'Запустить бота!' or event.obj.message['text'] == "Меню!":

                    Statist1 = massel(Statist1, event.obj.message['from_id'])
                    vk.messages.send(
                        user_id=event.obj.message['from_id'],
                        random_id=get_random_id(),
                        peer_id=event.obj.message['from_id'],
                        keyboard=keyboard_menu_1.get_keyboard(),
                        message='Выбирай категорию (1)')

                elif event.obj.message['text'] == 'Инструкция!':
                    vk.messages.send(
                        user_id=event.obj.message['from_id'],
                        random_id=get_random_id(),
                        peer_id=event.obj.message['from_id'],
                        keyboard=keyboard_1.get_keyboard(),
                        message=text_inst)

                elif event.obj.message['text'] == '/stat1':
                    vk.messages.send(
                        user_id=event.obj.message['from_id'],
                        random_id=get_random_id(),
                        peer_id=event.obj.message['from_id'],
                        message="Количество вызовов функций = " + str(Statist2))

                elif event.obj.message['text'] == '/stat2':

                    vk.messages.send(
                        user_id=event.obj.message['from_id'],
                        random_id=get_random_id(),
                        peer_id=event.obj.message['from_id'],
                        message="Людей активно использующих бота = " + str(int(len(Statist1) / 2)))

                elif event.obj.message['text'] == '/stat3':

                    vk.messages.send(
                        user_id=event.obj.message['from_id'],
                        random_id=get_random_id(),
                        peer_id=event.obj.message['from_id'],
                        message="Детальная статистика: " + "\n" + text_stat(Mass_of_c))

                elif event.obj.message['text'] in HI:
                    vk.messages.send(
                        user_id=event.obj.message['from_id'],
                        random_id=get_random_id(),
                        peer_id=event.obj.message['from_id'],
                        keyboard=keyboard_1.get_keyboard(),
                        message="Привет-привет, я готов тебе помочь со скидками!\nНажми 'Запустить бота!' \nЕсли клавиатура свернута, нажми на 4 точки в правом нижнем углу!")

                else:
                    if event.obj.message['text'].isdigit():

                        print("num")
                        if int(event.obj.message['text']) < (len(List_of_U_P) - 1):
                            Statist2 = Statist2 + 1
                            str1 = List_of_U_P[int(event.obj.message['text'])]
                            num = int(event.obj.message['text'])
                            texting2(str1, event.obj.message, num)


                    else:
                        print("str")
                        if event.obj.message['text'] in List_of_M:
                            vk.messages.send(
                                user_id=event.obj.message['from_id'],
                                random_id=get_random_id(),
                                peer_id=event.obj.message['from_id'],
                                keyboard=keyboard_2.get_keyboard(),
                                message=T0(event.obj.message['text']))

    elif event.type == VkBotEventType.MESSAGE_EVENT:

        if event.object.payload.get('type') in CALLBACK_TYPES:

            vk.messages.sendMessageEventAnswer(
                event_id=event.object.event_id,
                user_id=event.object.user_id,
                peer_id=event.object.peer_id,
                event_data=json.dumps(event.object.payload))








        elif event.object.payload.get('type') == "1":
            last_id = vk.messages.edit(
                peer_id=event.obj.peer_id,
                message='Выбирай категорию (1)',
                conversation_message_id=event.obj.conversation_message_id,
                keyboard=keyboard_menu_1.get_keyboard())


        elif event.object.payload.get('type') == "2":
            last_id = vk.messages.edit(
                peer_id=event.obj.peer_id,
                message='Выбирай категорию (2)',
                conversation_message_id=event.obj.conversation_message_id,
                keyboard=keyboard_menu_2.get_keyboard())


        elif event.object.payload.get('type') == "3":
            last_id = vk.messages.edit(
                peer_id=event.obj.peer_id,
                message='Выбирай категорию(3)',
                conversation_message_id=event.obj.conversation_message_id,
                keyboard=keyboard_menu_3.get_keyboard())

if __name__ == '__main__':
    print()
