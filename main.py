from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN, SESSION_NAME
from core.handler import setup_handlers
from utils.logger import logger

bot = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def main():
    await bot.start()
    await setup_handlers(bot)
    logger.info(f"Bot started as @{(await bot.get_me()).username}")
    await bot.idle()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
