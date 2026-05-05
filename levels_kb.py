from aiogram.utils.keyboard import InlineKeyboardBuilder
from textbook_data import TEXTBOOKS

def get_levels_keyboard(book_key):
    builder = InlineKeyboardBuilder()
    
    book = TEXTBOOKS.get(book_key)
    if not book:
        return None
    
    if "direct_url" in book and not book["items"]:
        builder.button(text="📖 Открыть учебник", url=book["direct_url"])
    else:
        for level_key, level in book["items"].items():
            builder.button(text=level["name"], url=level["url"])
    
    builder.button(text="🔙 Назад", callback_data="textbooks")
    builder.button(text="🏠 Главное меню", callback_data="main_menu")
    
    builder.adjust(1)
    return builder.as_markup()

def get_start_here_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="📚 Перейти к учебникам", callback_data="textbooks")
    builder.button(text="🔙 Назад", callback_data="back_to_main")
    builder.button(text="🏠 Главное меню", callback_data="main_menu")
    builder.adjust(1)
    return builder.as_markup()

def get_about_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="📚 Перейти к учебникам", callback_data="textbooks")
    builder.button(text="🔙 Назад", callback_data="back_to_main")
    builder.button(text="🏠 Главное меню", callback_data="main_menu")
    builder.adjust(1)
    return builder.as_markup()