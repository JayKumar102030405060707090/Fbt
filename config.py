import os
from dotenv import load_dotenv

load_dotenv()
OWNER_ID = int(os.getenv("OWNER_ID", "7168729089"))
API_ID = int(os.getenv("API_ID", 20882859))
API_HASH = os.getenv("API_HASH", "7c8f0bd8aa7be4af2a02492f9a807778")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7131160767:AAF220cVpiwmsnIgQly9nGBaaZiqokgNWzc")
SESSION_NAME = os.getenv("SESSION_NAME", "auto_forwarder_bot")
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://jaydipmore74:xCpTm5OPAfRKYnif@cluster0.5jo18.mongodb.net/?retryWrites=true&w=majority")
SESSION_DIR = os.getenv("SESSION_DIR", "./sessions")
