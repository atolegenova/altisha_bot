from aiogram .types import InlineKeyboardMarkup, InlineKeyboardButton,\
    ReplyKeyboardMarkup, KeyboardButton

start_ = InlineKeyboardButton('Start', callback_data='starting')
start_btn = InlineKeyboardMarkup(). add(start_)

registration = InlineKeyboardButton('Registration', callback_data='reg')
info = InlineKeyboardButton('Information', callback_data='info')
reg_btn = InlineKeyboardMarkup().row(registration, info)

weather = InlineKeyboardButton('Weather', callback_data='weather')
news = InlineKeyboardButton('NEWS',callback_data='news')
news_btn = InlineKeyboardMarkup().row(news, weather)


read_db = InlineKeyboardButton('база данных', callback_data='read_db')
admin_btn = InlineKeyboardMarkup().add(read_db)

next_btn = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Следующая новость'))
#next_btn = KeyboardButton('Следующая новость')

