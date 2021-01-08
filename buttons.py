from aiogram .types import InlineKeyboardMarkup, InlineKeyboardButton,\
    ReplyKeyboardMarkup, KeyboardButton

start_ = InlineKeyboardButton('Start', callback_data='starting')
start_btn = InlineKeyboardMarkup(). add(start_)

registration = InlineKeyboardButton('Registration', callback_data='reg')
info = InlineKeyboardButton('Information', callback_data='info')
reg_btn = InlineKeyboardMarkup().row(registration, info)


read_db = InlineKeyboardButton('база данных', callback_data='read_db')
admin_btn = InlineKeyboardMarkup().add(read_db)
