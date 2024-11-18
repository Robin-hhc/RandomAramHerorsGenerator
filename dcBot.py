import discord
from discord.ext import commands
from aramList import generator

# 这里 proxy 根据你自己的需要进行填写，也可以不用填
bot = commands.Bot(command_prefix='$', description='A bot that greets the user back.')


@bot.event
async def on_ready():
    print("Bot Online")


@bot.slash_command(name="generate_heroes", description="generate 15 random heroes for each team")
async def generate_heroes(ctx):
    filename = 'heroes.txt'
    await ctx.respond(generator(filename))

token = "MTMwODE1NTMzODczNzg0NDMzNw.GO1SkU._Mq_vtRFrMEHJh-JQGPcVi8Rpnb5NLZ4sBpjxA"
bot.run(token)
