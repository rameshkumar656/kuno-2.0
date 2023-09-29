from OpsAi import Ai
from AnonXMusic import app
from pyrogram import filters


@app.on_message(filters.command("ask"))
async def textt(_, message):
    	queri = message.text.split(None,1)[1]
    	print(queri)
    	gonb = Ai(query=queri)
    	await message.reply(gonb.chat())
