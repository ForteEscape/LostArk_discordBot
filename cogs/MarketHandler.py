import os

import discord
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from prettytable import PrettyTable


class MarketHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 시세요약(self, ctx):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920, 1080")
        chrome_options.add_argument("--remote-debugging-port=9222")
        await ctx.send("working")

        #service = Service(executable_path=os.environ.get('CHROMEDRIVER_PATH'))
        driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), chrome_options=chrome_options)

        await ctx.send("working - driver")

        #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        #await ctx.send("working - driver")

        try:
            await ctx.send("working - driver.get...")
            driver.get('https://lostark.game.onstove.com/Market/BookMark')
            driver.implicitly_wait(10)

            driver.find_element(By.XPATH, '//*[@id="user_id"]').send_keys('sehun8631@naver.com')
            driver.implicitly_wait(10)
            sleep(2)
            driver.find_element(By.XPATH, '//*[@id="user_pwd"]').send_keys('kk2924140**')
            driver.implicitly_wait(10)
            sleep(2)
            driver.find_element(By.XPATH, '//*[@id="idLogin"]/div[4]/button/span').click()
            driver.implicitly_wait(10)
            sleep(2)

            driver.implicitly_wait(10)
            """
            driver.find_element(By.XPATH, '//*[@id="lostark-wrapper"]/div/main/div/div[2]/a[2]').click()
            driver.implicitly_wait(10)
            """
            price_data = driver.find_element(By.XPATH, '//*[@id="tbodyItemList"]').text
            driver.implicitly_wait(10)
            sleep(2)

            driver.implicitly_wait(10)
            driver.find_element(By.XPATH, '//*[@id="marketList"]/div[2]/a[3]').click()
            driver.implicitly_wait(10)
            sleep(1)

            price_data2 = driver.find_element(By.XPATH, '//*[@id="tbodyItemList"]').text

            data_price = price_data + '\n' + price_data2
            data_price_list = data_price.split('\n')
            data_list = []

            name_list = [
                ['파결석  ', '파괴석 결정'],
                ['중레하  ', '중급 오레하 융화 재료'],
                ['하레하  ', '하급 오레하 융화 재료'],
                ['명  돌  ', '명예의 돌파석'],
                ['위명돌  ', '위대한 명예의 돌파석'],
                ['상레하  ', '상급 오레하 융화 재료'],
                ['경명돌  ', '경이로운 명예의 돌파석'],
                ['은  총  ', '태양의 은총'],
                ['파강석  ', '파괴강석'],
                ['축  복  ', '태양의 축복'],
                ['명파(소)', '명예의 파편 주머니(소)'],
                ['가  호  ', '태양의 가호'],
                ['명파(중)', '명예의 파편 주머니(중)'],
                ['명파(대)', '명예의 파편 주머니(대)'],
            ]

            for index in data_price_list:
                if index == '시세 확인 구매' or index == '[10개 단위 판매]':
                    pass
                else:
                    for name in name_list:
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

            output = PrettyTable()

            output.field_names = ["이름", "전날가", "최근가", "최저가"]

            for index in data_2d_list:
                output.add_row(index)

            await ctx.send(f"```\n{output}\n```")

        except Exception as error:
            await ctx.send(error)

        """
        driver.get('http://lostark.game.onstove.com/Market')
        page = driver.page_source

        await ctx.send(page + " loading success")

        driver.find_element(By.XPATH, '//*[@id="user_id"]').send_keys('sehun8631@naver.com')
        driver.implicitly_wait(10)
        sleep(2)
        driver.find_element(By.XPATH, '//*[@id="user_pwd"]').send_keys('kk2924140**')
        driver.implicitly_wait(10)
        sleep(2)
        driver.find_element(By.XPATH, '//*[@id="idLogin"]/div[4]/button/span').click()
        driver.implicitly_wait(10)
        sleep(2)

        page = driver.page_source
        await ctx.send(page + " loading success")

        driver.find_element(By.XPATH, '//*[@id="lostark-wrapper"]/div/main/div/div[2]/a[2]').click()
        driver.implicitly_wait(10)
        price_data = driver.find_element(By.XPATH, '//*[@id="tbodyItemList"]').text
        driver.implicitly_wait(10)
        sleep(2)

        driver.find_element(By.XPATH, '//*[@id="marketList"]/div[2]/a[3]').click()
        driver.implicitly_wait(10)
        sleep(1)
        price_data2 = driver.find_element(By.XPATH, '//*[@id="tbodyItemList"]').text

        page = driver.page_source
        await ctx.send(page + " loading success")

        data_price = price_data + '\n' + price_data2
        data_price_list = data_price.split('\n')
        data_list = []

        name_list = [
            ['파결석  ', '파괴석 결정'],
            ['중레하  ', '중급 오레하 융화 재료'],
            ['하레하  ', '하급 오레하 융화 재료'],
            ['명  돌  ', '명예의 돌파석'],
            ['위명돌  ', '위대한 명예의 돌파석'],
            ['상레하  ', '상급 오레하 융화 재료'],
            ['경명돌  ', '경이로운 명예의 돌파석'],
            ['은  총  ', '태양의 은총'],
            ['파강석  ', '파괴강석'],
            ['축  복  ', '태양의 축복'],
            ['명파(소)', '명예의 파편 주머니(소)'],
            ['가  호  ', '태양의 가호'],
            ['명파(중)', '명예의 파편 주머니(중)'],
            ['명파(대)', '명예의 파편 주머니(대)'],
        ]

        for index in data_price_list:
            if index == '시세 확인 구매' or index == '[10개 단위 판매]':
                pass
            else:
                for name in name_list:
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

        output = PrettyTable()

        output.field_names=["이름", "전날가", "최근가", "최저가"]

        for index in data_2d_list:
            output.add_row(index)

        await ctx.send(f"```\n{output}\n```")
"""

def setup(bot):
    bot.add_cog(MarketHandler(bot))