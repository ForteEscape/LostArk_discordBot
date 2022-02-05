import discord
import os
import asyncio
from discord.ext import commands

client = commands.Bot(command_prefix='!')

extensionUnit = ['cogs.CalenderHandler', 'cogs.CommonContentHandler',
                 'cogs.BotEventHandler', 'cogs.PlayerContentHandler',
                 'cogs.CollectionPointsHandler', 'cogs.BossRaidContentHandler',
                 'cogs.CommandInfoHandler', 'cogs.BotUpdateLogHandler', 'cogs.GuideContentHandler']

if __name__ == '__main__':
    for unit in extensionUnit:
        client.load_extension(unit)
        print(unit + "load successful")

client.run(os.environ['TOKEN'])