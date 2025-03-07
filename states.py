from aiogram.filters.state import State, StatesGroup


class Wait(StatesGroup):
    wait_weight = State()
