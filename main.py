import pandas as pd
from discord.ext import commands

client = commands.Bot(command_prefix='!')
path = "data/token.txt"
token_df = pd.read_csv(path)
token = 0
bot_execute_flag = True

extensionUnit = ['cogs.CalenderHandler', 'cogs.CommonContentHandler',
                 'cogs.BotEventHandler', 'cogs.PlayerContentHandler',
                 'cogs.CollectionPointsHandler', 'cogs.BossRaidContentHandler',
                 'cogs.CommandInfoHandler', 'cogs.BotUpdateLogHandler',
                 'cogs.GuideContentHandler', 'cogs.MarketHandler', 'cogs.EmojiHandler']

if __name__ == '__main__':
    for unit in extensionUnit:
        client.load_extension(unit)
        print(unit + "load successful")

    if not bot_execute_flag:
        token = token_df.loc[token_df['Bot'] == 'LOA_BOT_BETA', 'Token'][0]
    else:
        token = token_df.loc[token_df['Bot'] == 'LOA_BOT', 'Token'][1]

client.run(token)
