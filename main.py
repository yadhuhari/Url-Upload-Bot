import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = '/', self_bot=True, intents=intents, pm_help=True, case_insensitive=True)

DISCORD_TOKEN = "1123616020125454448"

@bot.event
async def on_ready():
    print("Bot Started..!!")
    print("---------------")

@bot.command(pass_context=True)
async def start(ctx):
    await ctx.send("""Hello {ctx.message.author.mention}

I am Url Upload Bot, You can use me very easily..!!
Just send me a direnct link to convert it into a file..!!

Made By BMZ ❤"""
    )
        
bot.run(DISCORD_TOKEN)
