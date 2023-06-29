import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix = '/', self_bot=True, intents=intents)

DISCORD_TOKEN=MTEyMzYxNjAyMDEyNTQ1NDQ0OA.GfR9TJ.9J7Bepjr6RtNgRAgFA-syHm7YV5TLeddso7Q2g

@client.event
async def on_ready():
    print("Bot Started..!!")
    print("---------------")

@client.command(pass_context=True)
async def start(ctx):
    await ctx.send("""Hello {ctx.message.author.mention}

I am Url Upload Bot, You can use me very easily..!!
Just send me a direnct link to convert it into a file..!!

Made By BMZ ❤"""
    )
                   
client.run(DISCORD_TOKEN)
