from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN, SESSION_NAME
from core.handler import setup_handlers
from utils.logger import logger

bot = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

if __name__ == "__main__":
    setup_handlers(bot)
    logger.info("Bot is starting...")
    bot.run()