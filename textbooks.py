from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile
from levels_kb import get_levels_keyboard
from textbook_data import TEXTBOOKS
from images_data import TEXTBOOK_IMAGES
import os

router = Router()

@router.callback_query(F.data.startswith("book_"))
async def show_book_levels(callback: CallbackQuery):
    book_key = callback.data.replace("book_", "")
    
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
    
    image_path = TEXTBOOK_IMAGES.get(book_key)
    if image_path and os.path.exists(image_path):
        # Отправляем новое сообщение с фото ВСЕГДА
        await callback.message.answer_photo(
            photo=FSInputFile(image_path),
            caption=text,
            reply_markup=get_levels_keyboard(book_key)
        )
    else:
        # Для "Вся копилка" и Integrated Chinese - просто текст
        await callback.message.answer(
            text,
            reply_markup=get_levels_keyboard(book_key)
        )
    
    await callback.answer()