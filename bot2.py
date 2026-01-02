import logging
import requests
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "8520082855:AAFnQ_MbV17MJhPSTQNVq5tm3pnuXx-xiWo"
API_URL = "http://buxoroda-ish.uz/advertisements/channel/"  # o'zingnikiga almashtir

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# Faqat CHANNEL postlari uchun
@dp.channel_post_handler()
async def channel_text_handler(message: types.Message):
    if not message.text:
        return  # faqat TEXT

    payload = {
        "text": message.text
    }

    try:
        r = requests.post(API_URL, json=payload, timeout=10)
        print("✅ Yuborildi | Status:", r.status_code)
    except Exception as e:
        print("❌ Xatolik:", e)


if __name__ == "__main__":
    print("🚀 Aiogram 2.25.1 TEXT scrapper bot ishga tushdi")
    executor.start_polling(dp, skip_updates=True)
