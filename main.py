import asyncio
import signal
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN, SESSION_NAME
from core.handler import setup_handlers
from utils.logger import logger

bot = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def start_bot():
    await bot.start()
    await setup_handlers(bot)
    me = await bot.get_me()
    logger.info(f"Bot started as @{me.username}")
    await bot.send_message(me.id, f"✅ Bot started as @{me.username}")
    await asyncio.Event().wait()  # Keeps the bot running

async def shutdown(signal_name):
    logger.warning(f"Received {signal_name}. Shutting down bot...")
    await bot.stop()
    logger.info("Bot stopped gracefully.")

def main():
    loop = asyncio.get_event_loop()
    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(sig, lambda s=sig: asyncio.create_task(shutdown(s.name)))
    try:
        loop.run_until_complete(start_bot())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot terminated manually.")
    finally:
        loop.run_until_complete(shutdown("exit"))

if __name__ == "__main__":
    main()
