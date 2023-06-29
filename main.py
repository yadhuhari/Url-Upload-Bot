import discord
from discord.ext import commands

client = commands.Bot('!')

@client.event
async def on_ready():
    print("Bot Started..!!")
    print("---------------")

@client.command(pass_context=True)
async def start(ctx):
    await ctx.send("""Hello {ctx.message.author.mention}

I am Url Upload Bot, You can use me very easily..!!
Just send me a direnct link to convert it into a file..!!

Made By BMZ ❤""")

client.run('MTEyMzYxNjAyMDEyNTQ1NDQ0OA.GCaMw4.k77Ac0zau7jx-GOxvavdHULILYBSuvHTewXfiY')
