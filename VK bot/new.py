from vk_api import VkApi
import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import json
import gspread

GROUP_ID = '219364665'
GROUP_TOKEN = 'vk1.a.Udr_3z5uGE0H0VcDsiUrnxXt8YXuiYaQZPdLIYC1YrzbFTxRZvvelbhTEFiB0-0cdRJ21Xy2M31lVbaXR3HWI0AWBQz74S0p8cjDs1A2BM6DGzIcirs90Jw0kyp2sbFuDkecVixcmfEY4FbN01pD7MR6520v-GN5Zfzm8GpP4xbaDPsC7IBlszgiaLxLo65XLAzAAp4Efm-tBI-N4n9mbQ'
API_VERSION = '5.120'

gc = gspread.service_account(filename="credentials.json")
sht2 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1Ce5d0HTVVaY6A41SREJDa4yN4lJGYRRL0N1r_CvLsKs/edit#gid=0')
worksheet = sht2.sheet1
list_of_lists = worksheet.get_values('A1:I152')
menu_dict = {}
promocod_dict = {}
shop_list = []

for row in list_of_lists[1:]:
    if row[8] not in menu_dict:
        menu_dict.setdefault(row[8], [])
    if row[0] not in menu_dict[row[8]]:
        menu_dict[row[8]].append(row[0])
    text = ''
    for x in [0, 3, 7, 5, 6, 4, 2]:
        text += f'{list_of_lists[0][x]}: {row[x]}\n'
    if row[0] not in promocod_dict:
        promocod_dict.setdefault(row[0], [row[8]])
    promocod_dict[row[0]].append(text)

category_list = list(menu_dict.keys())
settings = dict(one_time=False, inline=False)
settings2 = dict(one_time=False, inline=True)

stat_shop = {}

admin = '134828772'


def get_stat(stat_shop, cat):
    vk.messages.send(
        user_id=event.obj.user_id,
        random_id=get_random_id(),
        peer_id=event.obj.peer_id,
        message=f'Категория {cat} посещений{sum(len(z) for a, z in stat_shop[cat].items())}')
    for shop, stat_ in stat_shop[cat].items():
        vk.messages.send(
            user_id=event.obj.user_id,
            random_id=get_random_id(),
            peer_id=event.obj.peer_id,
            message=f'Магазин {shop} посетителей{len(set(stat_))}/посещений{len(stat_)}')


def universall_keyboard_slider(mass, flag, change_flang, slide_num=0, inline=5):
    keyb = VkKeyboard(**settings2)
    if len(mass) < (slide_num + 1) * inline:
        lenght = len(mass)
    else:
        lenght = (slide_num + 1) * inline
    for inl in range(slide_num * inline, lenght):
        d = {"type": flag, "data": str(inl), 'name_but': f"{mass[inl]}"}
        keyb.add_callback_button(label=f"{mass[inl]}", color=VkKeyboardColor.SECONDARY, payload=d)
        keyb.add_line()

    if slide_num == 0 and len(mass) >= inline:
        # первый
        keyb.add_callback_button(label="вперед", color=VkKeyboardColor.PRIMARY,
                                 payload={"type": change_flang, "data": str(slide_num + 1), 'flag': flag})
    elif len(mass) > (slide_num + 1) * inline:
        # посередине
        keyb.add_callback_button(label="назад", color=VkKeyboardColor.PRIMARY,
                                 payload={"type": change_flang, "data": str(slide_num - 1), 'flag': flag})
        keyb.add_callback_button(label="вперед", color=VkKeyboardColor.PRIMARY,
                                 payload={"type": change_flang, "data": str(slide_num + 1), 'flag': flag})

    else:
        keyb.add_callback_button(label="Меню!", color=VkKeyboardColor.PRIMARY,
                                 payload={"type": change_flang, "data": str(slide_num - 1), 'flag': flag})
        # конец
    return keyb.get_keyboard()


# Основное меню
keyboard_1 = VkKeyboard(**settings)

keyboard_1.add_callback_button(label='Таблица со всеми промокодами!', color=VkKeyboardColor.POSITIVE,
                               payload={"type": "open_link",
                                        "link": "https://docs.google.com/spreadsheets/d/1Ce5d0HTVVaY6A41SREJDa4yN4lJGYRRL0N1r_CvLsKs/edit#gid=0"})
keyboard_1.add_line()
keyboard_1.add_button(label='Запустить бота!', color=VkKeyboardColor.NEGATIVE, payload={"type": "text"})
keyboard_1.add_line()
keyboard_1.add_callback_button(label='Мы в Телеграме!', color=VkKeyboardColor.PRIMARY,
                               payload={"type": "open_link", "link": "https://t.me/skidkinezagorami"})

# Запускаем бот
vk_session = VkApi(token=GROUP_TOKEN, api_version=API_VERSION)
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, group_id=GROUP_ID)

CALLBACK_TYPES = ('show_snackbar', 'open_link', 'open_app', 'text')

