from datetime import datetime
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from tgbot.keyboards.keybrd import again, kb_menu

from tgbot.misc.states import Level
from tgbot.services.db_api.db_command import BotDB
from tgbot.services.parser import calcuate, inspect, dot

BotDB = BotDB('users_log.db')
err = 'Попробуйте написать цифрами'

async def user_start(message: Message):
    if not BotDB.user_exists(message.chat.id):
        BotDB.add_user(message.chat.id, message.chat.first_name, datetime.now())
        await message.bot.send_message('443232407', BotDB.count_users())
    await message.answer(f"Привет {message.chat.first_name}! \n"
                         f"Я помогаю быстро посчитать среднюю цену Вашей акции после того как Вы усреднитесь! \n"
                         f"\n"
                         f"Напишите, какая сейчас средняя цена акции!")
    await Level.mid_price.set()





async def user_again(message: Message):
    if not BotDB.user_exists(message.chat.id):
        BotDB.add_user(message.chat.id, message.chat.first_name, datetime.now())
        await message.bot.send_message('443232407', BotDB.count_users())
    await message.answer(f"Напишите, какая сейчас средняя цена акции у Вас в портфеле", reply_markup=kb_menu)
    await Level.mid_price.set()




async def my_mid_price(message: Message, state: FSMContext):
    replaced = dot(message.text)
    print(replaced)
    if inspect(replaced):
        my_mid_price = replaced
        dot(my_mid_price)
        await state.update_data(my_mid_price=my_mid_price)
        await message.answer(f"Теперь напишите какое количество акций на данный момент у Вас в портфеле", reply_markup=again)
        await Level.quality.set()
    else:
        await message.answer(f"{err}", reply_markup=again)




async def my_quality(message: Message, state: FSMContext):
    replaced = dot(message.text)
    print(replaced)
    if inspect(message.text):
        my_quality = replaced
        await state.update_data(my_quality=my_quality)
        await message.answer(f"Теперь напишите какая цена акции на данный момент", reply_markup=again)
        await Level.price_now.set()
    else:
        await message.answer(f"{err}", reply_markup=again)

async def my_price_now(message: Message, state: FSMContext):
    replaced = dot(message.text)
    print(replaced)
    if inspect(replaced):
        my_price_now = replaced
        await state.update_data(my_price_now=my_price_now)
        await message.answer(f"Теперь напишите сколько хотите преобрести акций для 'усреднения'", reply_markup=again)
        await Level.how_much.set()
    else:
        await message.answer(f"{err}", reply_markup=again)


async def finnaly(message: Message, state: FSMContext):
    replaced = dot(message.text)
    print(replaced)
    if inspect(replaced):
        how_much = replaced
        data = await state.get_data()
        mid_price = data.get('my_mid_price')
        data = await state.get_data()
        quality = data.get('my_quality')
        data = await state.get_data()
        price_now = data.get('my_price_now')
        my_finnaly = calcuate(float(mid_price), float(quality), float(price_now), float(how_much))
        await message.answer(f"Вы потратили  {my_finnaly[0]} на акции \n"
                         f"Средняя цена после 'усреднения'  {my_finnaly[1]}", reply_markup=again)
        await state.reset_state()
    else:
        await message.answer(f"{err}", reply_markup=again)


async def new_func(message: Message):
    await message.answer(f"Опишите какую функцию Вы хотели бы видеть в нашем боте", reply_markup=again)
    await Level.func.set()

async def write_func(message: Message):
    my_func = message.text
    BotDB.new_func(message.chat.id, message.chat.first_name, my_func)
    await message.answer(f"Спасибо {message.chat.first_name}, что помогаете нам развивать проект! \n"
                         f"Мы постараемся реализовать это в ближайшее время!", reply_markup=again)








def register_user(dp: Dispatcher):
    #Menu
    dp.register_message_handler(user_start, commands=["start"], state="*")
    dp.register_message_handler(user_again, text='Начать сначала', state="*")
    dp.register_message_handler(new_func, text='Предложить новую функцию', state="*")

    #Levels
    dp.register_message_handler(my_mid_price, state=Level.mid_price)
    dp.register_message_handler(my_quality, state=Level.quality)
    dp.register_message_handler(my_price_now, state=Level.price_now)
    dp.register_message_handler(finnaly, state=Level.how_much)

    dp.register_message_handler(write_func, state=Level.func)

