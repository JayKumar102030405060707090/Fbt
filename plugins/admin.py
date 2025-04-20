from pyrogram.types import Message
from database.models import get_all_users

async def admin_panel(client, message: Message):
    users = await get_all_users()
    text = "**Admin Panel**\n\nUsers:\n"
    async for user in users:
        text += f"• ID: `{user['_id']}` | Source: `{user.get('source')}` | Target: `{user.get('target')}`\n"
    await message.reply_text(text)