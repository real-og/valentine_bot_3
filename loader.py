from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
import logging
import os


logging.basicConfig(level=logging.INFO)
ADMIN_IDS = str(os.environ.get('ADMIN_IDS')).split(',')
BOT_TOKEN = str(os.environ.get('BOT_TOKEN'))

storage = RedisStorage2(db=3)
# storage = MemoryStorage()

default_text = 'Подпись...'
default_background = 'color9.png'
default_font = 'comforter.ttf'
default_photo = None

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage=storage)