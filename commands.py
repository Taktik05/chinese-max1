from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from main_menu_kb import get_main_menu_keyboard
router = Router()
@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "👋 你好！Я MAX (麦克斯) - твой гид по китайскому языку!",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="🔄 Перезапустить")]],
            resize_keyboard=True
        )
    )
    await message.answer(
        "📚 Выбирай раздел:",
        reply_markup=get_main_menu_keyboard()
    )
@router.message(F.text == "🔄 Перезапустить")
async def restart(message: Message):
    await message.answer(
        "📚 Выбирай раздел:",
        reply_markup=get_main_menu_keyboard()
    )