print("Ready")

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.obj.message['text'] != '':
            if event.from_user:
                if event.obj.message['text'] == 'Запустить бота!' or event.obj.message['text'] == "Меню!":
                    print(event.obj.message['from_id'])
                    vk.messages.send(
                        user_id=event.obj.message['from_id'],
                        random_id=get_random_id(),
                        peer_id=event.obj.message['from_id'],
                        message='Выберите категорию в которой хотите получить скидку ⬇️',
                        keyboard=universall_keyboard_slider(category_list, '1', '!'))
                elif event.obj.message['text'] == 'Статистика':
                    # if event.obj.message['from_id'] == admin:
                    vk.messages.send(
                        user_id=event.obj.message['from_id'],
                        random_id=get_random_id(),
                        peer_id=event.obj.message['from_id'],
                        message='Выберите категорию в которой хотите получить статистику ⬇️',
                        keyboard=universall_keyboard_slider(category_list, '3', '!'))
                    # else:
                    #     vk.messages.send(
                    #         user_id=event.obj.message['from_id'],
                    #         random_id=get_random_id(),
                    #         peer_id=event.obj.message['from_id'],
                    #         message='У вас нет прав администратора')
    elif event.type == VkBotEventType.MESSAGE_EVENT:
        if event.object.payload.get('type') in CALLBACK_TYPES:
            vk.messages.sendMessageEventAnswer(
                event_id=event.object.event_id,
                user_id=event.object.user_id,
                peer_id=event.object.peer_id,
                event_data=json.dumps(event.object.payload))
        # Слайдер для категорий
        elif event.object.payload.get('type') == '!':
            mass = category_list
            flag = event.object.payload.get('flag')
            change_flag = event.object.payload.get('type')
            slide_num = int(event.object.payload.get('data'))
            last_id = vk.messages.edit(
                peer_id=event.obj.peer_id,
                message=f"Выбирай категорию",
                conversation_message_id=event.obj.conversation_message_id,
                keyboard=universall_keyboard_slider(mass, flag, change_flag, slide_num=slide_num))
        # Слайдер для магазинов
        elif event.object.payload.get('type') == '@':
            mass = shop_list
            flag = '2'
            change_flag = event.object.payload.get('type')
            slide_num = int(event.object.payload.get('data'))
            last_id = vk.messages.edit(
                peer_id=event.obj.peer_id,
                message=f"Выбирай категорию",
                conversation_message_id=event.obj.conversation_message_id,
                keyboard=universall_keyboard_slider(mass, flag, change_flag, slide_num=slide_num))
        # Кнопки с магазинами
        elif event.object.payload.get('type') == '1':
            cat = event.object.payload.get('name_but')
            if cat in stat_shop:
                pass
            else:
                stat_shop.setdefault(cat, {})
            shop_index = int(event.object.payload.get('data'))
            shop_list = menu_dict[category_list[shop_index]]
            # категория
            vk.messages.send(
                user_id=event.obj.user_id,
                random_id=get_random_id(),
                peer_id=event.obj.peer_id,
                keyboard=universall_keyboard_slider(shop_list, '2', '@'),
                message='Выбирайте 🥰')
        # Промокоды
        elif event.object.payload.get('type') == '2':
            key_ = event.object.payload.get('name_but')
            # магазин
            promocod_list = promocod_dict[key_]
            for i in promocod_list[1:]:
                vk.messages.send(
                    user_id=event.obj.user_id,
                    random_id=get_random_id(),
                    peer_id=event.obj.peer_id,
                    message=i)
            keyb = VkKeyboard(**settings2)
            d = {"type": '1', "data": category_list.index(promocod_list[0]), 'name_but': f"{promocod_list[0]}"}
            keyb.add_callback_button(label=f"{promocod_list[0]}", color=VkKeyboardColor.SECONDARY, payload=d)
            keyb.add_line()
            keyb.add_button(label='Меню!', color=VkKeyboardColor.NEGATIVE, payload={"type": "text"})
            vk.messages.send(
                user_id=event.obj.user_id,
                random_id=get_random_id(),
                peer_id=event.obj.peer_id,
                message='Куда идем дальше',
                keyboard=keyb.get_keyboard(),
            )
            shop = event.object.payload.get('name_but')
            if shop in stat_shop[promocod_list[0]]:
                stat_shop[promocod_list[0]][shop].append(event.obj.user_id)
            else:
                stat_shop[promocod_list[0]].setdefault(shop, [event.obj.user_id])
        elif event.object.payload.get('type') == '3':
            get_stat(stat_shop, event.object.payload.get('name_but'))

# def keyboard_universal_slider(mass, flag, change_flag, slide_num=0, num_of_el=5):
#     keyb = VkKeyboard(**settings_inline)
#
#     if len(mass) < (slide_num + 1) * num_of_el:
#         lenght = len(mass)
#     else:
#         lenght = (slide_num + 1) * num_of_el
#
#     for i in range(slide_num * num_of_el, lenght):
#         d = {"type": flag, "data": str(i)}
#         keyb.add_button(label=mass[i], color=VkKeyboardColor.SECONDARY, payload=d)
#
#         keyb.add_line()
#
#     if slide_num == 0 and len(mass) >= num_of_el:
#         # первый
#         keyb.add_callback_button(label="вперед", color=VkKeyboardColor.PRIMARY,
#                                  payload={"type": change_flag, "data": str(slide_num + 1)})
#     elif len(mass) > (slide_num + 1) * num_of_el:
#         # посередине
#         keyb.add_callback_button(label="назад", color=VkKeyboardColor.PRIMARY,
#                                  payload={"type": change_flag, "data": str(slide_num - 1)})
#         keyb.add_callback_button(label="вперед", color=VkKeyboardColor.PRIMARY,
#                                  payload={"type": change_flag, "data": str(slide_num + 1)})
#
#     else:
#         keyb.add_callback_button(label="назад", color=VkKeyboardColor.PRIMARY,
#                                  payload={"type": change_flag, "data": str(slide_num - 1)})
#         # конец
#     return keyb.get_keyboard()
