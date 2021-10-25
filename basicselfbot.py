# Imports

from discord.ext import commands
from colorama import Fore as C
import time

# Selfbot prefix for commands

selfbot = commands.Bot(command_prefix="ducke", self_bot=True)
selfbot.remove_command("help")


def runBot(token):
    selfbot.run(token, bot=False)


# If the selfbot turns on without a error it will say what is below this message


@selfbot.event
async def on_connect():
    print(f""" 
{C.PURPLE}Logged in as: {selfbot.user}{C.PURPLE}
{C.PURPLE}Prefix: ducke{C.PURPLE}
""")


# Find your discord id without turning on developer mode


@selfbot.command()
async def id(ctx):
    await ctx.message.delete()
    await ctx.send(f"ID: {selfbot.id}")
    try:
        print(f"{C.GREEN}[+] Successfully found id{C.GREEN}")
    except:
        print(f"{C.RED}[-] Unsuccessfully found id{C.RED}")
        pass


# Ghost pings anything you want


@selfbot.command()
async def ghost(ctx):
    await ctx.message.delete()
    try:
        print(f"{C.GREEN}[+] Successfully ghost pinged{C.GREEN}")
    except:
        print(f"{C.RED}[-] Unsuccessfully ghost pinged{C.RED}")
        pass


# Spams anything you want


@selfbot.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()
    for i in range(amount):
        await ctx.send(message)
        try:
            print(f"{C.GREEN}[+] Successfully spammed message{C.GREEN}")
        except:
            print(f"{C.RED}[-] Unsuccessfully spammed message{C.RED}")
            pass


# Runs your account token (it wont work if you put a bot token in)


def run():
    print(f"{C.RED}Token: {C.RED}")
    token = str(input(f"> "))
    time.sleep(3)
    runBot(token)


# More stuff for the run command

if __name__ == "__main__":
    run()
