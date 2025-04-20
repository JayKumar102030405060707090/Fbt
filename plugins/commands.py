from pyrogram import Client, filters
from pyrogram.types import Message
from database.models import save_user, save_user_settings, get_user_settings
from core.auth import send_login_code, complete_login

sessions = {}

async def start_authorization(client: Client, message: Message):
    await message.reply_text("Please send your phone number (with country code).")
    sessions[message.from_user.id] = {"step": "awaiting_phone"}

async def show_features(client: Client, message: Message):
    text = (
        "**Bot Features:**\n"
        "• Secure login with phone number\n"
        "• Set source/target by pinning\n"
        "• Real-time auto-forwarding (all media)\n"
        "• Filters: regex, hashtags, prepend/append\n"
        "• Admin panel for managing users\n"
        "• Heroku/Docker deploy support"
    )
    await message.reply_text(text)

async def setup_source_target(client: Client, message: Message):
    await message.reply_text("Pin the **source chat** and send me a message from it.")
    sessions[message.from_user.id] = {"step": "awaiting_source"}

async def configure_filters(client: Client, message: Message):
    await message.reply_text("Send filters in JSON format. Example:\n"
        "`{\"regex_replace\": {\"old\": \"new\"}, \"hashtags\": [\"#tag\"], \"prepend\": \"[Prefix] \", \"append\": \" [Suffix]\"}`")
    sessions[message.from_user.id] = {"step": "awaiting_filters"}

async def logout_user(client: Client, message: Message):
    from database.models import delete_user
    await delete_user(message.from_user.id)
    await message.reply_text("Logged out and session removed.")