from os import getenv
from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dotenv import load_dotenv

load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher()
scheduler = AsyncIOScheduler()
