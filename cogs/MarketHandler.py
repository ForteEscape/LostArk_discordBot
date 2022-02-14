import os

import discord
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
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
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920, 1080")
        chrome_options.add_argument("--remote-debugging-port=9222")

        driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)

        driver.get('https://lostark.game.onstove.com/Market/BookMark')

        driver.find_element(By.XPATH, '//*[@id="user_id"]').send_keys('id')
        sleep(2)
        driver.find_element(By.XPATH, '//*[@id="user_pwd"]').send_keys('pwd')
        sleep(2)
        driver.find_element(By.XPATH, '//*[@id="idLogin"]/div[4]/button/span').click()
        sleep(2)

        price_data = driver.find_element(By.XPATH, '//*[@id="tbodyItemList"]').text
        sleep(1)

        driver.find_element(By.XPATH, '//*[@id="marketList"]/div[2]/a[3]').click()
        sleep(1)
        price_data2 = driver.find_element(By.XPATH, '//*[@id="tbodyItemList"]').text

        data_price = price_data + '\n' + price_data2
        data_price_list = data_price.split('\n')
        data_list = []

        driver.quit()

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

        print(data_2d_list)

        await ctx.send(f"```\n{output}\n```")

    @commands.command()
    async def 시세(self, ctx, *item_name):
        input_data = ' '.join(item_name)

        if item_name is None:
            embed = discord.Embed(title="!시세 명령어 설명",
                                  description="!시세 명령어에 대하여 설명합니다.")
            embed.add_field(name="!시세 [아이템 이름]",
                            value="입력받은 아이템의 가격을 출력합니다\n")
            await ctx.send(embed=embed)
        else:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--window-size=1920, 1080")
            chrome_options.add_argument("--remote-debugging-port=9222")

            driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)

            driver.get('https://lostark.game.onstove.com/Market')

            driver.find_element(By.XPATH, '//*[@id="user_id"]').send_keys('id')
            sleep(2)
            driver.find_element(By.XPATH, '//*[@id="user_pwd"]').send_keys('pwd')
            sleep(2)
            driver.find_element(By.XPATH, '//*[@id="idLogin"]/div[4]/button/span').click()
            sleep(2)

            name_input = driver.find_element(By.XPATH, '/html/body/div[2]/div/main/div/div[3]/div[2]/form/fieldset/div/div[1]/input')
            name_input.send_keys(input_data)
            sleep(2)
            search_btn = driver.find_element(By.XPATH, '/html/body/div[2]/div/main/div/div[3]/div[2]/form/fieldset/div/div[4]/button[1]')
            search_btn.click()

            sleep(2)
            driver.implicitly_wait(10)
            price_data = driver.find_element(By.XPATH, '/html/body/div[2]/div/main/div/div[3]/div[2]/div/div/div[1]/table/tbody').text
            sleep(2)
            data_price_list = price_data.split('\n')
            data_list = []

            driver.quit()

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
                if index == '시세 확인 구매' or index == '[10개 단위 판매]' or index == '[구매 시 거래 불가]':
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

            print(data_2d_list)

            await ctx.send(f"```\n{output}\n```")



def setup(bot):
    bot.add_cog(MarketHandler(bot))