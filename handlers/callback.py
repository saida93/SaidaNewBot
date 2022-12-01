from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp


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


async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton("Next", callback_data='button_call_3')
    markup.add(button_call_3)

    question = "Suriname is located on which continent?"
    answers = [
        "South Africa",
        "Australia",
        "America",
        "South America",
        "Eurasia",
        "Africa",
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="",
        open_period=10,
        reply_markup=markup
    )


async def quiz_4(call: types.CallbackQuery):
    question = "What was Meta Platform Inc formerly known as?"
    answers = [
        "Facebook",
        "Whatsup",
        "TikTok",
        "Linkeldn",
        "Odnoklassniki",
        "Agent.ru",
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

    )


def register_callback_handlers(dp: Dispatcher):
    dp.register_message_handler(quiz_2, lambda call: call.data == 'button_1')
    dp.register_message_handler(quiz_2, lambda call: call.data == 'button_2')
    dp.register_message_handler(quiz_4, lambda call: call.data == 'button_3')
