import random

from aiogram import types, Dispatcher
from config import bot, dp
from config import ADMIN





async def echo(message: types.Message):
    if message.text.isdigit():
        await bot.send_message(message.chat.id, int(message.text)**2)
    elif message.text.startswith('game')and message.from_user.id in ADMIN:
        emojis = ['🎯', '🎳', '🎰', '🎲', '⚽️', '🏀']
        pen = random.choice(emojis)
        await bot.send_dice(message.chat.id,emojis = pen)
    else:
        await bot.send_message(message.from_user.id,message.text)
        await bot.send_message(message.from_user.id, f"Hello {message.from_user.first_name}")
        await message.answer("How are you!")
        await message.reply("Do not answer this is system generated reply")


def register_extra_handlers(dp:Dispatcher):
    dp.register_message_handler(echo)