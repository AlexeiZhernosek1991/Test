from google.auth import credentials

token = '6236696473:AAH_OGgS5jBhtDC7ZRA8lJwXHHZkQCfxZwg'

import time
import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from telebot.types import InputMediaPhoto
import gspread

bot = telebot.TeleBot('6236696473:AAH_OGgS5jBhtDC7ZRA8lJwXHHZkQCfxZwg')

gc = gspread.service_account(filename='credentials.json')
sht2 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1kMgS4p93BGoZ6IAMaE8NlTxrQt_x8UI_yU8PMMD8xPM')
worksheet = sht2.sheet1
list_of_lists = worksheet.get_values('B2:M49')
print(list_of_lists)

stat_dict = {'all': [], 'user_finish': []}


def index(a_list: list, num_: str, id_message):
    for i in (0, 1, 2, 3, 11):
        if i == 0:
            try:
                bot.send_message(id_message, a_list[int(num_)][i])
            except:
                pass
        elif i == 1:
            try:
                list_photo = a_list[int(num_)][i].split(';')
                for photo in list_photo:
                    photo1 = open(f"media\\{photo}", 'rb')
                    bot.send_photo(id_message, photo=photo1)
                    photo1.close()
            except:
                pass
        elif i == 2:
            try:
                bot.send_message(id_message, a_list[int(num_)][i])
            except:
                pass
        elif i == 3:
            try:
                audio1 = open(f"media\\{a_list[int(num_)][i]}", 'rb')
                bot.send_audio(id_message, audio1)
                audio1.close()
            except:
                pass
        elif i == 11:
            if a_list[int(num_)] == a_list[-1]:
                try:
                    stat_dict['user_finish'].append(id_message)
                    bot.send_message(id_message, 'Попробуем еще раз\n Жми на "/start"')
                except:
                    pass
            else:
                try:
                    keyd_ = types.InlineKeyboardMarkup()
                    keyd_.add(types.InlineKeyboardButton('*', callback_data='a' + str(int(num_) + 1)))
                    bot.send_message(id_message, f'{a_list[int(num_)][i]}', reply_markup=keyd_)
                except:
                    pass


def quiz(a_list: list, num_: str, id_message):
    try:
        keyd_ = types.InlineKeyboardMarkup()
        button_list = a_list[int(num_)][5].split(',')
        for i in button_list:
            if i == a_list[int(num_)][6]:
                keyd_.add(types.InlineKeyboardButton(f'{i}', callback_data=f'y{num_}'))
            else:
                keyd_.add(types.InlineKeyboardButton(f'{i}', callback_data=f'f{num_}'))
        bot.send_message(id_message, a_list[int(num_)][0], reply_markup=keyd_)
    except:
        pass


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        id_message = message.chat.id
        index(list_of_lists, '0', id_message)
        stat_dict['all'].append(message.from_user.user_id)


@bot.message_handler(content_types=['text'])
def stat(message):
    if message.text == '/stat':
        id_message = message.chat.id
        statistic_ = len(stat_dict['user_finish']) / len(stat_dict['all']) * 100
        bot.send_message(id_message, f'Количество пользователей дошедших до финиша {statistic_}%')


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    print(call)
    bot.answer_callback_query(callback_query_id=call.id, )
    id_message = call.from_user.id
    flag = call.data[0]
    num_ = call.data[1:]
    print('работает')
    if flag == 'a':
        if list_of_lists[int(num_)][5] == '':
            index(list_of_lists, num_, id_message)
        else:
            quiz(list_of_lists, num_, id_message)
    elif flag == 'y':
        bot.send_message(id_message, list_of_lists[int(num_)][7])
        keyd_ = types.InlineKeyboardMarkup()
        keyd_.add(types.InlineKeyboardButton('*', callback_data='a' + str(int(num_) + 1)))
        bot.send_message(id_message, f'{list_of_lists[int(num_)][11]}', reply_markup=keyd_)
    elif flag == 'f':
        bot.send_message(id_message, list_of_lists[int(num_)][8])
        keyd_ = types.InlineKeyboardMarkup()
        keyd_.add(types.InlineKeyboardButton('*', callback_data='a' + str(int(num_) + 1)))
        bot.send_message(id_message, f'{list_of_lists[int(num_)][11]}', reply_markup=keyd_)
    else:
        pass


print("Ready")
bot.infinity_polling()

"""

bot.send_message(IdOfMessage, text)  
сообщение


photo1 = open("file", 'rb')
bot.send_photo(IdOfMessage, photo=photo1)
photo1.close()
фото

audio1 = open("file", 'rb')
bot.send_audio(IdOfMessage, audio1)
audio1.close()
аудио

stic1 = open("file", 'rb')
bot.send_sticker(IdOfMessage, stic1)
stic1.close()
стикер
"""
