from google.auth import credentials

token = '6236696473:AAH_OGgS5jBhtDC7ZRA8lJwXHHZkQCfxZwg'

import time
import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from telebot.types import InputMediaPhoto
import gspread

bot = telebot.TeleBot('6236696473:AAH_OGgS5jBhtDC7ZRA8lJwXHHZkQCfxZwg')

new_list = [1, 2, 3, 4, 5, 6]


def button(i):
    global new_list
    keyd_ = types.InlineKeyboardMarkup()
    keyd_.add(types.InlineKeyboardButton(f'{new_list[i]}', callback_data=f'H{new_list[i]}'))
    keyd_.row((types.InlineKeyboardButton('⇐', callback_data=f'R{int(i) - 1}')),
              (types.InlineKeyboardButton('⇒', callback_data=f'R{int(i) + 1}')))
    return keyd_


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.chat.id, 'Выберите товар', reply_markup=button(0))


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    i = int(call.data[1:])
    if call.data[0] == 'R' and i >= 0:
        try:
            bot.edit_message_reply_markup(call.message.chat.id, call.message.id, reply_markup=button(i))
        except:
            pass
    elif call.data[0] == 'H':
        bot.send_message(call.message.chat.id, f'{call.data}')


print("Ready")
bot.infinity_polling()
# markup123 = types.ReplyKeyboardMarkup(resize_keyboard=True)
# button1 = types.KeyboardButton("и тебе привет")
# markup123.add(button1)
#
# gc = gspread.service_account(filename='credentials.json')
# sht2 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1wYMzadwIGco2hLDBugqN75pUk-iGVXIbib7azxvV5R8/edit#gid=0')
# worksheet = sht2.sheet1
# list_of_lists = worksheet.get_values('A1:F7')
# print(list_of_lists)
#
# keyd = types.ReplyKeyboardMarkup()
# keyd.add(*(types.KeyboardButton(a[0]) for a in list_of_lists[1:]))
# kart_dict = {}
# for var in list_of_lists[1:]:
#     kart_dict.setdefault(var[0], var[1:])
# print(kart_dict)
#
# # var1 = None
# # var2 = None
# # var3 = ['/', '*', '+', '-']
#
# @bot.message_handler(content_types=['text'])
# def start(message):
#     if message.text == '/start':
#         bot.send_message(message.chat.id, 'Выберите товар', reply_markup=keyd)
#     else:
#         if message.text in kart_dict:
#             photo1 = open(f"photo\\{kart_dict[message.text][0]}", 'rb')
#             bot.send_message(message.chat.id, f'{list_of_lists[0][0]} {message.text}')
#             bot.send_photo(message.chat.id, photo=photo1)
#             photo1.close()
#             bot.send_message(message.chat.id, f'{list_of_lists[0][2]} {kart_dict[message.text][1]} \n'
#                                               f'{list_of_lists[0][3]} {kart_dict[message.text][2]} \n'
#                                               f'{list_of_lists[0][4]} {kart_dict[message.text][3]} \n'
#                                               f'{list_of_lists[0][5]} {kart_dict[message.text][4]}')
#         else:
#             bot.send_message(message.chat.id, 'вы выбрали не существующий товар Выберите товар', reply_markup=keyd)
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def query_handler(call):
#     bot.answer_callback_query(callback_query_id=call.id, )
#     id = call.message.chat.id
#     flag = call.data[0]
#     num_ = call.data[1:]


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

# @bot.message_handler(content_types=['text'])
# def start(message):
#     global var1, var2, var3
#     if var1 == None and message.text.isdigit():
#         var1 = int(message.text)
#         bot.send_message(message.chat.id, f"первое число = {message.text}")
#     elif var1 != None and var2 == None and message.text.isdigit():
#         var2 = int(message.text)
#         bot.send_message(message.chat.id, f"второе число = {message.text}")
#     elif var1 != None and var2 != None and message.text in var3:
#         if message.text == '/':
#             result = var1 / var2
#             var1, var2 = None, None
#             bot.send_message(message.chat.id, f"ответ = {result}")
#         elif message.text == '*':
#             result = var1 * var2
#             var1, var2 = None, None
#             bot.send_message(message.chat.id, f"ответ = {result}")
#         elif message.text == '-':
#             result = var1 - var2
#             var1, var2 = None, None
#             bot.send_message(message.chat.id, f"ответ = {result}")
#         elif message.text == '+':
#             result = var1 + var2
#             var1, var2 = None, None
#             bot.send_message(message.chat.id, f"ответ = {result}")
