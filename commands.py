from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from main_menu_kb import get_main_menu_keyboard
router = Router()
async def show_start(message: Message):
    # ОДНО сообщение с приветствием, текстом и Inline-кнопками
    await message.answer(
        "👋 你好！Я MAX (麦克斯) - твой гид по китайскому языку!\n\n"
        "Выбирай раздел:",
        reply_markup=get_main_menu_keyboard()
    )
@router.message(Command("start"))
async def cmd_start(message: Message):
    # Reply-кнопка
    await message.answer(
        ".",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="🔄 Перезапустить")]],
            resize_keyboard=True
        )
    )
    # Основное сообщение с Inline-меню
    await show_start(message)
@router.message(F.text == "🔄 Перезапустить")
async def restart(message: Message):
    await show_start(message)
