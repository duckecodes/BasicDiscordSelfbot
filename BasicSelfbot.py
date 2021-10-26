# Imports

from discord.ext import commands
import time

# Selfbot prefix for commands

selfbot = commands.Bot(command_prefix="ducke", self_bot=True)
selfbot.remove_command("help")

# Runs the account token


def runBot(token):
    selfbot.run(token, bot=False)


# If the selfbot turns on without a error it will say what is below this message


@selfbot.event
async def on_connect():
    print(f""" 
Logged in as: {selfbot.user}
Prefix: ducke
""")


# Find your discord id without turning on developer mode


@selfbot.command()
async def id(ctx):
    await ctx.message.delete()
    await ctx.send(f"ID: {selfbot.user.id}")
    try:
        print("[+] Successfully found id")
    except:
        print("[-] Unsuccessfully found id")
        pass


# Ghost pings anything you want


@selfbot.command()
async def ghost(ctx):
    await ctx.message.delete()
    try:
        print("[+] Successfully ghost pinged")
    except:
        print("[-] Unsuccessfully ghost pinged")
        pass


# Spams anything you want


@selfbot.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()
    for i in range(amount):
        await ctx.send(message)
        try:
            print("[+] Successfully spammed message")
        except:
            print("[-] Unsuccessfully spammed message")
            pass


# Runs your account token (it wont work if you put a bot token in)


def run():
    print("Token: ")
    token = str(input(f"> "))
    time.sleep(3)
    runBot(token)


# More stuff for the run command

if __name__ == "__main__":
    run()
