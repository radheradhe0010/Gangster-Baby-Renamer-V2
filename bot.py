import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6918817305:AAFecywHiuvIROIcNxQyyZZu86K3wHgAGPc")

API_ID = int(os.environ.get("API_ID", "23657837"))

API_HASH = os.environ.get("API_HASH", "d90bf753f0578c231a458fbb2d023e6f")

STRING = os.environ.get("STRING", "@renamer_all_bot")



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
