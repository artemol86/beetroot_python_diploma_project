from aiogram.types import ReplyKeyboardMarkup, KeyboardButton 
b1 = KeyboardButton('/Що мені приготувати? ')
b2 = KeyboardButton('/Показати_всі_страви')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).insert(b2)
