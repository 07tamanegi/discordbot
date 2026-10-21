
import random
import discord
from discord import app_commands
from discord.ext import commands


class Futatsuna(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="futatsuna",
        description="あなたの二つ名をランダム生成します",
    )
    async def futatsuna(self, interaction: discord.Interaction):
        first = [
            "漆黒", "孤高", "混沌", "究極", "伝説",
            "爆速", "深夜テンション", "寝不足",
            "限界突破", "禁断", "無敵", "虚空",
            "絶対零度", "異次元", "全知全能",
            "歩く災害", "永遠の初心者", "伝説級の暇人"
        ]

        second = [
            "支配者", "破壊神", "覇者", "番人",
            "革命児", "錬金術師", "観測者",
            "最終兵器", "伝説", "申し子",
            "亡霊", "勇者", "天才", "ラスボス",
            "暇人", "寝落ちの王"
        ]

        title = f"{random.choice(first)}の{random.choice(second)}"

        embed = discord.Embed(
            title="二つ名メーカー",
            description=f"## {title}",
            color=discord.Color.purple()
        )
        embed.set_footer(
            text=f"生成者: {interaction.user.display_name}"
        )

        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Futatsuna(bot))
