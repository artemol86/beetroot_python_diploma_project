from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from setup_keys import token_key
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token=token_key)
dp = Dispatcher(bot, storage=storage)

