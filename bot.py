from aiogram.utils import executor
from create_bot import dp
from db import sqlite_db


async def on_startup(_):
	print('Bot has been started')
	sqlite_db.sql_start()

from handlers import client, admin

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
