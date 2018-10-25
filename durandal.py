# Durandal 2.0 is a Discord Bot developed by Ange Pagel and compatible with Python 3.6.7.

import discord
from discord.ext import commands

print("  ____                            _       _   ____    ___  ")
print(" |  _ \ _   _ _ __ __ _ _ __   __| | __ _| | |___ \  / _ \ ")
print(" | | | | | | | '__/ _` | '_ \ / _` |/ _` | |   __) || | | |")
print(" | |_| | |_| | | | (_| | | | | (_| | (_| | |  / __/ | |_| |")
print(" |____/ \__,_|_|  \__,_|_| |_|\__,_|\__,_|_| |_____(_)___/ ")

print("\nInitialisation...\n")

token = "UltraSecretToken"  # Bot's Token
prefix = "!"  # Prefix used to call a Durandal command

Durandal = commands.Bot(command_prefix=prefix)


@Durandal.event
async def on_ready():
    print("Durandal 2.0 is online.\n")

    print("  Name : {}".format(Durandal.user.name))
    print("  ID   : {}".format(Durandal.user.id))


@Durandal.command()
async def ping():
    await Durandal.say("!pong")

@Durandal.command()
async def echo(*args):
    out = ""

    for word in args:
        if word != args[0] or word != args[1]:
            out += word + " "
    await Durandal.say(out)

Durandal.run(token)
