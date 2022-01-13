import sqlite3 as sq
from create_bot import bot


def sql_start():
	global base, cur
	base = sq.connect('dishes.db')
	cur = base.cursor()
	if base: 
		print('Connected to DB!')
	base.execute('CREATE TABLE IF NOT EXISTS dishes_list(img TEXT, name TEXT, recipe TEXT)')
	base.commit()

async def sql_add_command(state):
	async with state.proxy() as data:
		cur.execute('INSERT INTO dishes_list VALUES (?, ?, ?)', tuple(data.values()))
		base.commit()

async def sql_read_all(message):
	for dish in cur.execute('SELECT * FROM dishes_list').fetchall():
		await bot.send_photo(message.from_user.id, dish[0], f'Страва: {dish[1]}\nРецепт: {dish[2]}')
