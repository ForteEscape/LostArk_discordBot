import discord
from discord.ext import commands


class GuideContentHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 가이드(self, ctx, guide=None):
        if guide == None:
            embed = discord.Embed(title="!가이드 명령어 설명",
                                  description="!가이드 명령어에 대하여 설명합니다.")

            embed.add_field(name="!가이드 [육성, 아이템, 각인, 골드]",
                            value="육성의 경우 캐릭터 육성(또는 게임 전반적인 시스템)에 대하여 정보를 호출합니다.\n",
                            inline=False)

            embed.add_field(name="아이템",
                            value="아이템의 경우 아이템 세팅 방법 또는 아이템의 세트옵션 등에 대하여 정보를 호출합니다.\n",
                            inline=False)

            embed.add_field(name="각인",
                            value="각인의 경우 각인 세팅 방법 또는 각인 효과에 대하여 정보를 호출합니다.\n",
                            inline=False)

            embed.add_field(name="골드",
                            value="골드의 경우 골드 수급 방법에 대하여 정보를 호출합니다.")

            embed.set_footer(text="가이드의 경우 정보가 계속해서 추가됩니다.")

            await ctx.send(embed = embed)
        else:
            if guide == "육성":
                await ctx.send("육성 가이드 정보를 호출합니다\n"
                               "아이템 레벨 올리기(~1415까지)\n"
                               "https://arca.live/b/lostark/29674537?mode=best&p=1\n")

                await ctx.send("아이템 레벨 올리기 - 2\n"
                               "https://arca.live/b/lostark/29671166?mode=best&p=1\n")

            elif guide == "아이템":
                await ctx.send("아이템 가이드 정보를 호출합니다\n"
                               "1370 아르고스 아이템 어떤걸 맞춰야 하나요?\n"
                               "https://arca.live/b/lostark/29703275?mode=best&p=1")

            elif guide == "골드":
                await ctx.send("골드 수급처 - 1\n"
                               "https://arca.live/b/lostark/29692132?mode=best&p=1\n")

                await ctx.send("골드 수급처 - 2\n"
                               "https://arca.live/b/lostark/29700252?mode=best&p=1\n")

            elif guide == "각인":
                await ctx.send("각인 맞추기\n"
                               "https://arca.live/b/lostark/29683873?mode=best&p=1\n")

            else:
                await ctx.send(guide + " 부분의 가이드는 아직 제공되지 않았거나 존재하지 않는 부분입니다.")


def setup(bot):
    bot.add_cog(GuideContentHandler(bot))