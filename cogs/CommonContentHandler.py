import discord
from discord.ext import commands


class CommonContentHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 어비스던전(self, ctx, map=None):
        if map == None:
            embed = discord.Embed(title="!어비스던전 명령어 설명",
                                  description="!어비스던전 명령어에 대하여 설명합니다.")
            embed.add_field(name="!어비스던전 [낙원의문, 낙원, 오레하의우물, 오레하]",
                            value="각 어비스 던전의 공략을 호출합니다.\n"
                                  "ex) !어비스던전 오레하의우물 or !어비스던전 오레하")
            await ctx.send(embed=embed)
        else:
            if map == '낙원의문' or map == '낙원':
                await ctx.send(map + "어비스 던전에 대한 공략을 호출합니다\n"
                                     "낙원의 문 - 고요한 카르코사 공략"
                                     "https://www.youtube.com/watch?v=SvlfZQ8Krck&list=PLCGjmOutsfSiR6abIKMsiBTcHn4FfPuCP&index=4\n"
                                     "낙원의 문 - 태만의 바다 공략\n"
                                     "https://www.youtube.com/watch?v=Bb09UbKpynE&list=PLCGjmOutsfSiR6abIKMsiBTcHn4FfPuCP&index=3\n"
                                     "낙원의 문 - 아르카디아의 성역 공략\n"
                                     "https://www.youtube.com/watch?v=assmuJkN6-w&list=PLCGjmOutsfSiR6abIKMsiBTcHn4FfPuCP&index=1")
            elif map == '오레하' or map == '오레하의우물':
                await ctx.send(map + "어비스 던전에 대한 공략을 호출합니다\n"
                                     "오레하의 우물 - 아이라의 눈 공략\n"
                                     "https://www.youtube.com/watch?v=sbvDCi9nCVk&list=PLCGjmOutsfSiR6abIKMsiBTcHn4FfPuCP&index=10\n"
                                     "오레하의 우물 - 오레하 프라바사 공략\n"
                                     "https://www.youtube.com/watch?v=Sr7jyZvhhUs&list=PLCGjmOutsfSiR6abIKMsiBTcHn4FfPuCP&index=11")
            else:
                await ctx.send(map + "어비스 던전은 존재하지 않거나 자료부족으로 아직 추가되지 않았습니다.")

    @commands.command()
    async def 어비스레이드(self, ctx, named=None):
        if named == None:
            embed = discord.Embed(title="!어비스레이드 명령어 설명",
                                  description="!어비스레이드 명령어에 대하여 설명합니다.")
            embed.add_field(name="!어비스레이드 [아르고스]",
                            value="각 어비스 레이드 보스몹의 공략을 호출합니다.\n"
                                  "ex) !어비스레이드 아르고스")
            await ctx.send(embed=embed)
        else:
            if named == '아르고스' or named == '노르고스' or named == '노르고슨':
                await ctx.send("아르고스 레이드에 대한 정보를 호출합니다\n"
                               "아르고스 - 1페이즈 공략\n"
                               "https://www.youtube.com/watch?v=EwAUycmaZVs&list=PLCGjmOutsfSiR6abIKMsiBTcHn4FfPuCP&index=5\n"
                               "아르고스 - 2페이즈 공략\n"
                               "https://www.youtube.com/watch?v=FG9F6on4LAY&list=PLCGjmOutsfSiR6abIKMsiBTcHn4FfPuCP&index=12\n"
                               "아르고스 - 3페이즈 공략\n"
                               "https://www.youtube.com/watch?v=hCncYVwjlDY&list=PLCGjmOutsfSiR6abIKMsiBTcHn4FfPuCP&index=13")


def setup(bot):
    bot.add_cog(CommonContentHandler(bot))