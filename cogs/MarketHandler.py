import discord
import datetime
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
        self.item_nickname_list = [
            ['파결석', '파괴석 결정'],
            ['중레하', '중급 오레하 융화 재료'],
            ['하레하', '하급 오레하 융화 재료'],
            ['명돌', '명예의 돌파석'],
            ['위명돌', '위대한 명예의 돌파석'],
            ['상레하', '상급 오레하 융화 재료'],
            ['경명돌', '경이로운 명예의 돌파석'],
            ['은총', '태양의 은총'],
            ['파강석', '파괴강석'],
            ['축복', '태양의 축복'],
            ['명파(소)', '명예의 파편 주머니(소)'],
            ['가호', '태양의 가호'],
            ['명파(중)', '명예의 파편 주머니(중)'],
            ['명파(대)', '명예의 파편 주머니(대)'],
        ]

    @tasks.loop(seconds=1)
    async def get_price_data(self):
        """
        매 시간 20분과 50분에 거래소 관심목록 데이터를 크롤링한다. 크롤링한 데이터를 가공하여 클래스 필드에 넣는다.
        """
        chk_time = datetime.datetime.now(timezone('Asia/Seoul'))

        if (chk_time.minute == 20 and chk_time.second == 0) or (chk_time.minute == 50 and chk_time.second == 0):
            try:
                data_price_list = self.__get_data_from_bookmark()

                if data_price_list is None:
                    return

                print(self.update_time)

                self.price_data_list = self.__data_processing(data_price_list)
            except Exception as error:
                print(error)
                return

    @commands.command()
    async def 시세요약(self, ctx):
        """
        클래스 필드의 price_data_list에 값이 없을 시 위에 했던 데이터 크롤링을 실시한다.
        만약 존재할 시 해당 값을 바로 출력함으로서 로그인 - 데이터 크롤링 과정을 모두 생략하여 속도를 높인다.
        """

        if not self.price_data_list:
            data_price_list = self.__get_data_from_bookmark()

            if data_price_list is None:
                await ctx.send("거래소에 접속할 수 없습니다. 점검중이거나 서버 문제일 수 있습니다.")
                return

            self.price_data_list = self.__data_processing(data_price_list)

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

    @commands.command()
    async def 경매(self, ctx, character_class=None, parts=None, status1=None, status2=None, engrave1=None,
                 engrave_val1=None, engrave2=None, engrave2_val=None, price=None):

        if character_class is None:
            embed = discord.Embed(title="!경매 명령어 설명",
                                  description="!경매 명령어에 대하여 설명합니다.")
            embed.add_field(name="!경매 [직업 악세부위 전투특성 전투특성2 각인 각인수치 각인2 각인2수치 품질 가격]",
                            value="입력받은 조건에 부합한 악세를 찾습니다. 이때 전투특성이나 각인을 임의로 하고 싶을 경우 무조건 없음"
                                  "으로 입력해 주세요\n"
                                  "\nex) !경매 워로드 귀걸이 특화 없음 전투태세 5 원한 3 80 27000\n"
                                  "\nex) !경매 도화가 목걸이 신속 특화 만개 6 없음 없음 80 30000")
            await ctx.send(embed=embed)
        else:
            try:
                auction_path = 'https://lostark.game.onstove.com/Auction'

                driver = self.__get_driver()
                driver.get(auction_path)

                is_success = self.__log_in_process(driver)

                if not is_success:
                    driver.quit()
                    return None

                sleep(2)

                driver.find_element(By.XPATH, '//*[@id="lostark-wrapper"]/div/main/div/div[3]/div[2]/form/fieldset/div/div[5]/button[2]').click()
                sleep(2)

                driver.find_element(By.CSS_SELECTOR, '#selClassDetail > div.lui-select__title').click()
                sleep(1)
                elements = driver.find_elements(By.CSS_SELECTOR, '#selClassDetail > div.lui-select__option > label')
                sleep(2)

                for index in elements:
                    if index.text == character_class:
                        index.click()

                if parts == '목걸이':
                    driver.find_element(By.XPATH, '//*[@id="selCategoryDetail"]/div[1]').click()
                    driver.find_element(By.XPATH, '//*[@id="selCategoryDetail"]/div[2]/label[11]').click()
                elif parts == '귀걸이':
                    driver.find_element(By.XPATH, '//*[@id="selCategoryDetail"]/div[1]').click()
                    driver.find_element(By.XPATH, '//*[@id="selCategoryDetail"]/div[2]/label[12]').click()
                elif parts == '반지':
                    driver.find_element(By.XPATH, '//*[@id="selCategoryDetail"]/div[1]').click()
                    driver.find_element(By.XPATH, '//*[@id="selCategoryDetail"]/div[2]/label[13]').click()

                driver.find_element(By.XPATH,
                                    '//*[@id="modal-deal-option"]/div/div/div[1]/div[1]/table/tbody/tr[4]/td[2]/div/div[1]').click()
                sleep(1)

                driver.find_element(By.XPATH,
                                    '//*[@id="modal-deal-option"]/div/div/div[1]/div[1]/table/tbody/tr[4]/td[2]/div/div[2]/label[7]').click()

                driver.find_element(By.CSS_SELECTOR, '#selEtc_0 > div.lui-select__title').click()
                driver.find_element(By.CSS_SELECTOR,
                                    '#selEtc_0 > div.lui-select__option > label:nth-child(2)').click()
                sleep(1)

                driver.find_element(By.CSS_SELECTOR, '#selEtcSub_0 > div.lui-select__title').click()
                elements = driver.find_elements(By.CSS_SELECTOR, '#selEtcSub_0 > div.lui-select__option > label')

                for index in elements:
                    if index.text == status1:
                        index.click()
                sleep(1)

                if status2 != "없음":
                    driver.find_element(By.CSS_SELECTOR, '#selEtc_1 > div.lui-select__title').click()
                    driver.find_element(By.CSS_SELECTOR,
                                        '#selEtc_1 > div.lui-select__option > label:nth-child(2)').click()
                    sleep(1)

                    driver.find_element(By.CSS_SELECTOR, '#selEtcSub_1 > div.lui-select__title').click()
                    elements = driver.find_elements(By.CSS_SELECTOR,
                                                    '#selEtcSub_1 > div.lui-select__option > label')

                    for index in elements:
                        if index.text == status2:
                            index.click()
                    sleep(1)

                driver.find_element(By.CSS_SELECTOR, '#selEtc_2 > div.lui-select__title').click()
                driver.find_element(By.CSS_SELECTOR, '#selEtc_2 > div.lui-select__option > label:nth-child(3)').click()

                sleep(1)
                driver.find_element(By.CSS_SELECTOR, '#selEtcSub_2 > div.lui-select__title').click()
                elements = driver.find_elements(By.CSS_SELECTOR, '#selEtcSub_2 > div.lui-select__option > label')

                sleep(1)
                for index in elements:
                    if index.text == engrave1:
                        index.click()

                driver.find_element(By.CSS_SELECTOR, '#txtEtcMin_2').send_keys(engrave_val1)
                sleep(2)

                if engrave2 != "없음":
                    driver.find_element(By.CSS_SELECTOR, '#selEtc_3 > div.lui-select__title').click()
                    driver.find_element(By.CSS_SELECTOR,
                                        '#selEtc_3 > div.lui-select__option > label:nth-child(3)').click()

                    sleep(1)
                    driver.find_element(By.CSS_SELECTOR, '#selEtcSub_3 > div.lui-select__title').click()
                    elements = driver.find_elements(By.CSS_SELECTOR,
                                                    '#selEtcSub_3 > div.lui-select__option > label')

                    sleep(1)
                    for index in elements:
                        if index.text == engrave2:
                            index.click()

                    sleep(1)
                    driver.find_element(By.CSS_SELECTOR, '#txtEtcMin_3').send_keys(engrave2_val)

                sleep(5)
                driver.find_element(By.CSS_SELECTOR,
                                    '#modal-deal-option > div > div > div.lui-modal__button > button.lui-modal__search').click()
                sleep(30)


            except Exception as error:
                return



    # 데이터테이블 만드는 내부 메서드
    def __make_table(self, data_list):
        output = PrettyTable()

        output.field_names = ["이름", "전날가", "최근가", "최저가"]

        for index in data_list:
            output.add_row(index)

        return output

    def __get_data_from_bookmark(self):
        driver = self.__get_driver()
        driver.get('https://lostark.game.onstove.com/Market/BookMark')

        is_success = self.__log_in_process(driver)

        if not is_success:
            driver.quit()
            return None

        sleep(2)

        price_data = driver.find_element(By.XPATH, '//*[@id="tbodyItemList"]').text
        sleep(1)
        driver.find_element(By.XPATH, '//*[@id="marketList"]/div[2]/a[3]').click()

        sleep(2)
        price_data2 = driver.find_element(By.XPATH, '//*[@id="tbodyItemList"]').text

        data_price = price_data + '\n' + price_data2
        data_price_list = data_price.split('\n')

        driver.quit()

        self.update_time = datetime.datetime.now(timezone('Asia/Seoul')).strftime('%Y-%m-%d %H:%M:%S')

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
        #chrome_options.add_argument("--headless")
        #chrome_options.add_argument("--disable-dev-shm-usage")
        #chrome_options.add_argument("--no-sandbox")
        #chrome_options.add_argument("--disable-gpu")
        #chrome_options.add_argument("--window-size=1920, 1080")
        #chrome_options.add_argument("--remote-debugging-port=9222")

        # live service
        # driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)

        # ====================== testing service ==================================
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, chrome_options=chrome_options)
        # ====================== testing service end ==============================

        return driver


def setup(bot):
    bot.add_cog(MarketHandler(bot))