from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import dp, bot
from  parser.namba_films import parser


async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, f'Hi Whats up!{message.from_user.first_name}')

async def bagsparser(message: types.Message):
    items = parser()
    for item in items:
        await bot.send_message(message.from_user.id, f"{item['title']}\n{item['price']}\n{item['link']}")
# @dp.message_handler(commands=['mem'])
# async def mem(message: types.Message):
#     photo = open('images.jpg', 'rb')
#     await bot.send_photo(message.from_user.id, photo=photo)


async def i(message: types.Message):
    if message.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    else:
        await message.reply("Answer")


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


def register_client_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(i, commands=['pin'], commands_prefix='!')
    dp.register_message_handler(bagsparser, commands=['parser'])
