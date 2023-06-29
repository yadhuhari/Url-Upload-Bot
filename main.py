import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = '/', self_bot=True, intents=intents)

@bot.event
async def on_ready():
    print("Bot Started..!!")
    print("---------------")

@bot.slash_command()
async def start(ctx):
    await ctx.send("""Hello {ctx.message.author.mention}

I am Url Upload Bot, You can use me very easily..!!
Just send me a direnct link to convert it into a file..!!

Made By BMZ ❤"""
    )
        
bot.run("MTEyMzYxNjAyMDEyNTQ1NDQ0OA.GoKk5l.jPzMq4ZwoY_7HT7iXfxCW9gJVQd3MJ7sTeTYr4")
