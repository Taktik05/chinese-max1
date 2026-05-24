import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from commands import router as commands_router
from main_menu import router as main_menu_router
from textbooks import router as textbooks_router
from help_search import router as help_search_router

logging.basicConfig(level=logging.INFO)

async def main():
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN не найден в переменных окружения!")
        
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    
    dp.include_router(commands_router)
    dp.include_router(main_menu_router)
    dp.include_router(textbooks_router)
    dp.include_router(help_search_router)  # ДОБАВИТЬ
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
