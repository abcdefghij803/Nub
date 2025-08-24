import random
import string
import os
from os import getenv
import time
import pymongo
from telethon import TelegramClient, events, Button
from pyrogram import Client, filters
from thumbnails import *
from fonts import *

# Use getenv for all sensitive/configurable values
API_ID = os.getenv("API_ID","")
API_HASH = os.getenv("API_HASH", "")
STRING_SESSION = os.getenv("STRING_SESSION", "")
GROUP = os.getenv("GROUP", "nub_coder_s")
CHANNEL = os.getenv("CHANNEL", "nub_coders")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
OWNER_ID = int(os.getenv("OWNER_ID", 7789325573))
LOGGER_ID = os.getenv("LOGGER_ID", "-1002024032988")
mongodb = os.getenv("MONGODB_URI", "mongodb+srv://nubcoders:nubcoders@music.8rxlsum.mongodb.net/?retryWrites=true&w=majority&appName=music")
# Working directory
ggg = os.getcwd()

# Initialize data structures
# Track start time
StartTime = time.time()

# Set up MongoDB connection
mongo_client = pymongo.MongoClient(mongodb)
db = mongo_client['voice']
user_sessions = db['user_sessions']
collection = db["users"]
