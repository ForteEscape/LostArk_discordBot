import discord
from discord.ext import commands


class BossRaidContentHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 군단장(self, ctx, bossname=None, status=None):
        if bossname == None:
            embed = discord.Embed(title="!군단장 명령어 설명",
                                  description="!군단장 명령어에 대하여 설명합니다.")
            embed.add_field(name="!군단장 [발탄, 비아키스, 쿠크세이튼 리허설, 쿠크세이튼]",
                            value="각 군단장의 공략을 호출합니다.\n"
                                  "ex) !군단장 발탄 or !군단장 쿠크세이튼 리허설")
            await ctx.send(embed=embed)
        else:
            if bossname == "발탄" and status == None:
                await ctx.send("마수군단장 발탄에 대한 정보를 호출합니다,\n"
                               "1네임드 공략\n"
                               "https://www.youtube.com/watch?v=YNf2my7id-A&list=PLCGjmOutsfSiR6abIKMsiBTcHn4FfPuCP&index=14\n"
                               "2네임드 공략\n"
                               "https://www.youtube.com/watch?v=LakcTJ7lmgw&list=PLCGjmOutsfSiR6abIKMsiBTcHn4FfPuCP&index=15")
            elif bossname == "비아키스" and status == None:
                await ctx.send("욕망군단장 비아키스에 대한 정보를 호출합니다.\n"
                               "1네임드 공략\n"
                               "https://www.youtube.com/watch?v=RRxHRHWyp-Q&list=PLCGjmOutsfSiR6abIKMsiBTcHn4FfPuCP&index=17\n"
                               "2네임드 공략\n"
                               "https://www.youtube.com/watch?v=lLgvOOt3DSA&list=PLCGjmOutsfSiR6abIKMsiBTcHn4FfPuCP&index=18\n"
                               "3네임드 공략]\n"
                               "https://www.youtube.com/watch?v=GtVyd7N9M2Q&list=PLCGjmOutsfSiR6abIKMsiBTcHn4FfPuCP&index=19")
            elif bossname == "쿠크세이튼" and status == '리허설':
                await ctx.send("쿠크세이튼 리허설에 대한 정보를 호출합니다\n"
                               "1, 2네임드 공략\n"
                               "https://www.youtube.com/watch?v=c2jxXRDdoxI&list=PLiVteFwxYZPy-34x6a490B7oTFG5jI9Su&index=7\n"
                               "3네임드 공략\n"
                               "https://www.youtube.com/watch?v=XqhybgmXg1Q&list=PLiVteFwxYZPy-34x6a490B7oTFG5jI9Su&index=8")
            elif bossname == "쿠크세이튼":
                await ctx.send("쿠크세이튼 노말에 대한 정보를 호출합니다.\n"
                               "1네임드 공략\n"
                               "https://www.youtube.com/watch?v=Y1I19YwJuIY&list=PLCGjmOutsfSiR6abIKMsiBTcHn4FfPuCP&index=22\n"
                               "2네임드 공략\n"
                               "https://www.youtube.com/watch?v=pS81SiezMcc&list=PLCGjmOutsfSiR6abIKMsiBTcHn4FfPuCP&index=23\n"
                               "3네임드 공략\n"
                               "https://www.youtube.com/watch?v=YHiJToAhGZ0&list=PLCGjmOutsfSiR6abIKMsiBTcHn4FfPuCP&index=26\n"
                               "마리오패턴 공략\n"
                               "https://www.youtube.com/watch?v=CtzrlAifmeI&list=PLCGjmOutsfSiR6abIKMsiBTcHn4FfPuCP&index=25")


def setup(bot):
    bot.add_cog(BossRaidContentHandler(bot))