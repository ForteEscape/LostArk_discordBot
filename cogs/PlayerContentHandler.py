import discord
from discord.ext import commands


class PlayerContentHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 캐릭터정보(self, ctx, player=None):
        player_dic = {'유파민': 'https://loawa.com/char/%EC%9C%A0%ED%8C%8C%EB%AF%BC',
                      '나비릴': 'https://loawa.com/char/%EC%95%84%EB%93%9D%EB%B0%94%EB%93%9D%EC%97%B0%EA%B5%AC%EC%86%8C',
                      '릴리찐따': 'https://loawa.com/char/%EB%A6%B4%EB%A6%AC%EC%B0%90%EB%94%B0',
                      '풀피': 'https://loawa.com/char/%ED%8D%BD%ED%94%BC',
                      '누쿠누쿠': 'https://loawa.com/char/%EC%9C%97%EC%A7%91%EC%B8%B5%EA%B0%84%EC%86%8C%EC%9D%8C%EB%AF%BC%ED%8F%90%EB%85%80',
                      '차차': 'https://loawa.com/char/%EC%8A%A8%EC%83%81%EC%9D%98%EB%B9%9B',
                      '댕루': 'https://loawa.com/char/%EC%96%B4%ED%9D%A5%ED%8E%80%EC%B9%98%EB%8B%A4%EB%83%A5',
                      '우깡': 'https://loawa.com/char/%EB%A7%9B%EC%9E%88%EB%8A%94%EC%83%88%EC%9A%B4%EB%A7%A4%EC%9A%B0%EA%B9%A1',
                      '절정각인서': 'https://loawa.com/char/%EC%A0%88%EC%A0%95%EA%B0%81%EC%9D%B8%EC%84%9C'
                      }
        if player == None:
            embed = discord.Embed(title="!캐릭터정보 명령어 설명",
                                  description="!캐릭터정보 명령어에 대하여 설명합니다.")
            embed.add_field(name="!캐릭터정보 [누쿠누쿠, 차차]",
                            value="각 캐릭터의 정보 링크를 호출합니다.\n"
                                  "ex) !캐릭터정보 나비릴")
            await ctx.send(embed=embed)
        else:
            if player in player_dic:
                await ctx.send(player + ' 의 정보를 호출합니다.\n' + player_dic[player])
            else:
                await ctx.send(player + '은 추가되지 않았거나 이 디스코드에 없는 사람입니다.\n')


def setup(bot):
    bot.add_cog(PlayerContentHandler(bot))