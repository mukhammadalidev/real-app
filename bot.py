import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils import executor

API_TOKEN = "8447269525:AAG7IoTDoREtZOHeu33fOc6qARESqDWe4is"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Web App ochish 🌐",
                    web_app=WebAppInfo(url="https://buxoroda-ish.uz")
                )
            ]
        ]
    )
    await message.answer("Web Appga kirish uchun tugmani bosing:", reply_markup=keyboard)

@dp.message_handler(content_types=types.ContentType.WEB_APP_DATA)
async def web_app_data(message: types.Message):
    data = message.web_app_data.data
    await message.answer(f"Webdan kelgan data: {data}")

if __name__ == "__main__":
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
