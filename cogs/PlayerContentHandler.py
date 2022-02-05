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

        """
        player_dic = {'유파민': 'https://loawa.com/char/%EC%9C%A0%ED%8C%8C%EB%AF%BC',
                      '나비릴': 'https://loawa.com/char/%EC%95%84%EB%93%9D%EB%B0%94%EB%93%9D%EC%97%B0%EA%B5%AC%EC%86%8C',
                      '릴리찐따': 'https://loawa.com/char/%EB%A6%B4%EB%A6%AC%EC%B0%90%EB%94%B0',
                      '풀피': 'https://loawa.com/char/%ED%8D%BD%ED%94%BC',
                      '누쿠누쿠': 'https://loawa.com/char/%EC%9C%97%EC%A7%91%EC%B8%B5%EA%B0%84%EC%86%8C%EC%9D%8C%EB%AF%BC%ED%8F%90%EB%85%80',
                      '차차': 'https://loawa.com/char/%EC%8A%A8%EC%83%81%EC%9D%98%EB%B9%9B',
                      '댕루': 'https://loawa.com/char/%EC%96%B4%ED%9D%A5%ED%8E%80%EC%B9%98%EB%8B%A4%EB%83%A5',
                      '우깡': 'https://loawa.com/char/%EB%A7%9B%EC%9E%88%EB%8A%94%EC%83%88%EC%9A%B4%EB%A7%A4%EC%9A%B0%EA%B9%A1',
                      '체맛건': 'https://loawa.com/char/%EC%B2%B4%EB%A6%AC%EB%A7%9B%EB%82%98%EB%8A%94%EA%B1%B4%EC%8A%AC',
                      '귤남': 'https://loawa.com/char/%EA%B0%90%EA%B7%A4%EB%86%8D%EC%9E%A5%EC%83%81%EB%82%A8%EC%9E%90',
                      '쌀떡': 'https://loawa.com/char/%EA%B7%B8%EB%A3%A8%ED%86%A4%EC%BD%94%EC%9D%B8%EC%83%B5',
                      '따별': 'https://loawa.com/char/MaiR',
                      '차비': 'https://loawa.com/char/%EC%AE%B8%EC%98%A4%EC%98%A5',
                      '고희원': 'https://loawa.com/char/%EA%B3%A0%ED%9D%AC%EC%9B%90',
                      '뭉클': 'https://loawa.com/char/%EC%95%84%EA%B8%B0%EB%8C%95%EC%9F%9D',
                      '마마': 'https://loawa.com/char/%EB%A7%88%EB%A7%88%EB%A0%88%ED%9B%84',
                      '야스치이': 'https://loawa.com/char/2nd%EC%BB%B4%ED%8C%A8%EB%8B%88%EC%96%B8',
                      '워붕쿤': 'https://loawa.com/char/210301%EC%8B%9C%EC%9E%91',
                      '티인': 'https://loawa.com/char/%EB%84%A4%EC%BD%94%EB%A7%88%EC%B8%A0%EB%A6%AC',
                      '대주': 'https://loawa.com/char/%EB%8C%80%EC%A5%AC%EC%9D%B8',
                      '나그없': 'https://loawa.com/char/%EC%9A%B0%ED%95%9C%EC%8B%A4%EC%9C%A0%ED%86%B5',
                      }
        """

        if player == None:
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


def setup(bot):
    bot.add_cog(PlayerContentHandler(bot))