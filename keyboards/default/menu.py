from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


menu_buttons=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Sherik kerak"),
            KeyboardButton(text="Ishjoyi kerak"),
        ],
        [
            KeyboardButton(text="Hodim kerak"),
            KeyboardButton(text="Ustoz kerak")
        ],
        [
            KeyboardButton(text="shogird kerak")
        ]
    ],
    resize_keyboard=True,
)