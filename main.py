import discord
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
async def 내실(ctx, target):
    if target == "섬의 마음" or target == "섬마":
        await ctx.send("섬의 마음 내실에 관련된 정보입니다.\n"
                       "https://www.inven.co.kr/board/lostark/4821/67330")
    elif target == "거인의 심장" or target == "거심":
        await ctx.send("거인의 삼징 내실에 관련된 정보입니다.\n"
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
async def 모험의서(ctx, location):
    if location == "아르테미스":
        await ctx.send("아르테미스 모험의 서와 관련된 정보입니다\n"
                       "https://gam3.tistory.com/5")
    elif location == "유디아":
        await ctx.send("유디아 모험의 서와 관련된 정보입니다\n"
                       "https://gam3.tistory.com/8?category=929580")
    elif location == "루테란서부":
        await ctx.send("루테란 서부 모험의 서와 관련된 정보입니다\n"
                       "https://gam3.tistory.com/10?category=929580")
    elif location == "루테란동부":
        await ctx.send("루테란 동부 모험의 서와 관련된 정보입니다\n"
                       "https://gam3.tistory.com/11?category=929580")
    elif location == "토토이크":
        await ctx.send("토토이크 모험의 서와 관련된 정보입니다\n"
                       "https://gam3.tistory.com/12?category=929580")
    elif location == "애니츠":
        await ctx.send("애니츠 모험의 서와 관련된 정보입니다\n"
                       "https://gam3.tistory.com/13?category=929580")
    elif location == "아르데타인":
        await ctx.send("아르데타인 모험의 서와 관련된 정보입니다\n"
                       "https://gam3.tistory.com/14?category=929580")
    elif location == "베른북부":
        await ctx.send("베른북부 모험의 서와 관련된 정보입니다\n"
                       "https://gam3.tistory.com/15?category=929580")
    elif location == "슈샤이어":
        await ctx.send("슈샤이어 모험의 서와 관련된 정보입니다\n"
                       "https://gam3.tistory.com/16?category=929580")
    elif location == "로헨델":
        await ctx.send("로헨델 모험의 서와 관련된 정보입니다\n"
                       "https://m-lostark.game.onstove.com/Library/Tip/Views/137557?page=1&libraryStatusType=0&librarySearchCategory=0&searchtype=0&searchtext=&ordertype=latest&LibraryQaAnswerType=None&UserPageType=0")
    elif location == "욘":
        await ctx.send("욘 모험의 서와 관련된 정보입니다\n"
                       "https://m.inven.co.kr/webzine/wznews.php?idx=222436&site=lostark")
    elif location == "페이튼":
        await ctx.send("페이튼 모험의 서와 관련된 정보입니다\n"
                       "https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=hopeteam2&logNo=221863771957")
    elif location == "파푸니카":
        await ctx.send("파푸니카 모험의 서와 관련된 정보입니다.\n"
                       "https://www.inven.co.kr/webzine/news/?news=243074&site=lostark")
    elif location == "베른남부":
        await ctx.send("베른 남부 모험의 서와 관련된 정보입니다\n"
                       "https://www.inven.co.kr/webzine/news/?news=249587&site=lostark")
    else:
        await ctx.send(location+" 지역은 존재하지 않는 지역입니다. 띄어쓰기가 들어가 있는 지역은 붙여 써 주세요\n")

@client.command()
async def 군단장(ctx, bossname):
    if bossname == "발탄":
        await ctx.send("마수군단장 발탄에 대한 정보를 호출합니다,\n"
                       "1네임드 공략\n"
                       "https://www.youtube.com/watch?v=YNf2my7id-A&list=PLCGjmOutsfSiR6abIKMsiBTcHn4FfPuCP&index=14\n"
                       "2네임드 공략\n"
                       "https://www.youtube.com/watch?v=LakcTJ7lmgw&list=PLCGjmOutsfSiR6abIKMsiBTcHn4FfPuCP&index=15")
    elif bossname == "비아키스":
        await ctx.send("욕망군단장 비아키스에 대한 정보를 호출합니다.\n"
                       "1네임드 공략\n"
                       "https://www.youtube.com/watch?v=RRxHRHWyp-Q&list=PLCGjmOutsfSiR6abIKMsiBTcHn4FfPuCP&index=17\n"
                       "2네임드 공략\n"
                       "https://www.youtube.com/watch?v=lLgvOOt3DSA&list=PLCGjmOutsfSiR6abIKMsiBTcHn4FfPuCP&index=18\n"
                       "3네임드 공략]\n"
                       "https://www.youtube.com/watch?v=GtVyd7N9M2Q&list=PLCGjmOutsfSiR6abIKMsiBTcHn4FfPuCP&index=19")

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
                          "ex) !모험의서 루테란서부\n"
                          "현재 로헨델부터 베른 남부까지의 정보를 추가중입니다.",
                    inline=False)

    embed.add_field(name="!군단장 [발탄, 비아키스, 쿠크세이튼, 아브렐슈드, 일리아칸, 카멘]",
                    value="각 군단장에 대한 패턴을 알려줍니다.\n"
                          "ex) !군단장 발탄",
                    inline=False)

    embed.add_field(name="!이벤트",
                    value="현재 진행되는 이벤트가 모인 이벤트 페이지 링크를 호출합니다..\n"
                          "ex) !이벤트")

    embed.set_footer(text="건의사항 추가사항 받기 가능 그러나 반영 매우 늦음."
                          "각 정보의 경우 텍스트가 될 수도 있고 링크로도 올려질 수 있습니다.")
    await ctx.send(embed = embed)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("No such command")


client.run('ODYxOTczNjkyMjkyMDA1OTA4.YORljg.r-kGVZGVF-bENS1AGpwdcSURsLc')