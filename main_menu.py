from aiogram import Router, F
from aiogram.types import CallbackQuery
from main_menu_kb import get_main_menu_keyboard
from textbooks_kb import get_textbooks_keyboard
from levels_kb import get_start_here_keyboard, get_about_keyboard
from info_data import START_HERE_TEXT, ABOUT_TEXT

router = Router()

@router.callback_query(F.data == "main_menu")
async def show_main_menu(callback: CallbackQuery):
    await callback.message.answer(
        "👋 你好！Я MAX (麦克斯) - твой гид по китайскому языку!\n\n"
        "Выбирай раздел:",
        reply_markup=get_main_menu_keyboard()
    )
    await callback.answer()

@router.callback_query(F.data == "back_to_main")
async def back_to_main(callback: CallbackQuery):
    await callback.message.answer(
        "👋 你好！Я MAX (麦克斯) - твой гид по китайскому языку!\n\n"
        "Выбирай раздел:",
        reply_markup=get_main_menu_keyboard()
    )
    await callback.answer()

@router.callback_query(F.data == "textbooks")
async def show_textbooks(callback: CallbackQuery):
    await callback.message.answer(
        "📚 Выбери серию учебников:",
        reply_markup=get_textbooks_keyboard()
    )
    await callback.answer()

@router.callback_query(F.data == "start_here")
async def show_start_here(callback: CallbackQuery):
    await callback.message.answer(
        START_HERE_TEXT,
        reply_markup=get_start_here_keyboard()
    )
    await callback.answer()

@router.callback_query(F.data == "about")
async def show_about(callback: CallbackQuery):
    await callback.message.answer(
        ABOUT_TEXT,
@router.callback_query(F.data == "feedback")
async def show_feedback(callback: CallbackQuery):
    text = """📝 Обратная связь

Спасибо за использование бота MAX (麦克斯 mài kè sī)

Ваше мнение поможет нам улучшить содержание бота, сделать навигацию удобнее и добавить новые полезные материалы.

Пожалуйста, уделите 2–3 минуты для прохождения небольшой анкеты.

🔗 Ссылка на форму:
https://forms.yandex.ru/u/6a20e0f8068ff076339986a3

Заранее спасибо! 🙏"""
    
    # Создаём клавиатуру с кнопкой "Назад"
    from aiogram.utils.keyboard import InlineKeyboardBuilder
    builder = InlineKeyboardBuilder()
    builder.button(text="🔙 Назад", callback_data="back_to_main")
    builder.button(text="🏠 Главное меню", callback_data="main_menu")
    builder.adjust(1)
    
    await callback.message.edit_text(text, reply_markup=builder.as_markup())
    await callback.answer()
        reply_markup=get_about_keyboard()
    )
    await callback.answer()
