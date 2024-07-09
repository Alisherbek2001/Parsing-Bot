import asyncio
import logging
import sys
from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Message
from function import parse_post
from api import create_post
import aiohttp

load_dotenv()

TOKEN = getenv("BOT_TOKEN")
CHANNEL_ID = getenv("CHANNEL_ID")

if not TOKEN:
    raise ValueError("BOT_TOKEN topilmadi. .env faylini tekshiring.")
if not CHANNEL_ID:
    raise ValueError("CHANNEL_ID topilmadi. .env faylini tekshiring.")

dp = Dispatcher()

async def download_file(bot: Bot, file_id: str):
    file = await bot.get_file(file_id)
    file_path = file.file_path
    file_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(file_url) as resp:
            if resp.status == 200:
                return await resp.read()
    return None

@dp.channel_post()
async def handle_channel_post(message: Message, bot: Bot) -> None:
    """
    Bu handler kanalga yuborilgan har qanday postni qabul qiladi
    """
    if message.text:
        data = parse_post(message.text)
        title = data['title']
        description = data['description']
        result = create_post(title=title, description=description, file=None)
    elif message.photo:
        data = parse_post(message.caption)
        title = data['title']
        description = data['description']
        file_content = await download_file(bot, message.photo[-1].file_id)
        if file_content:
            result = create_post(title=title, description=description, file=('image.jpg', file_content, 'image/jpeg'))
        else:
            logging.error("Rasmni yuklab olishda xatolik")
            return
    else:
        logging.info("Qo'llab-quvvatlanmaydigan xabar turi")
        return

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    
    await bot.get_updates(offset=-1)
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())