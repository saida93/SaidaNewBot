from aiogram import Dispatcher, types
from config import bot, dp


async def echo(message: types.Message):
    bad_words = []
    for word in bad_words:
        if word in message.text.lower():
            await bot.delete_message(message.chat.id, message.message_id)


    if message.text.startswith('.'):
        await bot .pin_chat_message(message.chat.id, message.message_id)


def register_handler_extra(dp: Dispatcher):
   dp.message_handler(echo)
