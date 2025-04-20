from pyrogram import Client, filters
from database.models import get_user_settings
from utils.helpers import transform_message

async def forward_message(client, message):
    user_id = message.from_user.id
    settings = await get_user_settings(user_id)

    if not settings or not settings.get("source") or not settings.get("target"):
        return

    if str(message.chat.id) != str(settings["source"]):
        return

    text = await transform_message(message.text or "", settings.get("filters", {}))
    await client.copy_message(
        chat_id=settings["target"],
        from_chat_id=message.chat.id,
        message_id=message.message_id,
        caption=text or message.caption
    )