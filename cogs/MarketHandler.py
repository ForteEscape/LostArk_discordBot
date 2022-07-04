import discord
import datetime, csv, math, string
from pytz import timezone
from discord.ext import commands, tasks
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from prettytable import PrettyTable


class MarketHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.price_data_list = []
        self.update_time = None
        self.get_price_data.start()
        self.is_alamed = False
        self.item_nickname_list = self.__get_nickname()

    @tasks.loop(seconds=1)
    async def get_price_data(self):
        """
        매 시간 20분과 50분에 거래소 관심목록 데이터를 크롤링한다. 크롤링한 데이터를 가공하여 클래스 필드에 넣는다.
        """
        chk_time = datetime.datetime.now(timezone('Asia/Seoul'))

        if (chk_time.minute == 21 and chk_time.second == 0) or (chk_time.minute == 51 and chk_time.second == 0):
            try:
                data_price_list = self.__get_data_from_csv()

                if data_price_list is None:
                    return

                print("load success")
                load_time = datetime.datetime.now(timezone('Asia/Seoul'))

                '''
                announcement function
                if not self.is_alamed:
                    self.is_alamed = True

                    embed = discord.Embed(title="점검 알림")
                    embed.add_field(name="점검 내용",
                                    value="점검 시간: 11:20 ~ 별도 안내 까지\n"
                                          "점검 동안 봇 서비스가 간헐적으로 중단되거나 전면 중단될 수 있습니다.\n")
                    channel = self.bot.get_channel(id)
                    await channel.send(embed=embed)
                '''

                self.price_data_list = data_price_list
                self.update_time = load_time

            except Exception as error:
                print(error)
                return

    @commands.command()
    async def 경매(self, ctx, *condition):
        data = ' '.join(condition)

        if data == '':
            embed = discord.Embed(title="!경매 명령어 설명",
                                  description="!경매 명령어에 대하여 설명합니다.")
            embed.add_field(name="!경매 [파티 인원] [아이템 이름]",
                            value="경매 가격에 대한 입찰가를 출력합니다\n")
            await ctx.send(embed=embed)
        else:
            party = data.split(' ')[0]
            gold_data = data.split(' ')[1]
            orig_data = gold_data

            is_data_digit = True

            # gold_data가 각인서 또는 강화 확률 추가 아이템 이름으로 나올 경우
            if not gold_data.isdecimal():
                is_data_digit = False
                is_item_in_list = False

                # 만약 nickname list에서 해당 품목을 찾는다면, 해당 이름(nickname)으로 변환
                for item in self.item_nickname_list:
                    if gold_data in item:
                        gold_data = item[0]
                        is_item_in_list = True

                # 이후 검색
                if is_item_in_list:
                    for item in self.price_data_list:
                        if item[0] == gold_data:
                            if '\"' in item[3]:
                                item[3] = item[3].strip('\"')
                            if ',' in item[3]:
                                item[3] = item[3].replace(",", "")

                            price_data = int(item[3])
                            gold_data = price_data
                            break
                else:
                    await ctx.send("요청하신 " + gold_data + " 의 가격을 찾지 못했습니다. 숫자로 입력하시거나 정확한 데이터를 넣어주세요")
                    return
            else:
                # 아니라면, text-format 형식을 int로 변환
                gold_data = int(gold_data)
                
            # 경매가 계산 및 디스코드 출력
            if party == '4' or party == '4인':
                bid_gold, bid_before_gold = self.__calculate_bidgold(4, gold_data)
                embed = discord.Embed(title="경매가 결과")

                if not is_data_digit:
                    embed.add_field(name=orig_data + " 에 대한 4인 입찰 가격",
                                    value="4인 입찰 추천 경매가는 " + str(bid_before_gold) + "골드, 최대 " + str(bid_gold) + "골드 까지입니다.\n")
                else:
                    embed.add_field(name=str(gold_data) + "골드 에 대한 4인 입찰 가격",
                                    value="4인 입찰 추천 경매가는 " + str(bid_before_gold) + "골드, 최대 " + str(
                                        bid_gold) + "골드 까지입니다.\n")
                await ctx.send(embed=embed)
            elif party == '8' or party == '8인':
                bid_gold, bid_before_gold = self.__calculate_bidgold(8, gold_data)
                embed = discord.Embed(title="경매가 결과")

                if not is_data_digit:
                    embed.add_field(name=orig_data + " 에 대한 8인 입찰 가격",
                                    value="8인 입찰 추천 경매가는 " + str(bid_before_gold) + "골드, 최대 " + str(
                                        bid_gold) + "골드 까지입니다.\n")
                else:
                    embed.add_field(name=str(gold_data) + "골드 에 대한 8인 입찰 가격",
                                    value="8인 입찰 추천 경매가는 " + str(bid_before_gold) + "골드, 최대 " + str(
                                        bid_gold) + "골드 까지입니다.\n")
                await ctx.send(embed=embed)

    def __calculate_bidgold(self, party_type, gold_data):
        bid_gold, bid_before_gold = 0, 0

        if party_type == 4:
            bid_gold = gold_data * 0.95 * 0.75
            bid_before_gold = gold_data * 0.95 * 0.68
            bid_gold = math.floor(bid_gold)
            bid_before_gold = math.floor(bid_before_gold)
        elif party_type == 8:
            bid_gold = gold_data * 0.95 * 0.875
            bid_before_gold = gold_data * 0.95 * 0.795
            bid_gold = math.floor(bid_gold)
            bid_before_gold = math.floor(bid_before_gold)

        return bid_gold, bid_before_gold

    @commands.command()
    async def 시세요약(self, ctx):
        """
        클래스 필드의 price_data_list에 값이 없을 시 위에 했던 데이터 크롤링을 실시한다.
        만약 존재할 시 해당 값을 바로 출력함으로서 로그인 - 데이터 크롤링 과정을 모두 생략하여 속도를 높인다.
        """
        if not self.price_data_list:
            data_price_list = self.__get_data_from_csv()

            if data_price_list is None:
                await ctx.send("거래소에 접속할 수 없습니다. 점검중이거나 서버 문제일 수 있습니다.")
                return

            self.price_data_list = data_price_list

        output = self.__make_table(self.price_data_list)
        await ctx.send(f"```\n{output}\n```")
        await ctx.send("데이터 최신화 시각 : " + self.update_time)

    @commands.command()
    async def 시세(self, ctx, *item_name):
        """
        사용자가 price_data_list 내에 존재하는 항목을 검색할 시 캐싱된 데이터에서 바로 값을 가져와
        속도를 절약한다. 만약 존재하지 않는 항목을 검색 할 시 기존과 똑같이 검색하여 값을 가져온다.
        """
        input_data = ' '.join(item_name)

        if input_data == '':
            embed = discord.Embed(title="!시세 명령어 설명",
                                  description="!시세 명령어에 대하여 설명합니다.")
            embed.add_field(name="!시세 [아이템 이름]",
                            value="입력받은 아이템의 가격을 출력합니다\n")
            await ctx.send(embed=embed)
        else:
            is_item_in_list = False
            data_price_list = []
            output = None

            # 만약 시세 가격표(캐싱 된 가격표)가 만들어졌다면
            if self.price_data_list:
                # 닉네임으로 먼져 치환(이미 치환된 데이터기 때문)
                for item in self.item_nickname_list:
                    if input_data in item:
                        input_data = item[0]
                        is_item_in_list = True

                # 이후 검색
                if is_item_in_list:
                    for item in self.price_data_list:
                        if item[0] == input_data:
                            data_price_list.append(item)

                    output = self.__make_table(data_price_list)

                else:
                    # 존재하지 않을 시 일련의 과정을 거쳐 다시 데이터 크롤링
                    data_price_list = self.__get_data_from_market(input_data)

                    if data_price_list is None:
                        await ctx.send("거래소에 접속할 수 없습니다. 점검중이거나 서버 문제일 수 있습니다.")
                        return

                    data_2d_list = self.__data_processing(data_price_list)
                    output = self.__make_table(data_2d_list)
            else:
                data_price_list = self.__get_data_from_market(input_data)

                if data_price_list is None:
                    await ctx.send("거래소에 접속할 수 없습니다. 점검중이거나 서버 문제일 수 있습니다.")
                    return

                data_2d_list = self.__data_processing(data_price_list)
                output = self.__make_table(data_2d_list)

            await ctx.send(f"```\n{output}\n```")

    # 데이터 테이블 만드는 내부 메서드
    def __make_table(self, data_list):
        output = PrettyTable()

        output.field_names = ["이름", "전날가", "최근가", "최저가"]

        for index in data_list:
            output.add_row(index)

        return output

    def __get_data_from_csv(self):
        path = r"/home/sehun5515/DataCrawler/data/output/Total_data.csv"

        with open(path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            data_price_list = list(reader)

        return data_price_list

    # 시세 검색에서 데이터 크롤링 시 사용하는 내부 메서드
    def __get_data_from_market(self, item_name):
        driver = self.__get_driver()
        driver.get('https://lostark.game.onstove.com/Market')

        is_success = self.__log_in_process(driver)

        if not is_success:
            driver.quit()
            return None

        sleep(2)

        name_input = driver.find_element(By.XPATH,
                                         '/html/body/div[2]/div/main/div/div[3]/div[2]/form/fieldset/div/div[1]/input')
        name_input.send_keys(item_name)
        sleep(2)
        search_btn = driver.find_element(By.XPATH,
                                         '/html/body/div[2]/div/main/div/div[3]/div[2]/form/fieldset/div/div[4]/button[1]')
        search_btn.click()

        sleep(2)
        driver.implicitly_wait(10)
        price_data = driver.find_element(By.XPATH,
                                         '/html/body/div[2]/div/main/div/div[3]/div[2]/div/div/div[1]/table/tbody').text
        sleep(2)
        data_price_list = price_data.split('\n')

        driver.quit()

        return data_price_list

    # 데이터 가공
    def __data_processing(self, data_price_list):
        data_list = []
        for index in data_price_list:
            if index == '시세 확인 구매' or index == '[10개 단위 판매]' or index == '[구매 시 거래 불가]':
                pass
            else:
                for name in self.item_nickname_list:
                    if index in name:
                        index = name[0]

                data_list.append(index)

        temp_list = []
        data_2d_list = []

        for index in data_list:
            temp_list.append(index)

            if len(temp_list) == 4:
                data_2d_list.append(temp_list)
                temp_list = []

        return data_2d_list

    # 데이터 크롤링 준비 메서드
    def __log_in_process(self, driver):
        try:
            driver.find_element(By.XPATH, '//*[@id="user_id"]').send_keys('sehun8631@naver.com')
            sleep(2)
            driver.find_element(By.XPATH, '//*[@id="user_pwd"]').send_keys('kk2924140**')
            sleep(2)
            driver.find_element(By.XPATH, '//*[@id="idLogin"]/div[4]/button/span').click()

            return True

        except Exception as error:
            print("log in failed cause this error")
            print(error)
            return False

    # 데이터 크롤링 준비 메서드2
    def __get_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920, 1080")

        # live service
        driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)

        # ====================== testing service ==================================
        # service = Service(ChromeDriverManager().install())
        # driver = webdriver.Chrome(service=service, chrome_options=chrome_options)
        # ====================== testing service end ==============================

        return driver

    def __get_nickname(self):
        path = "./data/nickname.csv"

        with open(path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            nickname_data = list(reader)

        file.close()

        return nickname_data


def setup(bot):
    bot.add_cog(MarketHandler(bot))