import types
from aiogram.types.web_app_info import WebAppInfo
from aiogram import *
import json
import sqlite3

bot = Bot("6184823844:AAE7JvBRB4shgFkLd2353I9ihWf4Ggtkr74")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Форма заказа',web_app=WebAppInfo(url='https://ober1.st8.ru/tg/new/telegram.html')))
    await message.answer('Привет', reply_markup=markup)

@dp.message_handler(content_types=['web_app_data'])
async def web_app(message:types.Message):
    res = json.loads(message.web_app_data.data)
    name = res['name']
    email = res['email']
    text = res['text']
    tg = res['telegram_id']
    time = res['time']
    print(name,email,tg,text, time)
    string = f'{name},{email},{tg},{time},{text}\n'
    with open('req.txt', 'a', encoding='utf-8')as file:
        file.write(string)

@dp.message_handler(commands=['test'])
async def test(message:types.Message):
    res = []
    with open('req.txt', 'r', encoding='utf-8')as file1:
        for i in file1.readlines():
            res.append(i)
    for i in res:
        await message.answer(i)
executor.start_polling(dp)