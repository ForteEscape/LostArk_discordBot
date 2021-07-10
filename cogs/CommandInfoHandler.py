import discord
from discord.ext import commands


class CommandInfoHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 명령어(self, ctx):
        embed = discord.Embed(title="LOA_helper봇 명령어",
                              description="로스트아크 정보 알려주기 귀찮아서 만듬")
        embed.add_field(name="  !내실 [거심, 섬마, 미술품, 오르페우스, 항해물, 스킬포인트]",
                        value="내실 관련 정보 출력, 각 내실 포인트의 수급처를 알려줍니다.\n"
                              "스킬 포인트의 경우 스킬 포인트의 수급처를 알려줍니다.\n"
                              "ex) !내실 오르페우스",
                        inline=False)

        embed.add_field(name="  !모험의서 [대륙 이름]",
                        value=" 각 대륙의 모험의 서 요소에 대하여 정보를 알려줍니다. 이때 베른 북부, 루테란 동부 등의 띄어쓰기는 모두 붙여서 씁니다.\n"
                              "ex) !모험의서 루테란서부\n",
                        inline=False)

        embed.add_field(name="!군단장 [발탄, 비아키스, 쿠크세이튼, 아브렐슈드, 일리아칸, 카멘]",
                        value="각 군단장에 대한 패턴을 알려줍니다.\n"
                              "ex) !군단장 발탄",
                        inline=False)

        embed.add_field(name="!이벤트",
                        value="현재 진행되는 이벤트가 모인 이벤트 페이지 링크를 호출합니다..\n"
                              "ex) !이벤트",
                        inline=False)

        embed.add_field(name="!어비스던전 [오레하의우물, 오레하, 낙원의문, 낙원]",
                        value="각 어비스 던전의 정보를 호출합니다.\n"
                              "ex) !어비스던전 오레하 or !어비스던전 오레하의우물",
                        inline=False)

        embed.add_field(name="!어비스레이드 [아르고스]",
                        value="각 어비스 레이드 보스몹의 정보를 호출합니다.\n"
                              "ex) !어비스레이드 아르고스",
                        inline=False)

        embed.add_field(name="!캐릭터정보 [누쿠누쿠, 차차]",
                        value="각 캐릭터의 정보 링크를 호출합니다..\n"
                              "ex) !캐릭터정보 나비릴")

        embed.set_footer(text="건의사항 추가사항 받기 가능 그러나 반영 매우 늦음."
                              "각 정보의 경우 텍스트가 될 수도 있고 링크로도 올려질 수 있습니다.")

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(CommandInfoHandler(bot))