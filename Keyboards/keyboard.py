from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(
    KeyboardButton("CANCEL")
)

submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(
    KeyboardButton("ДА"),
    KeyboardButton("НЕТ"),
)
