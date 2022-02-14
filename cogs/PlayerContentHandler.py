import discord
from discord.ext import commands


class PlayerContentHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 캐릭터정보(self, ctx, player=None):
        player_nickname_list = [
            ['아득바득연구소', '나비릴', '노비릴'],
            ['릴리찐따', '릴찐'],
            ['퍽피', '풀피', '소세지', '퍽피', '대학원생'],
            ['윗집층간소음민폐녀', '누무누무', '누쿠', '노쿠'],
            ['그루톤코인샵', '캬떡', '쌀떡'],
            ['쮸오옥', '차비'],
            ['마마레후', '마마'],
            ['2nd컴패니언', '컴패', '야스치이'],
            ['210301시작', '워붕쿤', '워붕이'],
            ['대쥬인', '대주인', '머주', '대주'],
            ['우한실유통', '나그없'],
            ['체리맛나는건슬', '체맛건'],
            ['MaiR', '따별'],
            ['어흥펀치다냥', '댕루'],
            ['맛있는새운매우깡', '우깡'],
            ['아기댕쟝', '뭉클'],
            ['감귤농장상남자', '귤남'],
            ['네코마츠리', '티인'],
        ]

        nickname = player
        for nicknameList in player_nickname_list:
            if player in nicknameList:
                player = nicknameList[0]

        if player is None:
            embed = discord.Embed(title="!캐릭터정보 명령어 설명",
                                  description="!캐릭터정보 명령어에 대하여 설명합니다.")
            embed.add_field(name="!캐릭터정보 [누쿠누쿠, 차차]",
                            value="각 캐릭터의 정보 링크를 호출합니다.\n"
                                  "사용 가능한 이름들\n"
                                  "======================================\n"
                                  "유파민, 나비릴, 릴리찐따, 풀피, 누쿠누쿠, 차차, 댕루, 우깡, 절정각인서, 체맛건, 귤남, 쌀떡, 따별, 차비, 고희원\n"
                                  "뭉클, 마마, 워붕쿤, 티인, 야스치이, 대주인, 나그없")
            await ctx.send(embed=embed)
        else:
            await ctx.send(nickname + ' 의 정보를 호출합니다.\n' + 'https://www.mgx.kr/lostark/character/?character_name=' + player)

    @commands.command()
    async def 길드정보(self, ctx, guild=None):
        if guild == None:
            embed = discord.Embed(title="!길드정보 명령어 설명",
                                  description="!길드정보 명령어에 대하여 설명합니다.")
            embed.add_field(name="!길드정보 [아이엠말보로]",
                            value="입력으로 받은 길드의 정보를 호출합니다.")

            await ctx.send(embed=embed)
        else:
            await ctx.send(guild + ' 길드의 정보를 호출합니다.\n' + 'https://www.mgx.kr/lostark/guild/search/?guild_name=' + guild)


def setup(bot):
    bot.add_cog(PlayerContentHandler(bot))