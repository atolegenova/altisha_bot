import time
import logging
from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters import Text
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram.utils.emoji import emojize
from aiogram import Bot, Dispatcher, executor, types
#from aiogram.types import Contact, Location
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from buttons import *
from classes import User, Form
from database import Data
from config import *
from parse import list_news
from weather_parse import weather

list_news.reverse()

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
new_user = {}
database = Data("db.db")
Data.create_db(database)


@dp.message_handler(commands=['start'])
async def hello(msg: types.Message):
    if msg.from_user.id == admin:
        await bot.send_message(msg.from_user.id, 'Здравствуй создатель!', reply_markup=admin_btn)
        await Form.admin_step.set()
    else:
        await bot.send_message(msg.from_user.id, f"Hello {msg.from_user.first_name}!", reply_markup=start_btn)
        await Form.starting.set()



@dp.callback_query_handler(text='starting', state=Form.starting)
async def start_func(query: types.CallbackQuery, state: FSMContext):
    user_id = query.from_user.id
    new_user[user_id] = User(user_id)
    id_ = new_user[user_id]
    id_.first_name = query.from_user.first_name
    all_users = database.get_users()
    for i in all_users:
        if user_id not in i:
            await bot.send_message(user_id, "Нужно зарегестрироваться", reply_markup=reg_btn)
            await Form.first_step.set()

        else:
            await bot.send_message(user_id, "Вы уже зарегестрированы", reply_markup=news_btn)
            await Form.news.set()





@dp.callback_query_handler(text='reg', state=Form.first_step)
@dp.callback_query_handler(text='info', state=Form.first_step)
async def first_step_func(query: types.CallbackQuery, state: FSMContext):
    msg = query.data
    if msg == 'reg':
        await bot.send_message(query.from_user.id, "Введите ваш номер телефона?")
        await Form.second_step.set()
    elif msg == 'info':
        await bot.send_message(query.from_user.id, "Для испрользования бота необходима регистрация")
        await Form.starting.set()


@dp.message_handler(content_types=types.ContentTypes.TEXT, state=Form.second_step)
async def second_step_func(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        id_ = new_user[msg.from_user.id]
        id_.phone = msg.text
    await bot.send_message(msg.from_user.id, f"Ваш номер {id_.phone} записан! Спасибо.")
    database.add_user(msg.from_user.id, id_.first_name, id_.phone)
    await bot.send_message(msg.from_user.id, "Регистрация прошла успешно. Можете пользоваться ботом")
    await Form.starting.set()


@dp.callback_query_handler(text='read_db', state=Form.admin_step)
async def admin_func(query: types.CallbackQuery, state: FSMContext):
    if query.data == 'read_db':
        for i in range(len(database.get_users())):
            msg = f"id = {database.get_users()[i][0]}\n" \
                  f"name = {database.get_users()[i][1]}\n" \
                  f"phone = {database.get_users()[i][2]}"
            await bot.send_message(admin, msg)
            time.sleep(1)


@dp.callback_query_handler(text='news', state=Form.news)
@dp.callback_query_handler(text='weather', state=Form.news)
async def news_func(query: types.CallbackQuery, state=FSMContext):
    if query.data == 'news':
        text = list_news.pop()
        await bot.send_message(query.from_user.id, text, reply_markup=next_btn)
        await Form.next_news.set()
    elif query.data == 'weather':
        await bot.send_message(query.from_user.id, weather, reply_markup=next_btn)
        await Form.next_news.set()




@dp.message_handler(content_types=types.ContentTypes.TEXT, state=Form.next_news)
async def next_news(msg: types.Message, state=FSMContext):
    if msg.text == 'Следующая новость':
        text = list_news.pop()
        await bot.send_message(msg.from_user.id, text)




executor.start_polling(dp, skip_updates=True)
