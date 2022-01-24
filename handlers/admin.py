from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from db import sqlite_db
from keyboards import kb_admin
from setup_keys import admins
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton 


class FSMAdmin(StatesGroup):
	photo = State()
	name = State()
	recipe = State()
	link = State()

async def make_changes_command(message: types.Message):
	if message.from_user.id in admins:
		await bot.send_message(message.from_user.id, 'Ти пройшов перевірку на адміна, \
			вітаю!\nТепер додавай або видаляй страви', reply_markup=kb_admin)
		await message.delete()
	else:
		await bot.send_message(message.from_user.id, 'Ти не адмін! Тобі не можна! :-)')


async def cm_start(message : types.Message):
	if message.from_user.id in admins:
		await FSMAdmin.photo.set()
		await message.reply('Додай фото')

async def cancel_handler(message: types.Message, state: FSMContext):
	if message.from_user.id in admins:
		current_state = await state.get_state()
		if current_state is None:
			return
		await state.finish()
		await message.reply('Successfully canceled')

async def load_photo(message : types.Message, state: FSMContext):
	if message.from_user.id in admins:
		async with state.proxy() as data:
			data['photo'] = message.photo[0].file_id
		await FSMAdmin.next()
		await message.reply('Додай назву')

async def load_name(message : types.Message, state: FSMContext):
	if message.from_user.id in admins:
		async with state.proxy() as data:
			data['name'] = message.text
		await FSMAdmin.next()
		await message.reply('Тепер сам рецепт(не більше 200 символів!))')

async def load_recipe(message : types.Message, state: FSMContext):
	if message.from_user.id in admins:
		async with state.proxy() as data:
			data['recipe'] = message.text

		await sqlite_db.sql_add_command(state)
		await state.finish()

@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback_run(callback_query: types.CallbackQuery):
	if message.from_user.id in admins:
		await sqlite_db.sql_delete_command(callback_query.data.replace('del ', ''))
		await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} видалено.', show_alert=True)


@dp.message_handler(commands='Delete')
async def del_item(message: types.Message):
	if message.from_user.id in admins:
		read = await sqlite_db.sql_read_all_2()
		for dish in read:
			await bot.send_photo(message.from_user.id, dish[0],f'{dish[1]}\nОписание: {dish[2]}')
			await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().\
				add(InlineKeyboardButton(f'Видалити {dish[1]}', callback_data=f'del {dish[1]}')))


def register_handlers_admin(dp: Dispatcher):
	dp.register_message_handler(cm_start, commands=['add'], state=None)
	dp.register_message_handler(cm_start, Text(equals='add', ignore_case=True), state=None)
	dp.register_message_handler(cancel_handler, state='*', commands='cancel')
	dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state='*')
	dp.register_message_handler(load_photo, content_types=['photo'], state = FSMAdmin.photo)
	dp.register_message_handler(load_name, state = FSMAdmin.name)
	dp.register_message_handler(load_recipe, state = FSMAdmin.recipe)
	dp.register_message_handler(make_changes_command, commands=['admin'])
#	dp.register_message_handler(del_callback_run, commands=['del'], state=None)
#	dp.register_message_handler(del_item, commands=['Delete'], state=None)