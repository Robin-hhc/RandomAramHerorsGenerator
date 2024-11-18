import discord
from aramList import generator

bot = discord.Bot()


@bot.event
async def on_ready():
    print("Bot Online")


@bot.slash_command(name="generate_heroes", description="generate 15 random heroes for each team")
async def generate_heroes(ctx):
    filename = 'heroes.txt'
    await ctx.respond(generator(filename))


token = ""  # Put your own bot token here
bot.run(token)
