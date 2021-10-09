import discord
from discord.ext import commands, tasks
import colorama
from colorama import Fore as F
import sys
import os
import time, asyncio
import json



os.system("cls")


print('''

\033[1;35;40m      ╔═╗         ╔╗
\033[1;35;40m      ║╔╝         ║║
\033[1;35;40m╔══╦═╦╝╚╦══╦═╦══╦═╝║
\033[1;35;40m║║═╣╔╬╗╔╣╔╗║╔╣╔═╣╔╗║
\033[1;35;40m║║═╣║║║║║╚╝║║║╚═╣╚╝║
\033[1;35;40m╚══╩╝╚╩╝╚══╩╝╚══╩══╝\n''')
token = input("\033[1;35;40mEnter Token: ")


intents = discord.Intents().all()
client = commands.Bot(command_prefix=".", intents=intents)
client.remove_command("help")



@client.event
async def on_connect():
    os.system("cls")
    print('''

\033[1;35;40m      ╔═╗         ╔╗
\033[1;35;40m      ║╔╝         ║║
\033[1;35;40m╔══╦═╦╝╚╦══╦═╦══╦═╝║
\033[1;35;40m║║═╣╔╬╗╔╣╔╗║╔╣╔═╣╔╗║
\033[1;35;40m║║═╣║║║║║╚╝║║║╚═╣╚╝║
\033[1;35;40m╚══╩╝╚╩╝╚══╩╝╚══╩══╝\n''')
    print("\033[1;35;40m[1] Mass DM [2] Mass DM Friends")
    e = input("\033[1;35;40mChoice: ")
    if e == "1":
        message = input("\033[1;35;40mEnter Message: ")
        for channel in client.private_channels:
            try:
                await channel.send(f"{message}")
                print(f"\033[1;35;40mSent message to: {channel}")
            except:
                print(f"\033[1;31;40mFailed to message to: {channel}")   
    elif e == "2":
        message = input("\033[1;35;40mEnter Message: ")
        for user in client.user.friends:
            try:
                await user.send(f"{message}")
                print(f"\033[1;35;40mSent message to: {user}")
            except:
                print(f"\033[1;31;40mFailed to message to: {user}")









def check():
    os.system('cls')
    try:
        client.run(token, bot=False)
    except:
        print('''
 \033[1;31;40mInvalid Token Passed''')
        time.sleep(2)

check()
