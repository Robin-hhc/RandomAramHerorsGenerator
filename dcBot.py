import discord
from discord.ext import commands
from aramList import generator

bot = commands.Bot(command_prefix='$', description='A bot that greets the user back.')


@bot.event
async def on_ready():
    print("Bot Online")


@bot.slash_command(name="generate_heroes", description="generate 15 random heroes for each team")
async def generate_heroes(ctx):
    filename = 'heroes.txt'
    await ctx.respond(generator(filename))


token = ""  # Put your own bot token here
bot.run(token)
