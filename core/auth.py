from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.errors import SessionPasswordNeededError
from config import API_ID, API_HASH, SESSION_DIR
import os

def get_session_name(phone):
    return os.path.join(SESSION_DIR, f"{phone}.session")

async def send_login_code(phone):
    client = TelegramClient(get_session_name(phone), API_ID, API_HASH)
    await client.connect()
    if not await client.is_user_authorized():
        sent = await client.send_code_request(phone)
        return sent.phone_code_hash
    await client.disconnect()
    return None

async def complete_login(phone, code, phone_code_hash, password=None):
    client = TelegramClient(get_session_name(phone), API_ID, API_HASH)
    await client.connect()
    if not await client.is_user_authorized():
        try:
            await client.sign_in(phone, code, phone_code_hash=phone_code_hash)
        except SessionPasswordNeededError:
            if password:
                await client.sign_in(password=password)
            else:
                return False
    return True