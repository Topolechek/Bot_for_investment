from aiogram.dispatcher.filters.state import StatesGroup, State


class Level(StatesGroup):
    mid_price = State()
    quality = State()
    price_now = State()
    how_much = State()

    func = State()
