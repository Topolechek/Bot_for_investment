from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hcode

from tgbot.handlers.user import user_again
from tgbot.keyboards.keybrd import again


async def bot_echo(message: types.Message):
    text = [
        "Видимо что-то пошло не так, нажми 'Начать сначала' \n"
        "Или нажми /start в меню"
    ]

    await message.answer('\n'.join(text))


async def bot_echo_all(message: types.Message, state: FSMContext):
    state_name = await state.get_state()
    text = [
        f'Эхо в состоянии {hcode(state_name)}',
        'Содержание сообщения:',
        hcode(message.text)
    ]
    await message.answer('\n'.join(text), reply_markup=again)


def register_echo(dp: Dispatcher):
    dp.register_message_handler(bot_echo)
    dp.register_message_handler(bot_echo_all, state="*", content_types=types.ContentTypes.ANY)
    dp.register_message_handler(user_again, text='Начать сначала', state="*")