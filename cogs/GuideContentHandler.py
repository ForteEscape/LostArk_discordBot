import discord, csv
from discord.ext import commands


class GuideContentHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 각인(self, ctx, *engrave_name):
        engrave_description_path = r'./data/engrave_description.csv'
        engrave_nickname_path = r'./data/engrave_nickname.csv'

        input_data = ' '.join(engrave_name)
        engrave_name = self.__get_data_from_csv(engrave_description_path)
        engrave_nickname_list = self.__get_data_from_csv(engrave_nickname_path)

        for engrave_nickname in engrave_nickname_list:
            if input_data in engrave_nickname:
                input_data = engrave_nickname[0]

        if not input_data:
            embed = discord.Embed(title="!각인 명령어 설명",
                                  description="!각인 명령어에 대하여 설명합니다.")
            embed.add_field(name="!캐릭터정보 [정밀 단도]",
                            value="각 각인의 설명을 호출합니다.\n")
            await ctx.send(embed=embed)
        else:
            description = ''
            for element in engrave_name:
                if input_data == element[0]:
                    description = element[1]

            if description != '':
                embed = discord.Embed(title=input_data + " 각인 설명",
                                      description=description)
                await ctx.send(embed=embed)
            else:
                await ctx.send(input_data + " 각인은 존재하지 않는 각인이거나 추가되지 않은 각인입니다.")

    def __get_data_from_csv(self, path):
        with open(path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            description_data = list(reader)
        file.close()

        return description_data

def setup(bot):
    bot.add_cog(GuideContentHandler(bot))
