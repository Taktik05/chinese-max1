from aiogram import Router, F
from aiogram.types import CallbackQuery, URLInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

# Прямые ссылки на изображения
HELP_IMAGES = {
    "textbooks": "https://raw.githubusercontent.com/Taktik05/chinese-max1/main/1uchebnik.png",
    "meaning": "https://raw.githubusercontent.com/Taktik05/chinese-max1/main/ieroglif.png",
    "pronunciation": "https://raw.githubusercontent.com/Taktik05/chinese-max1/main/proizn.png",
    "examples": "https://raw.githubusercontent.com/Taktik05/chinese-max1/main/prediya.png",
    "videos": "https://raw.githubusercontent.com/Taktik05/chinese-max1/main/video.png",
    "hsk": "https://raw.githubusercontent.com/Taktik05/chinese-max1/main/matHSK.png",
    "apps": "https://raw.githubusercontent.com/Taktik05/chinese-max1/main/pril.png"
}

def get_help_search_keyboard():
    """Клавиатура с 8 кнопками раздела помощи"""
    builder = InlineKeyboardBuilder()
    buttons = [
        "📘 Учебники", "🈶 Значение иероглифа", "🔊 Произношение",
        "📝 Примеры предложений", "🎥 Видеоуроки", "🎯 Материалы HSK",
        "📱 Приложения", "⬅️ Назад"
    ]
    for btn in buttons:
        if btn == "⬅️ Назад":
            callback_data = "back_to_main"
        elif btn == "📘 Учебники":
            callback_data = "help_textbooks"
        elif btn == "🈶 Значение иероглифа":
            callback_data = "help_meaning"
        elif btn == "🔊 Произношение":
            callback_data = "help_pronunciation"
        elif btn == "📝 Примеры предложений":
            callback_data = "help_examples"
        elif btn == "🎥 Видеоуроки":
            callback_data = "help_videos"
        elif btn == "🎯 Материалы HSK":
            callback_data = "help_hsk"
        elif btn == "📱 Приложения":
            callback_data = "help_apps"
        else:
            callback_data = "back_to_main"
        builder.button(text=btn, callback_data=callback_data)
    builder.adjust(2)
    return builder.as_markup()


@router.callback_query(F.data == "help_search")
async def show_help_search(callback: CallbackQuery):
    await callback.message.edit_text(
        "🔍 Помощь в поиске материалов\n\nВыберите, что вас интересует:",
        reply_markup=get_help_search_keyboard()
    )
    await callback.answer()


async def send_help_with_image(callback: CallbackQuery, image_key: str, text: str):
    """Отправляет фото + текст, потом удаляет старое сообщение (опционально)"""
    photo_url = HELP_IMAGES.get(image_key)
    if photo_url:
        photo = URLInputFile(photo_url)
        await callback.message.answer_photo(
            photo=photo,
            caption=text,
            reply_markup=get_help_search_keyboard()
        )
        # Удаляем старое сообщение с меню (чтобы не было каши)
        try:
            await callback.message.delete()
        except:
            pass
    else:
        await callback.message.edit_text(text, reply_markup=get_help_search_keyboard())
    await callback.answer()


@router.callback_query(F.data == "help_textbooks")
async def help_textbooks(callback: CallbackQuery):
    text = """📘 Как искать учебники по китайскому языку

Если нужного вам материала нет в нашем боте, то, чтобы найти нужный учебник, указывайте название серии, уровень и тип файла (PDF, workbook, audio).

Примеры запросов:
• HSK Standard Course 3 workbook PDF
• Integrated Chinese Level 2 audio
• Boya Chinese Beginner PDF
• Developing Chinese Intermediate workbook

Полезные ресурсы:
• Chinese Zero to Hero — https://www.zerotohero.ca
• HSK Academy — https://www.hsk.academy
• Google Books — https://books.google.com
• Internet Archive — https://archive.org
• ТГ канал с доп материалами — https://t.me/hsk4us (учебники)
• ТГ канал — https://t.me/bookchinese (сказки и рассказы на китайском)
• Методическая копилка для преподавателей — https://t.me/chineseppt

📌 Чем точнее запрос, тем быстрее вы найдете нужный материал."""
    await send_help_with_image(callback, "textbooks", text)


