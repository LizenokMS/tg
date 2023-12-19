from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token="secret")
dp = Dispatcher(bot)

with open ("zadaniya.txt", "r", encoding="utf-8") as file:
    students = [line.rstrip("\n")  for line in file]
    students = list(filter(None, students))
print(students)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    buttons = [
        [types.KeyboardButton(text="Help")],
        [types.KeyboardButton(text="Что-то")]
               ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=buttons,
                                         resize_keyboard=True)

    await message.answer(text="🏆Привет, <em>я бот</em>",
                         parse_mode="HTML",
                         reply_markup=keyboard)

HELP_COMMAND = """Этот бот даст задание каждому студенту на зачет🫡
Нажмите /start, чтобы начать работу.
/help - список команд💥
/start - начать работу💥
"""

@dp.message_handler(lambda message: message.text == "Help")
async def help1_command(message: types.Message):
    await message.answer(text=HELP_COMMAND, parse_mode="HTML")
    await message.delete()
    
@dp.message_handler(commands=["help"])
async def help2_command(message: types.Message):
    await message.answer(text=HELP_COMMAND, parse_mode="HTML")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
