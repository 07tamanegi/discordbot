```python
import discord
import os
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if "愛媛修飾" in message.content:
        await message.reply("後置修飾")
    if "徳島修飾" in message.content:
        await message.reply("後置修飾")
    if "後置修飾" in message.content:
        await message.reply("ありがとうございます😁")

TOKEN = os.getenv("DISCORD_TOKEN")

# Webサーバの立ち上げ
keep_alive()

client.run(TOKEN)
```