@router.callback_query(F.data == "help_meaning")
async def help_meaning(callback: CallbackQuery):
    text = """🈶 Как узнать значение иероглифа

Введите иероглиф в специализированный словарь, чтобы узнать значение, чтение, порядок черт и примеры употребления.

Полезные ресурсы:
• Pleco — https://www.pleco.com
• MDBG Chinese Dictionary — https://www.mdbg.net
• YellowBridge — https://www.yellowbridge.com
• TrainChinese — https://www.trainchinese.com
• StrokeOrder — https://www.strokeorder.com/
• 大БКРС — https://bkrs.info/

Примеры для поиска:
• 好
• 学
• 爱
• 朋友

📌 Изучайте не только перевод, но и примеры предложений."""
    await send_help_with_image(callback, "meaning", text)


@router.callback_query(F.data == "help_pronunciation")
async def help_pronunciation(callback: CallbackQuery):
    text = """🔊 Как проверить произношение

Найдите слово или иероглиф и прослушайте произношение носителя языка.

Полезные ресурсы:
• Forvo — https://forvo.com
• Pleco — https://www.pleco.com
• Google Translate — https://translate.google.com
• TrainChinese — https://www.trainchinese.com
• 大БКРС — https://bkrs.info/
• 懂中文 (тренировка тонов) — https://www.dong-chinese.com/learn/sounds/pinyin/toneTrainer

📌 Повторяйте вслух и сравнивайте своё произношение с оригиналом."""
    await send_help_with_image(callback, "pronunciation", text)


@router.callback_query(F.data == "help_examples")
async def help_examples(callback: CallbackQuery):
    text = """📝 Где искать примеры употребления слов

Введите слово в словарь или корпус, чтобы увидеть реальные предложения с переводом.

Полезные ресурсы:
• Tatoeba — https://tatoeba.org
• MDBG Chinese Dictionary — https://www.mdbg.net
• Reverso Context — https://context.reverso.net
• TrainChinese — https://www.trainchinese.com
• 大БКРС — https://bkrs.info/

📌 Изучение слов в контексте помогает быстрее запоминать лексику."""
    await send_help_with_image(callback, "examples", text)


@router.callback_query(F.data == "help_videos")
async def help_videos(callback: CallbackQuery):
    text = """🎥 Где искать видеоуроки

Видеоуроки помогают развивать аудирование, произношение и понимание грамматики.

Полезные ресурсы:
• Yoyo Chinese — https://www.yoyochinese.com
• Chinese Zero to Hero — https://www.zerotohero.ca
• Mandarin Corner — https://mandarincorner.org
• YouTube (курс HSK от Пекинского университета) — https://www.youtube.com/@learnchinese666

📌 Используйте видео как дополнение к учебникам и практике."""
    await send_help_with_image(callback, "videos", text)


@router.callback_query(F.data == "help_hsk")
async def help_hsk(callback: CallbackQuery):
    text = """🎯 Как искать материалы для HSK

Для подготовки к экзамену используйте ключевые слова: vocabulary, listening, workbook, mock test.

Примеры запросов:
• HSK 1 vocabulary PDF
• HSK 3 listening audio
• HSK 4 grammar guide
• HSK 5 mock tests

Полезные ресурсы:
• HSK Academy — https://www.hsk.academy
• Chinese Zero to Hero — https://www.zerotohero.ca
• HSK Standard Course — https://www.hskstandardcourse.com
• Mandarin Bean — https://mandarinbean.com

📌 Подбирайте материалы в соответствии со своим уровнем HSK."""
    await send_help_with_image(callback, "hsk", text)


@router.callback_query(F.data == "help_apps")
async def help_apps(callback: CallbackQuery):
    text = """📱 Рекомендуемые приложения

• Pleco — https://www.pleco.com
(словарь, карточки, примеры предложений)

• HelloChinese — https://www.hellochinese.cc
(интерактивные уроки и упражнения)

• Anki — https://apps.ankiweb.net
(карточки и интервальные повторения)

• Du Chinese — https://www.duchinese.net
(адаптированные тексты с озвучкой)

• Skritter — https://skritter.com
(практика написания иероглифов)

• TrainChinese — https://www.trainchinese.com
(словарь, примеры предложений и карточки)

📌 Используйте приложения для ежедневной практики и повторения."""
    await send_help_with_image(callback, "apps", text)
