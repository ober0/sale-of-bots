import types
from aiogram.types.web_app_info import WebAppInfo
from aiogram import *
import json

bot = Bot("6184823844:AAE7JvBRB4shgFkLd2353I9ihWf4Ggtkr74")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Форма заказа',web_app=WebAppInfo(url='https://ober1.st8.ru/tg/telegram.html')))
    await message.answer('Привет', reply_markup=markup)

@dp.message_handler(content_types=['web_app_data'])
async def web_app(message:types.Message):
    res = json.loads(message.web_app_data.data)
    name = res['name']
    email = res['email']
    text = res['text']
    tg = res['telegram_id']
    print(name,email,tg,text)



executor.start_polling(dp)