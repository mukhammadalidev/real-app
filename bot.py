from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Web ochish 🌐",
                web_app=WebAppInfo(url="https://saytingiz.uz")
            )
        ]
    ]
)
