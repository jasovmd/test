import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.all()

bot = commands.Bot(command_prefix='[', intents=intents)

@bot.event
async def on_ready():
    print("Bot is online")

@bot.event
async def on_member_join(member):
    print(f'{member} join!')

@bot.event
async def on_member_remove(member):
    print(f'{member} leave!')

bot.run('MTIxNjU5Nzk1NDUxMzg2NjgzMw.G0Sub9.VVCQAFF3f81E44_coYCDh0DwhLKIP-QiWclT_A')