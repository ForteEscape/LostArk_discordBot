import discord
from discord.ext import commands


class CalenderHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 이벤트(self, ctx):
        await ctx.send("현재 진행되는 이벤트 페이지를 호출합니다.\n"
                       "https://lostark.game.onstove.com/News/Event/Now")

    @commands.command()
    async def 공지(self, ctx):
        await ctx.send("공지사항 페이지를 호출합니다.\n"
                       "https://lostark.game.onstove.com/News/Notice/List")

    @commands.command()
    async def 일정(self, ctx):
        embed = discord.Embed(title="로스트아크 필드보스, 모험 섬 출현 일정",
                              description="로스트아크 내 캘린더 필드보스 및 모험 섬 일정을 간략하게 이미지화합니다.")
        embed.set_image(url="https://cdn.discordapp.com/attachments/685396623483994185/862703916822429746/calander.jpg")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(CalenderHandler(bot))