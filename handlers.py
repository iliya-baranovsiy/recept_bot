from aiogram.filters import CommandStart
from aiogram import F, types, Router
from aiogram.types import Message
from states import Wait
from aiogram.fsm.context import FSMContext
from functions import *
from kb import *
import time

router = Router()

users_dict = {}


@router.message(CommandStart())
async def hello_mes(msg: Message):
    user_id = msg.chat.id
    users_dict[user_id] = []
    buttons = InlineKeyboardMarkup(inline_keyboard=main_menu)
    await msg.answer("Приветсвенное сообщение в разработке, выберете один из унктов меню 👇", reply_markup=buttons)


@router.callback_query(F.data == "instruction")
async def get_instruction(call: CallbackQuery):
    buttons = InlineKeyboardMarkup(inline_keyboard=back_to_menu)
    await call.message.answer("Здесь будет инструкция к применению\nДля продолжения вернитесь в меню 👇", reply_markup=buttons)


@router.callback_query(F.data == "rasch")
async def weight_inp(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Введите вес пациента числом (Если число не целое введите его с помощью ' . ')")
    await state.set_state(Wait.wait_weight)


@router.message(F.text, Wait.wait_weight)
async def weight(msg: Message):
    user_id = msg.chat.id
    mes = msg.text
    buttons = InlineKeyboardMarkup(inline_keyboard=dozes)
    if mes.isdigit():
        users_dict[user_id] = int(mes)
        await msg.answer("Отлично, теперь выберете дозировку препората 🧑‍🔬", reply_markup=buttons)
    elif is_float(mes):
        users_dict[user_id] = float(mes)
        await msg.answer("Отлично, теперь выберете дозировку препората 🧑‍🔬", reply_markup=buttons)
    else:
        back_to_menu_1 = InlineKeyboardMarkup(inline_keyboard=back_to_menu)
        await msg.answer('Вы ввели неверный формат данных, введите заново или перейдите в меню',
                         reply_markup=back_to_menu_1)


@router.callback_query(F.data == "0.4")
async def doze_1(call: CallbackQuery):
    user_id = call.message.chat.id
    buttons = InlineKeyboardMarkup(inline_keyboard=back_to_menu)
    try:
        ans = create_answer_04(users_dict[user_id], 0.4)
        await call.message.answer(
            f'На вес пациента: <b>{users_dict[user_id]} кг</b>\nС дозировкой: <b>0.4 мг/кг</b>\nПринимается: <b>{ans[0]}</b>\nРекомендуемая продолжительность лечения: <b>{ans[1]}</b>',
            parse_mode='HTML')
        time.sleep(4)
        await call.message.answer("Чтобы продолжить введите вес пациента или вернитесь в меню", reply_markup=buttons)
    except:
        await call.message.answer("Упс, что-то пошло не так, попробуйте ввести вес заново или вернитесь в меню",reply_markup=buttons)


@router.callback_query(F.data == "0.6")
async def doze_2(call: CallbackQuery):
    user_id = call.message.chat.id
    buttons = InlineKeyboardMarkup(inline_keyboard=back_to_menu)
    try:
        ans = create_answer_04(users_dict[user_id], 0.6)
        await call.message.answer(
            f'На вес пациента: <b>{users_dict[user_id]} кг</b>\nС дозировкой: <b>0.6 мг/кг</b>\nПринимается: <b>{ans[0]}</b>\nРекомендуемая продолжительность лечения: <b>{ans[1]}</b>',
            parse_mode='HTML')
        time.sleep(4)
        await call.message.answer("Чтобы продолжить введите вес пациента или вернитесь в меню", reply_markup=buttons)
    except:
        await call.message.answer("Упс, что-то пошло не так, попробуйте ввести вес заново или вернитесь в меню", reply_markup=buttons)


@router.callback_query(F.data == "0.8")
async def doze_3(call: CallbackQuery):
    user_id = call.message.chat.id
    buttons = InlineKeyboardMarkup(inline_keyboard=back_to_menu)
    try:
        ans = create_answer_04(users_dict[user_id], 0.8)
        await call.message.answer(
            f'На вес пациента: <b>{users_dict[user_id]} кг</b>\nС дозировкой: <b>0.8 мг/кг</b>\nПринимается: <b>{ans[0]}</b>\nРекомендуемая продолжительность лечения: <b>{ans[1]}</b>',
            parse_mode='HTML')
        time.sleep(4)
        await call.message.answer("Чтобы продолжить введите вес пациента или вернитесь в меню", reply_markup=buttons)
    except:
        await call.message.answer("Упс, что-то пошло не так, попробуйте ввести вес заново или вернитесь в меню",
                                  reply_markup=buttons)


@router.callback_query(F.data == "menu")
async def menu(call: CallbackQuery, state: FSMContext):
    buttons = InlineKeyboardMarkup(inline_keyboard=main_menu)
    await call.message.answer("Выберете одну из предложенных функций 👇", reply_markup=buttons)
    await state.clear()


@router.message()
async def free_mes(msg: Message):
    buttons = InlineKeyboardMarkup(inline_keyboard=main_menu)
    await msg.answer("Я не понимаю, что Вы от меня требуете 😓, выберете пожалуйста доступные функции из меню",
                     reply_markup=buttons)
