import discord
from discord.ext import commands


class FunnyCommandHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 곤란(self, ctx):
        embed = discord.Embed()
        embed.set_image(url="https://cdn.discordapp.com/attachments/685396623483994185/862703916822429746/calander.jpg")
        await ctx.send(embed=embed)

    @commands.command()
    async def 분노(self, ctx):
        embed = discord.Embed()
        embed.set_image(url="https://cdn.discordapp.com/attachments/685396623483994185/862703916822429746/calander.jpg")
        await ctx.send(embed=embed)

    @commands.command()
    async def 격분(self, ctx):
        embed = discord.Embed()
        embed.set_image(url="https://cdn.discordapp.com/attachments/685396623483994185/862703916822429746/calander.jpg")
        await ctx.send(embed=embed)

    @commands.command()
    async def 칭찬(self, ctx):
        embed = discord.Embed()
        embed.set_image(url="https://cdn.discordapp.com/attachments/685396623483994185/862703916822429746/calander.jpg")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(FunnyCommandHandler(bot))