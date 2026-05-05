from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_main_menu_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="📚 Учебники", callback_data="textbooks")
    builder.button(text="🎯 С чего начать", callback_data="start_here")
    builder.button(text="ℹ️ О боте", callback_data="about")
    builder.adjust(1)
    return builder.as_markup()