from aiogram.utils.keyboard import InlineKeyboardBuilder
from textbook_data import TEXTBOOKS

def get_textbooks_keyboard():
    builder = InlineKeyboardBuilder()
    
    for key, book in TEXTBOOKS.items():
        if key not in ["all_collection"]:
            builder.button(text=book["name"], callback_data=f"book_{key}")
    
    builder.button(text="📦 Вся копилка", callback_data="book_all_collection")
    builder.button(text="🔙 Назад", callback_data="back_to_main")
    builder.button(text="🏠 Главное меню", callback_data="main_menu")
    
    builder.adjust(1)
    return builder.as_markup()