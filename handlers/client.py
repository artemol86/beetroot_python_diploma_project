from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from db import sqlite_db


async def command_start(message: types.Message):
	try:
		await bot.send_message(message.from_user.id, 'Привіт! Цей бот рандомно\
			генерує ідеї для приготування їжі! Вибери щось на свій смак!', reply_markup=kb_client)
		await message.delete()
	except:
		await message.reply('Бот працює тільки через приватні сповіщення \
			кнопками, напишіть йому: \nhttps://t.me/heeYop5ebot')


async def dishes_all(message : types.Message):
	await sqlite_db.sql_read_all(message)

async def random_dish(message : types.Message):
	await sqlite_db.sql_random_read(message)

async def empty(message : types.Message):
	await bot.send_message(message.from_user.id, 'Немає такої команди!\nСпробуй так: /start')
	await message.delete()

	
def register_handlers_client(dp : Dispatcher):
	dp.register_message_handler(command_start, commands=['start', 'help'])
	dp.register_message_handler(dishes_all, commands=['Показати_всі_страви'])
	dp.register_message_handler(random_dish, commands=['Що_мені_приготувати?'])
#	dp.register_message_handler(empty)
