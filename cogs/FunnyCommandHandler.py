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

    @commands.command()
    async def 웃프네요(self, ctx):
        embed = discord.Embed()
        embed.set_image(url="https://cdn.discordapp.com/attachments/863529285553618947/864593966389657660/ff5204660b3192f7.png")
        await ctx.send(embed=embed)

    @commands.command()
    async def 웃음(self, ctx):
        embed = discord.Embed()
        embed.set_image(url="https://cdn.discordapp.com/attachments/863529285553618947/864593973976760320/c5efe7d8b57fa748.png")
        await ctx.send(embed=embed)

    @commands.command()
    async def 인사(self, ctx):
        embed = discord.Embed()
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/863529285553618947/864593976366465084/a3fb08af21b05254.png")
        await ctx.send(embed=embed)

    @commands.command()
    async def 슬픔(self, ctx):
        embed = discord.Embed()
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/863529285553618947/864593978196099092/ca70b83f7e1269a4.png")
        await ctx.send(embed=embed)

    @commands.command()
    async def 참담(self, ctx):
        embed = discord.Embed()
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/863529285553618947/864594482380668928/afff2f1c589e0b0c.png")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(FunnyCommandHandler(bot))