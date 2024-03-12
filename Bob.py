import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members=True

bot = commands.Bot(command_prefix='[', intents=intents)

@bot.event
async def on_ready():
    print("Bot is online")

@bot.event
async def on_member_join(member):
    print(f'{member} join!')
    channel = bot.get_channel(1216933471084351578)
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    print(f'{member} leave!')
    channel = bot.get_channel(1216933648612200488)
    await channel.send(f'{member} leave!')

bot.run('MTIxNjU5Nzk1NDUxMzg2NjgzMw.GR6T7i.zDo3Rqjshkj2EkpK7abvrUVUCnzSu4HbZNQXH4')