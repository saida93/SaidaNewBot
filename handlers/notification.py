import aioschedule
from aiogram import types, Dispatcher
from config import bot
import asyncio


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await bot.send_message(chat_id=chat_id, text="OK!")


async def go_to_work():
    await bot.send_message(chat_id=chat_id, text="wake up!")


async def scheduler():
    aioschedule.every().thursday.at('15:47').do(go_to_work)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handlers_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: 'Remind' in word.text)
