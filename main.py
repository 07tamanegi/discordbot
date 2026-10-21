import discord
import os
from discord.ext import commands
from keep_alive import keep_alive

class MyBot(commands.Bot):
    async def setup_hook(self):
        await self.load_extension("cogs.nitaname")
        await self.tree.sync()

intents = discord.Intents.default()
intents.message_content = True

bot = MyBot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"ログインしました: {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if "愛媛修飾" in message.content:
        await message.reply("後置修飾")
    if "徳島修飾" in message.content:
        await message.reply("後置修飾")
    if "後置修飾" in message.content:
        await message.reply("ありがとうございます:grin:")

TOKEN = os.getenv("DISCORD_TOKEN")
keep_alive()
bot.run(TOKEN)
