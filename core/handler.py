from pyrogram import Client, filters
from pyrogram.types import Message

from plugins.commands import (
    start_authorization,
    show_features,
    setup_source_target,
    logout_user,
    configure_filters,
)
from core.forwarder import forward_message
from plugins.admin import admin_panel


async def setup_handlers(bot: Client):
    me = await bot.get_me()

    @bot.on_message(filters.command("authorize") & filters.private)
    async def handle_authorize(client: Client, message: Message):
        await start_authorization(client, message)

    @bot.on_message(filters.command("features") & filters.private)
    async def handle_features(client: Client, message: Message):
        await show_features(client, message)

    @bot.on_message(filters.command("setup") & filters.private)
    async def handle_setup(client: Client, message: Message):
        await setup_source_target(client, message)

    @bot.on_message(filters.command("filters") & filters.private)
    async def handle_filters(client: Client, message: Message):
        await configure_filters(client, message)

    @bot.on_message(filters.command("logout") & filters.private)
    async def handle_logout(client: Client, message: Message):
        await logout_user(client, message)

    @bot.on_message(filters.command("admin") & filters.user(me.id))
    async def handle_admin(client: Client, message: Message):
        await admin_panel(client, message)

    @bot.on_message(filters.private)
    async def handle_forward(client: Client, message: Message):
        await forward_message(client, message)
