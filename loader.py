from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from utils import config

bot = Bot(token=config('7650294135:AAFzylW3QSMnYm6L137RIovQl7WndjGQb_A'), parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
vip = Dispatcher(bot, storage=storage)
