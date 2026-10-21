import discord
import os
from discord.ext import commands
from keep_alive import keep_alive


GUILD_ID = 1360196681634807900  # 実際のサーバーIDに変更


class MyBot(commands.Bot):
    async def setup_hook(self):
        print("[起動] setup_hook開始")

        try:
            await self.load_extension("cogs.futatsuna")
            print("[成功] futatsuna.py読み込み完了")

            guild = discord.Object(id=GUILD_ID)

            self.tree.copy_global_to(guild=guild)
            synced = await self.tree.sync(guild=guild)

            print(f"[成功] 登録したコマンド数: {len(synced)}")
            print(f"[成功] コマンド名: {[cmd.name for cmd in synced]}")

        except Exception as e:
            print(f"[エラー] {type(e).__name__}: {e}")
            raise


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
        await message.reply("ありがとうございます😀")


TOKEN = os.getenv("DISCORD_TOKEN")

keep_alive()
bot.run(TOKEN)
