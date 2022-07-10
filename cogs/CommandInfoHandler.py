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
                        value=" 각 대륙의 모험의 서 요소에 대하여 정보를 알려줍니다.\n"
                              "ex) !모험의서 루테란 서부\n",
                        inline=False)

        embed.add_field(name="!군단장 [발탄, 비아키스, 쿠크세이튼, 아브렐슈드, 일리아칸, 카멘]",
                        value="각 군단장에 대한 패턴을 알려줍니다.\n"
                              "ex) !군단장 발탄",
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
                        value="각 캐릭터의 정보 링크를 호출합니다.\n"
                              "ex) !캐릭터정보 나비릴",
                        inline=False)

        embed.add_field(name="!경매 [파티인원] [가격 또는 각인서 이름]",
                        value="물품 금액에 대한 적절한 경매 입찰가를 출력합니다.\n"
                              "ex) !경매 4인 4800, !경매 8인 저받",
                        inline=False)

        embed.add_field(name="!시세요약 [범주]",
                        value="입력된 범주에 대한 시세가를 요약하여 출력합니다. 범주에 아무것도 없을 시 모든 데이터를 출력합니다.\n"
                              "ex) !시세요약, !시세요약 돌파석, !시세요약 재련재료",
                        inline=False)

        embed.add_field(name="!시세 [물품 이름]",
                        value="입력된 물품에 대한 시세를 검색하여 출력합니다. 축약어도 가능합니다.\n"
                              "ex) !시세 저주받은 인형, !시세 돌격대장",
                        inline=False)

        embed.add_field(name="!각인 [각인 이름]",
                        value="입력된 각인에 대한 정보를 출력합니다. 축약어도 가능합니다.\n"
                              "ex) !각인 저주받은 인형, !각인 돌대",
                        inline=False)

        embed.set_footer(text="건의사항 추가사항 받기 가능 그러나 반영 매우 늦음."
                              "각 정보의 경우 텍스트가 될 수도 있고 링크로도 올려질 수 있습니다.")

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(CommandInfoHandler(bot))