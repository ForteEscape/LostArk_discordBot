import discord
from discord.ext import commands


class BotUpdateLogHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def log(self, ctx):
        embed = discord.Embed(title="LOA_help 디스코드 봇 업데이트 내역",
                              description="디스코드 봇 업데이트 기록 내역입니다.")

        embed.add_field(name="1.0v 업데이트",
                        value="디스코드 봇 구동시작, 모험의 서, 내실, 명령어 설명 추가",
                        inline=False)

        embed.add_field(name="1.1v 업데이트",
                        value="어비스 레이드, 어비스 던전 기능 추가, 각 명령어에 추가 입력 없을 시 명령어 설명 표시 설정\n"
                              "오탈자 개선",
                        inline=False)

        embed.add_field(name="1.2v 업데이트",
                        value="군단장 레이드 부분 기능 추가(리허설 등의 세부설정), 군단장 쿠크세이튼 정보 추가",
                        inline=False)

        embed.add_field(name="1.3v 업데이트",
                        value="내부 코드 구조 개선 - 여러 개의 핸들러 클래스로 각 클래스당 맡는 명령어 분배 및 모듈화\n",
                        inline=False)

        embed.add_field(name="1.4v 업데이트",
                        value="가이드, 이스터에그 기능 추가\n",
                        inline=False)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(BotUpdateLogHandler(bot))