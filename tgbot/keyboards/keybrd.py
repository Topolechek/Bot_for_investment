from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text=f'Начать сначала')
        ],
        [
            KeyboardButton(text='Предложить новую функцию')
        ],

    ],
    resize_keyboard=True
)

again = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text=f'Начать сначала')
        ]
    ],
    resize_keyboard=True
)

admin_kb = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text=f'Count')
        ],
        [
            KeyboardButton(text=f'Data')
        ],
        [
            KeyboardButton(text=f'News')
        ],
        [
            KeyboardButton(text=f'Начать сначала')
        ]
    ],
    resize_keyboard=True
)

