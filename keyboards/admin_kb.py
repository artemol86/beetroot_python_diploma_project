from aiogram.types import ReplyKeyboardMarkup, KeyboardButton 

add_button = KeyboardButton('/Add ')
del_button = KeyboardButton('/Delete')

kb_admin = ReplyKeyboardMarkup(resize_keyboard=True)
kb_admin.add(add_button).insert(del_button)
