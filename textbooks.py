from aiogram import Router, F
from aiogram.types import CallbackQuery
from levels_kb import get_levels_keyboard
from textbook_data import TEXTBOOKS

router = Router()

@router.callback_query(F.data.startswith("book_"))
async def show_book_levels(callback: CallbackQuery):
    book_key = callback.data.replace("book_", "")
    
    if book_key == "all_collection":
        await callback.message.edit_text(
            "📦 Полный сборник всех материалов по китайскому языку.\n\n"
            "Нажми на кнопку ниже, чтобы открыть:",
            reply_markup=get_levels_keyboard(book_key)
        )
        await callback.answer()
        return
    
    book = TEXTBOOKS.get(book_key)
    if not book:
        await callback.answer("❌ Учебник не найден", show_alert=True)
        return
    
    text = f"📚 {book['name']}\n📝 {book['description']}\n\n"
    
    if "direct_url" in book and not book["items"]:
        text += "Нажми на кнопку ниже, чтобы открыть учебник:"
    else:
        text += "Выбери уровень:"
        for level_key, level in book["items"].items():
            text += f"\n• {level['name']} - {level['description']}"
    
    await callback.message.edit_text(
        text,
        reply_markup=get_levels_keyboard(book_key)
    )
    await callback.answer()