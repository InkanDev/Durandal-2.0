# Durandal 2.0 is a Discord Bot developed by Ange Pagel and compatible with Python 3.6.7.

import discord
from discord.ext import commands
from log import Log
from random import randint

print("  ____                            _       _   ____    ___  ")
print(" |  _ \ _   _ _ __ __ _ _ __   __| | __ _| | |___ \  / _ \ ")
print(" | | | | | | | '__/ _` | '_ \ / _` |/ _` | |   __) || | | |")
print(" | |_| | |_| | | | (_| | | | | (_| | (_| | |  / __/ | |_| |")
print(" |____/ \__,_|_|  \__,_|_| |_|\__,_|\__,_|_| |_____(_)___/ ")

print("\nInitialisation...\n")

token = open("token.txt", "r").read()  # Bot's Token
prefix = "!"  # Prefix used to call a Durandal command

Durandal = commands.Bot(command_prefix=prefix)


@Durandal.event
async def on_ready():
    print("Durandal 2.0 is online.\n")

    print("  Name : {}".format(Durandal.user.name))
    print("  ID   : {}".format(Durandal.user.id))

    print("\n........................................................\n")

    print("Connected Servers :")
    for server in Durandal.servers:
        print("\n  Name : {}".format(server.name))
        print("  ID   : {}".format(server.id))

    print("\n........................................................\n")

    print("Event Log :\n")
    Log.event("Durandal started.")


@Durandal.event
async def on_server_join(server):
    Log.event("Durandal joined server: {}".format(server.name))


@Durandal.event
async def on_server_remove(server):
    Log.event("Durandal left server: {}".format(server.name))


@Durandal.command(pass_context=True)
async def ping(ctx):
    await Durandal.say("!pong")
    Log.event("Command !ping invoked by: " + ctx.message.author.nick + "(" + str(ctx.message.author) + ")"
              + " from server: " + ctx.message.author.server.name
              + ", channel: " + ctx.message.channel.name)


@Durandal.command(pass_context=True)
async def echo(ctx, *args):
    out = ""

    if args[0] == "-c":
        channel_id = args[1]

        for word in args:
            if word not in [args[0], args[1]]:
                out += word + " "
        await Durandal.send_message(Durandal.get_channel(channel_id), out)

    else:
        for word in args:
                out += word + " "
        await Durandal.say(out)

    Log.event("Command !echo invoked by: " + ctx.message.author.nick + "(" + str(ctx.message.author) + ")"
              + " from server: " + ctx.message.author.server.name
              + ", channel: " + ctx.message.channel.name)

@Durandal.command(pass_context=True)
async def random(ctx, *args):
    try:
        min = int(args[0])
        max = int(args[1])
        await Durandal.say(str(randint(min, max)))
    except ValueError:
        await Durandal.say("Error in given values")

Durandal.run(token)
