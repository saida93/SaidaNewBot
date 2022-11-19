from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from decouple import config
import logging


TOKEN =config("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id,f'Hi Whats up!{message.from_user.first_name}')

@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data='button_call_1')
    markup.add(button_call_1)

    question = "Why are flamingos are pink?"
    answers = [
        "Because they like pink color",
        'Because of their diet of algae, shrimps, and crustaceans',
        'No They Are Grey',
        'I dont Know',
        'They are so funny',
    ]


    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="",
        open_period=10,
        reply_markup=markup
    )



@dp.callback_query_handler(text="button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("Next", callback_data='button_call_2')
    markup.add(button_call_2)

    question = "What is the size of a newborn Kangaroo?"
    answers = [
        "One inch",
        "15cm",
        "1m",
        "20cm",
        "1cm",
        "3cm",
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="",
        open_period=10,
        reply_markup=markup
    )

#@dp.message_handler(commands =['mem'])
#async def mem(message:types.Message):
#    photo2 = ('photo/photo.jpg','rb')
#   await bot.send_photo(message.chat.id, photo = photo2)
#photo cannot be uploaded



@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isdigit():
        await bot.send_message(message.chat.id, int(message.text)**2)
    else:
        await bot.send_message(message.from_user.id,message.text)
        await bot.send_message(message.from_user.id, f"Hello {message.from_user.first_name}")
        await message.answer("How are you!")
        await message.reply("Do not answer this is system generated reply")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
