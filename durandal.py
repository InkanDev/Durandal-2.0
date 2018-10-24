# Durandal 2.0 is a Discord Bot developed by Ange Pagel and compatible with Python 3.6.7.

import discord

print("  ____                            _       _   ____    ___  ")
print(" |  _ \ _   _ _ __ __ _ _ __   __| | __ _| | |___ \  / _ \ ")
print(" | | | | | | | '__/ _` | '_ \ / _` |/ _` | |   __) || | | |")
print(" | |_| | |_| | | | (_| | | | | (_| | (_| | |  / __/ | |_| |")
print(" |____/ \__,_|_|  \__,_|_| |_|\__,_|\__,_|_| |_____(_)___/ ")

print("\nInitialisation...\n")

token = "UltraSecretToken"  # Bot's Token
prefix = "!"  # Prefix used to call a Durandal command

Durandal = discord.Client()


@Durandal.event
async def on_ready():
    print("Durandal 2.0 is online.\n")

    print("  Name : {}".format(Durandal.user.name))
    print("  ID   : {}".format(Durandal.user.id))


@Durandal.event
async def on_message(message):

    if message.content.startswith(prefix+"ping"):
        await Durandal.send_message(message.channel, prefix+"pong")


Durandal.run(token)