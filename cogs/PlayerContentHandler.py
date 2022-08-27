import glob
import discord
import requests
import csv
import os
from prettytable import PrettyTable
from discord.ext import commands, tasks
from pytz import timezone
import datetime


class PlayerContentHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.party_name_list = []
        self.output_list = []
        self.week_list = []
        self.print_party_member.start()
        self.member_id = self.__get_member_id()

    @tasks.loop(seconds=1)
    async def print_party_member(self):
        if not self.output_list:
            return

        days = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
        chk_time = datetime.datetime.now(timezone('Asia/Seoul')) + datetime.timedelta(seconds=1800)
        day_of_week = days[chk_time.weekday()]

        announce_party = []

        abrel_party_list = [
            "노브1~6", "하브1~6", "노브1~4", "하브1~4",
            "노브1~2", "노브3~4", "노브5~6", "하브1~2",
            "하브3~4", "하브5~6", "하브1~2노브3~4", "하브1~2노브3~6",
            "하브1~4노브5~6"
        ]

        illiakan_party_list = ["아칸노말", "아칸하드", "에피데믹"]

        for element in self.output_list:
            if element[2] == day_of_week:
                announce_party.append(element)

        for data in announce_party:
            party_time = data[3].split()

            for index in range(len(data[4])):
                for element in self.member_id:
                    if data[4][index] in element:
                        data[4][index] = element[1]

            party_data = data[0].split()[1]

            if len(party_time) == 1:
                if chk_time.hour == int(party_time[0]) and chk_time.minute == 0 and chk_time.second == 0:
                    if len(data[4]) == 4:
                        # 카양겔 채널
                        channel = self.bot.get_channel(998535792110620692)
                        await channel.send(data[0] + " 파티에 대한 인원 입니다.")
                        await channel.send(f"```\n{data[1]}\n```")
                        await channel.send(f"<@{data[4][0]}> <@{data[4][1]}> <@{data[4][2]}> <@{data[4][3]}>")
                    elif party_data in abrel_party_list:
                        # 아브렐슈드 채널
                        channel = self.bot.get_channel(998535769977262170)
                        await channel.send(data[0] + " 파티에 대한 인원 입니다.")
                        await channel.send(f"```\n{data[1]}\n```")
                        await channel.send(f"<@{data[4][0]}> <@{data[4][1]}> <@{data[4][2]}> <@{data[4][3]}> "
                                           f"<@{data[4][4]}> <@{data[4][5]}> <@{data[4][6]}> <@{data[4][7]}>")
                    elif party_data in illiakan_party_list:
                        channel = self.bot.get_channel(1006737870268158003)
                        await channel.send(data[0] + " 파티에 대한 인원 입니다.")
                        await channel.send(f"```\n{data[1]}\n```")
                        await channel.send(f"<@{data[4][0]}> <@{data[4][1]}> <@{data[4][2]}> <@{data[4][3]}> "
                                           f"<@{data[4][4]}> <@{data[4][5]}> <@{data[4][6]}> <@{data[4][7]}>")
            else:
                if chk_time.hour == int(party_time[0]) and chk_time.minute == int(party_time[1]) and chk_time.second == 0:
                    if len(data[4]) == 4:
                        # 카양겔 채널
                        channel = self.bot.get_channel(998535792110620692)
                        await channel.send(data[0] + " 파티에 대한 인원 입니다.")
                        await channel.send(f"```\n{data[1]}\n```")
                        await channel.send(f"<@{data[4][0]}> <@{data[4][1]}> <@{data[4][2]}> <@{data[4][3]}>")
                    elif party_data in abrel_party_list:
                        # 아브렐슈드 채널
                        channel = self.bot.get_channel(998535769977262170)
                        await channel.send(data[0] + " 파티에 대한 인원 입니다.")
                        await channel.send(f"```\n{data[1]}\n```")
                        await channel.send(f"<@{data[4][0]}> <@{data[4][1]}> <@{data[4][2]}> <@{data[4][3]}> "
                                           f"<@{data[4][4]}> <@{data[4][5]}> <@{data[4][6]}> <@{data[4][7]}>")
                    elif party_data in illiakan_party_list:
                        channel = self.bot.get_channel(1006737870268158003)
                        await channel.send(data[0] + " 파티에 대한 인원 입니다.")
                        await channel.send(f"```\n{data[1]}\n```")
                        await channel.send(f"<@{data[4][0]}> <@{data[4][1]}> <@{data[4][2]}> <@{data[4][3]}> "
                                           f"<@{data[4][4]}> <@{data[4][5]}> <@{data[4][6]}> <@{data[4][7]}>")

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

    @commands.command()
    async def 파티설정(self, ctx):
        if ctx.message.author.id not in [345903852878430210, 723494509257818132]:
            await ctx.send("Not authorized user")
            return

        [os.remove(f) for f in glob.glob("./data/party_data/*.txt")]

        # old data cleaning
        if self.output_list:
            print("old data washing")
            self.output_list.clear()
            self.week_list.clear()
            self.party_name_list.clear()

        attachment_url = ctx.message.attachments[0].url
        file_request = requests.get(attachment_url)
        file_request.encoding = 'UTF-8'

        with open('./data/party_data/party_data.txt', 'w', newline='') as file:
            file.write(file_request.text)
        file.close()

        self.__read_data()
        self.__make_party_data_output()

        participate_weekly_member_list = []

        for element in self.output_list:
            participate_member = element[4]

            for member in participate_member:
                if (member not in participate_weekly_member_list) and (member not in ["공석", "서폿", "워로드", "홀나", "지인"]):
                    participate_weekly_member_list.append(member)

        if len(participate_weekly_member_list) <= 4:
            await ctx.send("참여자가 너무 작아 수동으로 호출해주셔야 합니다.")
        else:
            member_id = participate_weekly_member_list
            for index in range(len(member_id)):
                for element in self.member_id:
                    if member_id[index] in element:
                        member_id[index] = element[1]

            abrel_party_list = [
                "노브1~6", "하브1~6", "노브1~4", "하브1~4",
                "노브1~2", "노브3~4", "노브5~6", "하브1~2",
                "하브3~4", "하브5~6", "하브1~2노브3~4", "하브1~2노브3~6",
                "하브1~4노브5~6"
            ]

            illiakan_party_list = ["아칸노말", "아칸하드", "에피데믹"]
            for element in self.output_list:
                party = element[0].split()[1]
                if party in abrel_party_list:
                    channel = self.bot.get_channel(998535769977262170)
                    await channel.send(element[0] + " 파티에 대한 인원 입니다.")
                    await channel.send(f"```\n{element[1]}\n```")
                elif party in ["카양겔", "카양겔1", "카양겔2", '카양겔3']:
                    channel = self.bot.get_channel(998535792110620692)
                    await channel.send(element[0] + " 파티에 대한 인원 입니다.")
                    await channel.send(f"```\n{element[1]}\n```")
                elif party in illiakan_party_list:
                    channel = self.bot.get_channel(1006737870268158003)
                    await channel.send(element[0] + " 파티에 대한 인원 입니다.")
                    await channel.send(f"```\n{element[1]}\n```")

            if len(member_id) == 5:
                await ctx.send(f"<@{member_id[0]}> <@{member_id[1]}> <@{member_id[2]}> <@{member_id[3]}> <@{member_id[4]}>")
            elif len(member_id) == 6:
                await ctx.send(
                    f"<@{member_id[0]}> <@{member_id[1]}> <@{member_id[2]}> <@{member_id[3]}> <@{member_id[4]}> "
                    f"<@{member_id[5]}>")
            elif len(member_id) == 7:
                await ctx.send(
                    f"<@{member_id[0]}> <@{member_id[1]}> <@{member_id[2]}> <@{member_id[3]}> <@{member_id[4]}> "
                    f"<@{member_id[5]}> <@{member_id[6]}>")
            elif len(member_id) == 8:
                await ctx.send(
                    f"<@{member_id[0]}> <@{member_id[1]}> <@{member_id[2]}> <@{member_id[3]}> <@{member_id[4]}> "
                    f"<@{member_id[5]}> <@{member_id[6]}> <@{member_id[7]}>")
            elif len(member_id) == 9:
                await ctx.send(
                    f"<@{member_id[0]}> <@{member_id[1]}> <@{member_id[2]}> <@{member_id[3]}> <@{member_id[4]}> "
                    f"<@{member_id[5]}> <@{member_id[6]}> <@{member_id[7]}> <@{member_id[8]}>")
            elif len(member_id) == 10:
                await ctx.send(
                    f"<@{member_id[0]}> <@{member_id[1]}> <@{member_id[2]}> <@{member_id[3]}> <@{member_id[4]}> "
                    f"<@{member_id[5]}> <@{member_id[6]}> <@{member_id[7]}> <@{member_id[8]}> <@{member_id[9]}>")
            elif len(member_id) == 11:
                await ctx.send(
                    f"<@{member_id[0]}> <@{member_id[1]}> <@{member_id[2]}> <@{member_id[3]}> <@{member_id[4]}> "
                    f"<@{member_id[5]}> <@{member_id[6]}> <@{member_id[7]}> <@{member_id[8]}> <@{member_id[9]}> "
                    f"<@{member_id[10]}>")
            elif len(member_id) == 12:
                await ctx.send(
                    f"<@{member_id[0]}> <@{member_id[1]}> <@{member_id[2]}> <@{member_id[3]}> <@{member_id[4]}> "
                    f"<@{member_id[5]}> <@{member_id[6]}> <@{member_id[7]}> <@{member_id[8]}> <@{member_id[9]}> "
                    f"<@{member_id[10]}> <@{member_id[11]}>")
            elif len(member_id) == 13:
                await ctx.send(
                    f"<@{member_id[0]}> <@{member_id[1]}> <@{member_id[2]}> <@{member_id[3]}> <@{member_id[4]}> "
                    f"<@{member_id[5]}> <@{member_id[6]}> <@{member_id[7]}> <@{member_id[8]}> <@{member_id[9]}> "
                    f"<@{member_id[10]}> <@{member_id[11]}> <@{member_id[12]}>")
            elif len(member_id) == 14:
                await ctx.send(
                    f"<@{member_id[0]}> <@{member_id[1]}> <@{member_id[2]}> <@{member_id[3]}> <@{member_id[4]}> "
                    f"<@{member_id[5]}> <@{member_id[6]}> <@{member_id[7]}> <@{member_id[8]}> <@{member_id[9]}> "
                    f"<@{member_id[10]}> <@{member_id[11]}> <@{member_id[12]}> <@{member_id[13]}>")
            elif len(member_id) == 15:
                await ctx.send(
                    f"<@{member_id[0]}> <@{member_id[1]}> <@{member_id[2]}> <@{member_id[3]}> <@{member_id[4]}> "
                    f"<@{member_id[5]}> <@{member_id[6]}> <@{member_id[7]}> <@{member_id[8]}> <@{member_id[9]}> "
                    f"<@{member_id[10]}> <@{member_id[11]}> <@{member_id[12]}> <@{member_id[13]}> <@{member_id[14]}>")

    def __read_data(self):
        with open('./data/party_data/party_data.txt', 'r', encoding='utf-8') as file:
            reader = file.read().splitlines()
        file.close()
        reader.append('')

        self.__write_data(reader)

    def __write_data(self, data):
        datalist = []
        filename_list = []

        for element in data:
            if element == '':
                filename = datalist[0]
                filename_list.append(filename)
                with open('./data/party_data/' + filename + '.txt', 'w', newline='') as file:
                    file.writelines('\n'.join(datalist))
                file.close()

                datalist.clear()
            else:
                datalist.append(element)

        with open('./data/party_data/party_list.txt', 'w', newline='') as file:
            file.writelines('\n'.join(filename_list))
        file.close()

    def __make_party_data_output(self):
        with open('./data/party_data/party_list.txt', 'r', encoding='utf-8') as file:
            reader = file.read().splitlines()
        file.close()

        for filename in reader:
            with open('./data/party_data/' + filename + '.txt', 'r', encoding='utf-8') as file:
                party_data = file.read().splitlines()
            file.close()

            is_party_member_four = False
            party_info_list = filename.split()

            if party_info_list[1] in ['카양겔', '카양겔1', '카양겔2', '카양겔3']:
                is_party_member_four = True

            day_of_week = party_info_list[0]

            time = party_info_list[2]
            time = time.replace('시', ' ')
            time = time.replace('분', '')
            participated_member_list = []

            if is_party_member_four:
                for index in range(1, 5):
                    member_list = party_data[index]
                    participated_member_list.append(member_list)
            else:
                for index in range(1, 5):
                    member_list = party_data[index].split()
                    participated_member_list.append(member_list[0])
                    participated_member_list.append(member_list[1])

            self.week_list.append(day_of_week)
            self.output_list.append(
                [filename, self.__make_table(party_data, is_party_member_four), day_of_week, time, participated_member_list]
            )

    def __make_table(self, data, num_of_party_mem_four):
        table = PrettyTable()

        try:
            if num_of_party_mem_four:
                table.field_names = ["1파티"]
                for index in range(1, 5):
                    member_list = []
                    member_list.append(data[index])
                    table.add_row(member_list)
            else:
                table.field_names = ["1파티", "2파티"]

                for index in range(1, 5):
                    member_list = data[index].split()
                    table.add_row(member_list)
        except Exception as error:
            print(error)
            return

        return table

    def __get_member_id(self):
        with open("./data/party_data/member_id.csv", 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)
        file.close()

        return data


def setup(bot):
    bot.add_cog(PlayerContentHandler(bot))