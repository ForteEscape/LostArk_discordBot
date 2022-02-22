from time import sleep
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


class CalenderHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.event_thumbnail_list = []
        self.event_subject_list = []
        self.event_duration_list = []
        self.event_link_list = []
        self.previous_notice_maintenance = None
        self.current_notice_maintenance = None
        self.notice_maintenance_article = None
        self.data_update.start()

    @tasks.loop(seconds=1)
    async def data_update(self):
        chk_time = datetime.datetime.now(timezone('Asia/Seoul'))

        if chk_time.hour == 6 and chk_time.minute == 5 and chk_time.second == 0:
            self.__data_preprocess_for_event()

        if (chk_time.minute == 32 and chk_time.now().second == 0) or (chk_time.minute == 2 and chk_time.second == 0):
            is_change = self.__get_data_from_notice()

            if is_change is None:
                return
            elif is_change is True:
                channel = self.bot.get_channel(945592198165069834)

                embed = discord.Embed(title=self.previous_notice_maintenance)
                embed.add_field(name="내용", value=self.notice_maintenance_article)

                await channel.send(embed=embed)

    @commands.command()
    # 셀레니움을 이용한 크롤링 후 데이터 가공, 사용자에게 제공으로 변경(특정 채널에 출력되도록 수정)
    async def 이벤트(self, ctx):
        channel = self.bot.get_channel(945204576699678730)

        if not self.event_subject_list or not self.event_thumbnail_list or not self.event_duration_list:
            self.__data_preprocess_for_event()

        for index in range(0, len(self.event_subject_list)):
            embed = discord.Embed(title=self.event_subject_list[index],
                                  description=self.event_duration_list[index])
            embed.set_image(url=self.event_thumbnail_list[index])
            embed.set_footer(text=self.event_link_list[index])
            await channel.send(embed=embed)

    # 공지가 올라오면 이를 디스코드 서버에 올릴 수 있도록 변경 가능한가? - 처리함
    @commands.command()
    async def 공지(self, ctx):
        if self.previous_notice_maintenance is None and self.current_notice_maintenance is None:
            self.__get_data_from_notice()

        embed = discord.Embed(title=self.previous_notice_maintenance)
        embed.add_field(name="내용", value=self.notice_maintenance_article)
        await ctx.send(embed=embed)

    @commands.command()
    async def 일정(self, ctx):
        embed = discord.Embed(title="로스트아크 필드보스, 모험 섬 출현 일정",
                              description="로스트아크 내 캘린더 필드보스 및 모험 섬 일정을 간략하게 이미지화합니다.")
        embed.set_image(url="https://cdn.discordapp.com/attachments/685396623483994185/862703916822429746/calander.jpg")
        await ctx.send(embed=embed)

    def __get_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920, 1080")
        chrome_options.add_argument("--remote-debugging-port=9222")

        # live service
        driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)

        # ====================== testing service ==================================
        # service = Service(ChromeDriverManager().install())
        # driver = webdriver.Chrome(service=service, chrome_options=chrome_options)
        # ====================== testing service end ==============================

        return driver

    # 점검 데이터 가져오기
    def __get_data_from_notice(self):
        article_path = '#lostark-wrapper > div > main > div > div.board.board--article > article > section > div'
        title_path = 'a > div.list__subject > span.list__title'
        notice_list_path = '#list > div.list.list--default > ul:nth-child(2) > li'
        notice_path = 'https://lostark.game.onstove.com/News/Notice/List?noticetype=inspection'

        if self.previous_notice_maintenance is None and self.current_notice_maintenance is None:
            driver = self.__get_driver()
            driver.get(notice_path)

            if driver.current_url != notice_path:
                return

            sleep(1)

            notice_data = driver.find_elements(By.CSS_SELECTOR, notice_list_path)

            self.previous_notice_maintenance = notice_data[0].find_element(By.CSS_SELECTOR, title_path).text
            self.current_notice_maintenance = notice_data[0].find_element(By.CSS_SELECTOR, title_path).text

            notice_data[0].click()

            notice_article_data = driver.find_element(By.CSS_SELECTOR, article_path)
            self.notice_maintenance_article = notice_article_data.text

            return True
        else:
            driver = self.__get_driver()
            driver.get(notice_path)

            if driver.current_url != notice_path:
                return None

            notice_data = driver.find_elements(By.CSS_SELECTOR, notice_list_path)
            self.current_notice_maintenance = notice_data[0].find_element(By.CSS_SELECTOR, title_path).text

            # 만약 제목이 같지 않다 -> 공지 리스트에 변경이 생겼다
            if self.current_notice_maintenance != self.previous_notice_maintenance:
                notice_data[0].click()
                notice_article_data = driver.find_element(By.CSS_SELECTOR, article_path)
                self.notice_maintenance_article = notice_article_data.text
                self.previous_notice_maintenance = self.current_notice_maintenance

                return True

    def __get_data_from_event(self, driver):
        elements = driver.find_elements(By.CSS_SELECTOR,
                                        '#lostark-wrapper > div > main > div > div > div.list.list--event > ul > li')

        for index in elements:
            self.event_thumbnail_list.append(
                index.find_element(By.CSS_SELECTOR, 'a > div.list__thumb > img').get_attribute('src'))
            self.event_subject_list.append(index.find_element(By.CSS_SELECTOR, 'a > div.list__subject > span').text)
            self.event_duration_list.append(index.find_element(By.CSS_SELECTOR, 'a > div.list__term').text)
            self.event_link_list.append(index.find_element(By.CSS_SELECTOR, 'a').get_attribute('href'))

    def __data_preprocess_for_event(self):
        self.event_thumbnail_list = []
        self.event_subject_list = []
        self.event_duration_list = []

        driver = self.__get_driver()
        event_path = 'https://lostark.game.onstove.com/News/Event/Now'
        driver.get(event_path)

        if driver.current_url != event_path:
            return

        sleep(1)

        page = driver.find_elements(By.CLASS_NAME, "pagination__number")

        for index in page:
            index.click()
            sleep(1)
            self.__get_data_from_event(driver=driver)


def setup(bot):
    bot.add_cog(CalenderHandler(bot))