import discord
import os
import asyncio
from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print("log in success in as {0.user}".format(client))


@client.command()
async def hello(ctx):
    await ctx.send("hello world")


@client.command()
async def 이벤트(ctx):
    await ctx.send("현재 진행되는 이벤트 페이지를 호출합니다.\n"
                   "https://lostark.game.onstove.com/News/Event/Now")


@client.command()
async def 일정(ctx):
    embed = discord.Embed(title="로스트아크 필드보스, 모험 섬 출현 일정",
                          description="로스트아크 내 캘린더 필드보스 및 모험 섬 일정을 간략하게 이미지화합니다.")
    embed.set_image(url="https://cdn.discordapp.com/attachments/685396623483994185/862703916822429746/calander.jpg")
    await ctx.send(embed = embed)


@client.command()
async def 내실(ctx, target = None):
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


@client.command()
async def 모험의서(ctx, location = None):
    location_dic = {'아르테미스':'https://gam3.tistory.com/5',
                    '유디아':'https://gam3.tistory.com/8?category=929580',
                    '루테란서부':'https://gam3.tistory.com/10?category=929580',
                    '루테란동부':'https://gam3.tistory.com/11?category=929580',
                    '토토이크':'https://gam3.tistory.com/12?category=929580',
                    '애니츠':'https://gam3.tistory.com/13?category=929580',
                    '아르데타인':'https://gam3.tistory.com/14?category=929580',
                    '베른북부':'https://gam3.tistory.com/15?category=929580',
                    '로헨델':'https://m-lostark.game.onstove.com/Library/Tip/Views/137557?page=1&libraryStatusType=0&librarySearchCategory=0&searchtype=0&searchtext=&ordertype=latest&LibraryQaAnswerType=None&UserPageType=0',
                    '욘':'https://m.inven.co.kr/webzine/wznews.php?idx=222436&site=lostark',
                    '페이튼':'https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=hopeteam2&logNo=221863771957',
                    '파푸니카':'https://www.inven.co.kr/webzine/news/?news=243074&site=lostark',
                    '베른남부':'https://www.inven.co.kr/webzine/news/?news=249587&site=lostark'
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


@client.command()
async def 군단장(ctx, bossname = None, status = None):
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


@client.command()
async def info(ctx):
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

    await ctx.send(embed = embed)


@client.command()
async def 캐릭터정보(ctx, player = None):
    player_dic = {'유파민':'https://loawa.com/char/%EC%9C%A0%ED%8C%8C%EB%AF%BC',
                  '나비릴':'https://loawa.com/char/%EC%95%84%EB%93%9D%EB%B0%94%EB%93%9D%EC%97%B0%EA%B5%AC%EC%86%8C',
                  '릴리찐따':'https://loawa.com/char/%EB%A6%B4%EB%A6%AC%EC%B0%90%EB%94%B0',
                  '풀피':'https://loawa.com/char/%ED%8D%BD%ED%94%BC',
                  '누쿠누쿠':'https://loawa.com/char/%EC%9C%97%EC%A7%91%EC%B8%B5%EA%B0%84%EC%86%8C%EC%9D%8C%EB%AF%BC%ED%8F%90%EB%85%80',
                  '차차':'https://loawa.com/char/%EC%8A%A8%EC%83%81%EC%9D%98%EB%B9%9B',
                  '댕루':'https://loawa.com/char/%EC%96%B4%ED%9D%A5%ED%8E%80%EC%B9%98%EB%8B%A4%EB%83%A5',
                  '우깡':'https://loawa.com/char/%EB%A7%9B%EC%9E%88%EB%8A%94%EC%83%88%EC%9A%B4%EB%A7%A4%EC%9A%B0%EA%B9%A1',
                  '절정각인서':'https://loawa.com/char/%EC%A0%88%EC%A0%95%EA%B0%81%EC%9D%B8%EC%84%9C'
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


@client.command()
async def 어비스던전(ctx, map = None):
    if map == None:
        embed = discord.Embed(title="!어비스던전 명령어 설명",
                              description="!어비스던전 명령어에 대하여 설명합니다.")
        embed.add_field(name="!어비스던전 [낙원의문, 낙원, 오레하의우물, 오레하]",
                        value="각 어비스 던전의 공략을 호출합니다.\n"
                              "ex) !어비스던전 오레하의우물 or !어비스던전 오레하")
        await ctx.send(embed = embed)
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


@client.command()
async def 어비스레이드(ctx, named = None):
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


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("No such command")

client.run(os.environ['TOKEN'])