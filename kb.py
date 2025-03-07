from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

main_menu = [
    [InlineKeyboardButton(text="Сделать расчёт 🎯", callback_data="rasch")],
    [InlineKeyboardButton(text="Инструкция к применению 📝", callback_data="instruction")]
]

dozes = [
    [InlineKeyboardButton(text="0,4 мг/г 💊", callback_data='0.4')],
    [InlineKeyboardButton(text="0,6 мг/кг 💊", callback_data='0.6')],
    [InlineKeyboardButton(text="0,8 мг/кг 💊", callback_data='0.8')],
]

back_to_menu = [
    [InlineKeyboardButton(text="Меню  📊", callback_data="menu")],
]
