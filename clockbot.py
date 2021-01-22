import discord
import asyncio
import os, sys, traceback
from discord.ext import commands

bot = commands.Bot(command_prefix="!", description="Pretty useless bot.")
init_exts = ['cogs.chat', 'cogs.misc', 'cogs.owner']

counter = 0
print("Loading extensions...")
for extension in init_exts:
    try:
        bot.load_extension(extension)
        counter += 1
    except Exception as e:
        print(f"Failed loading {extension}")
        print(f"{type(e).__name__}: {e}")
print(f"Loaded [{counter}/{len(init_exts)}] extensions")

@bot.event
async def on_connect():
    print("Connecting...")

@bot.event
async def on_disconnect():
    print("{bot.user.name} has been disconnected")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="인생낭비"))
    print(f"{bot.user.name} is now online")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return # Unknown command; just ignore it
    raise error

# Testing range

@bot.command()
async def test(ctx, *, arg):
    print(arg)
    await ctx.send("```" + arg + "```")

# Token & Run

f = open("token.txt", 'r')
token = f.readline()
f.close()

print("Launching client...")
bot.run(token)
print("Client terminated")

flags = bot.get_cog('flags')
print(f"Exitcode : {flags.exitcode}")
print("Program end.\n")