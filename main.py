from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from decouple import config
import logging
from handlers import client,callback,extra
from config import dp, bot





client.register_client_handlers(dp)
callback.register_callback_handlers(dp)
extra.register_extra_handlers(dp)






if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
