from pyrogram import Client, filters
from plugins.commands import start_authorization, show_features, setup_source_target, logout_user, configure_filters
from core.forwarder import forward_message
from plugins.admin import admin_panel

def setup_handlers(bot: Client):
    bot.add_handler(filters.command("authorize") & filters.private, start_authorization)
    bot.add_handler(filters.command("features") & filters.private, show_features)
    bot.add_handler(filters.command("setup") & filters.private, setup_source_target)
    bot.add_handler(filters.command("filters") & filters.private, configure_filters)
    bot.add_handler(filters.command("logout") & filters.private, logout_user)
    bot.add_handler(filters.command("admin") & filters.user(bot.me.id), admin_panel)

    bot.add_handler(filters.all & filters.private, forward_message)