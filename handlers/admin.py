from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp
from aiogram.dispatcher.filters import Text
from db import sqlite_db
from keyboards import admin_kb
from setup_keys import users

class FSMAdmin(StatesGroup):
	photo = State()
	name = State()
	recipe = State()
	link = State()

#Starting dialog
#@dp.message_handler(commands='Add', state=None)
async def cm_start(message : types.Message):
#	if message.from_user.id in users:
	await FSMAdmin.photo.set()
	await message.reply('Додай фото')

#Exit from State(canceling adding)
#@dp.message_handler(state='*', commands='cancel')
#@dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
	current_state = await state.get_state()
	if current_state is None:
		return
	await state.finish()
	await message.reply('Successfully canceled')

#Catch 1st question and put into dictionary
#@dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message : types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['photo'] = message.photo[0].file_id
	await FSMAdmin.next()
	await message.reply('Додай назву')

#Catch 2nd question
#@dp.message_handler(state=FSMAdmin.name)
async def load_name(message : types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['name'] = message.text
	await FSMAdmin.next()
	await message.reply('Тепер сам рецепт(не більше 200 символів!))')

#Catch 3rd question	
#@dp.message_handler(state=FSMAdmin.recipe)
async def load_recipe(message : types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['recipe'] = message.text

#	async with state.proxy() as data:
#		await message.reply(str(data))
	await sqlite_db.sql_add_command(state)
	await state.finish()


#register handlerss
def register_handlers_admin(dp: Dispatcher):
	dp.register_message_handler(cm_start, commands=['add'], state=None)
	dp.register_message_handler(cm_start, Text(equals='add', ignore_case=True), state=None)
	dp.register_message_handler(cancel_handler, state='*', commands='cancel')
	dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state='*')
	dp.register_message_handler(load_photo, content_types=['photo'], state = FSMAdmin.photo)
	dp.register_message_handler(load_name, state = FSMAdmin.name)
	dp.register_message_handler(load_recipe, state = FSMAdmin.recipe)