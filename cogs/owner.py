import discord
import asyncio
import os, sys
from discord.ext import commands

# Owner only commands
class owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.flags = bot.get_cog('flags')

    # @commands.event - not required
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.NotOwner):
            await ctx.send("에러: WieeRd 전용 커맨드")

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, *extensions):
        for ext in extensions:
            try:
                self.bot.load_extension(ext)
                await ctx.send(f"{ext} has been loaded")
            except Exception as e:
                await ctx.send(f"Failed loading {ext}")
                await ctx.send(f"{type(e).__name__}: {e}")
                
    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, *extensions):
        for ext in extensions:
            try:
                self.bot.unload_extension(ext)
                await ctx.send(f"{ext} has been unloaded")
            except Exception as e:
                await ctx.send(f"Failed unloading {ext}")
                await ctx.send(f"{type(e).__name__}: {e}")

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, *extensions):
        for ext in extensions:
            try:
                self.bot.reload_extension(ext)
                await ctx.send(f"{ext} has been reloaded")
            except Exception as e:
                await ctx.send(f"Failed reloading {ext}")
                await ctx.send(f"{type(e).__name__}: {e}")

    @commands.command()
    @commands.is_owner()
    async def quit(self, ctx):
        print("Quit command has been called")
        self.flags.exitcode = 'quit'
        await ctx.send("장비를 정지합니다")
        await self.bot.logout()

    @commands.command()
    @commands.is_owner()
    async def restart(self, ctx):
        print("Restart command has been called")
        self.flags.exitcode = 'restart'
        await ctx.send("I'll be back")
        await self.bot.logout()


def setup(bot):
    bot.add_cog(owner(bot))
    print(f"{__name__} has been loaded ")

def teardown(bot):
    print(f"{__name__} has been unloaded")
