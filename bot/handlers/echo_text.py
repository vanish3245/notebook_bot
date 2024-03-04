from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import State, StatesGroup

# from bot.handlers.database import save_user_data


router = Router()


@router.message(Command('start'))
async def products(message: Message):
    await message.answer(text='HI')


# @router.callback_query(F.data == 'products')
# async def call_products(call: CallbackQuery):
#     await call.message.answer(text='Круто!')

# @router.callback_query(Pagination.filter())
# async def pagination_handlers(call: CallbackQuery, callback_data: Pagination):
#     num = callback_data.page
#     page = int(callback_data.page)

#     if callback_data.action == 'next':
#         if num < 2:
#             num += 1
#         else:
#             num = 2
#     else:
#         if num > 1:
#             num -= 1
#         else:
#             num = 1

#     await call.message.edit_reply_markup(reply_markup=products_progress(num, page))



# class Form(StatesGroup):
#     name = State()
#     age = State()
#     about = State()
#     photo = State()

# @router.message(Command('profile'))
# async def registr(message: Message, state: FSMContext):
#     await state.set_state(Form.name)
#     await message.answer('Как тебя зовут?')


# @router.message(Form.name)
# async def form_name(message: Message, state: FSMContext):
#     await state.update_data(name=message.text)
#     await state.set_state(Form.age)
#     await message.answer('Скольлко тебе лет?')



# @router.message(Form.age)
# async def from_age(message: Message, state: FSMContext):
#     await state.update_data(age=int(message.text))
#     data = await state.get_data()
#     await state.clear()

#     save_user_data(data)
#     await message.answer(f"Привет: {data['name']}\nТебе: {data['age']} лет")

# @router.message(Command('time'))
# async def time_message(message: Message):
#     await message.answer(text='Каждую минуту будет отправляться напоминание', reply_markup=time_progress())


# async def send_hello_message(call: CallbackQuery):
#     while user['in_time_message']:
#         await call.message.answer(text='Привет')
#         await asyncio.sleep(60)

# @router.callback_query(lambda c: c.data == 'time_one')
# async def time_1(call: CallbackQuery):
#     global user

#     if not user['in_time_message']:
#         user['in_time_message'] = True
#         asyncio.create_task(send_hello_message(call))
#     else:
#         user['in_time_message'] = False
#         await call.message.answer('Напоминание отключено')


@router.message()
async def echo(message: Message):
    await message.answer(message.text)

