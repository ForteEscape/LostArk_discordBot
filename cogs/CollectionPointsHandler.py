import discord
from discord.ext import commands


class CollectionPointHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 내실(self, ctx, target=None):
        if target == None:
            embed = discord.Embed(title="!내실 명령어 설명",
                                  description="!내실 명령어에 대하여 설명합니다.")
            embed.add_field(name="!내실 [섬마, 거심, 미술품, ...]",
                            value="각 내실의 공략을 호출합니다.\n"
                                  "ex) !내실 섬마 or !내실 거심")
            await ctx.send(embed=embed)
        else:
            if target == "섬의 마음" or target == "섬마":
                await ctx.send("섬의 마음 내실에 관련된 정보입니다.\n"
                               "https://www.inven.co.kr/board/lostark/4821/67330")
            elif target == "거인의 심장" or target == "거심":
                await ctx.send("거인의 심장 내실에 관련된 정보입니다.\n"
                               "https://inty.kr/entry/lostark-hearts")
            elif target == "오르페우스의 별" or target == "오르페우스":
                await ctx.send("오르페우스의 별 내실에 관련된 정보입니다.\n"
                               "https://inty.kr/entry/lostark-orpheus\n"
                               "니아 호감도의 경우에 대한 호감도 스킵 꼼수 링크입니다.\n"
                               "https://www.inven.co.kr/board/lostark/4821/75029")
            elif target == "미술품":
                await ctx.send("위대한 미술품 내실에 관련된 정보입니다.\n"
                               "https://gamecat.tistory.com/36")
            elif target == "모험물":
                await ctx.send("항해 모험물 내실에 관련된 정보입니다.\n"
                               "https://www.inven.co.kr/board/lostark/4821/69444")
            elif target == "세계수의 잎":
                await ctx.send("세계수의 잎은 전 대륙의 벌목, 식물채집, 채광, 낚시, 고고학, 수렵을 통해 얻을 수 있습니다\n"
                               "각 생활 종목 당 10개의 세계수의 잎이 배정되어 있으며 1개는 가이드 퀘스트를 통하여 얻을 수 있습니다.")

    @commands.command()
    async def 모험의서(self, ctx, location=None):
        location_dic = {'아르테미스': 'https://gam3.tistory.com/5',
                        '유디아': 'https://gam3.tistory.com/8?category=929580',
                        '루테란서부': 'https://gam3.tistory.com/10?category=929580',
                        '루테란동부': 'https://gam3.tistory.com/11?category=929580',
                        '토토이크': 'https://gam3.tistory.com/12?category=929580',
                        '애니츠': 'https://gam3.tistory.com/13?category=929580',
                        '아르데타인': 'https://gam3.tistory.com/14?category=929580',
                        '베른북부': 'https://gam3.tistory.com/15?category=929580',
                        '로헨델': 'https://m-lostark.game.onstove.com/Library/Tip/Views/137557?page=1&libraryStatusType=0&librarySearchCategory=0&searchtype=0&searchtext=&ordertype=latest&LibraryQaAnswerType=None&UserPageType=0',
                        '욘': 'https://m.inven.co.kr/webzine/wznews.php?idx=222436&site=lostark',
                        '페이튼': 'https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=hopeteam2&logNo=221863771957',
                        '파푸니카': 'https://www.inven.co.kr/webzine/news/?news=243074&site=lostark',
                        '베른남부': 'https://www.inven.co.kr/webzine/news/?news=249587&site=lostark'
                        }

        if location == None:
            embed = discord.Embed(title="!모험의서 명령어 설명",
                                  description="!모험의서 명령어에 대하여 설명합니다.")
            embed.add_field(name="!모험의서 [루테란동부, 루테란서부, 유디아, ...]",
                            value="각 모험의 서의 정보를 호출합니다.\n"
                                  "ex) !모험의서 아르테미스")
            await ctx.send(embed=embed)
        else:
            if location in location_dic:
                await ctx.send(location + ' 모험의 서와 관련된 정보입니다\n' + location_dic[location])
            else:
                await ctx.send(location + ' 지역은 없는 지역입니다 띄어쓰기를 하였을 경우 붙여쓰기를 해주세요')


def setup(bot):
    bot.add_cog(CollectionPointHandler(bot))