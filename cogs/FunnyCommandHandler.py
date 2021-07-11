import discord
from discord.ext import commands


class FunnyCommandHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 곤란(self, ctx):
        embed = discord.Embed()
        embed.set_image(url="https://cdn.discordapp.com/attachments/863529285553618947/863708128659111956/KakaoTalk_20210711_072534641_01.jpg")
        await ctx.send(embed=embed)

    @commands.command()
    async def 분노(self, ctx):
        embed = discord.Embed()
        embed.set_image(url="https://cdn.discordapp.com/attachments/863529285553618947/863708126883610654/KakaoTalk_20210711_072534641.jpg")
        await ctx.send(embed=embed)

    @commands.command()
    async def 격분(self, ctx):
        embed = discord.Embed()
        embed.set_image(url="https://cdn.discordapp.com/attachments/863529285553618947/863708124901015572/KakaoTalk_20210711_072534641_03.jpg")
        await ctx.send(embed=embed)

    @commands.command()
    async def 칭찬(self, ctx):
        embed = discord.Embed()
        embed.set_image(url="https://cdn.discordapp.com/attachments/863529285553618947/863708118654255114/KakaoTalk_20210711_072534641_02.jpg")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(FunnyCommandHandler(bot))