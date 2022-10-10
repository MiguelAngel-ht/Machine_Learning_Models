""" Adolfo Cisneros Mendez 000790559
19 September 2022
The FAQ Bot, Phase 3
Modified from faq_bot_0.py """

import discord
from discord.ext import commands
from load_data import *
import sys

# OBTAIN MESSAGE AND GET RESPONSE AND SEND TO DISCORD
async def send_message(message, user_message):
    user_message.lower()
    try:
        response = get_response(user_message)    # RESPONSE
        await message.channel.send(response)        # SEND RESPONSE TO DISCORD

    except Exception as e:
        print(e)


# TALK TO THE USER
def chat():
    # INICIO
    print("Hello! I know stuff about chat bots.", end="")
    print("\nWhen you're done talking, just say 'goodbye','quit' or 'q' \n")

    # conection to discord
    with open("bot_token.txt") as file:
        TOKEN = file.read()
    intents = discord.Intents.default()
    intents.message_content = True
    client = commands.Bot(command_prefix="--",case_insensitive=True,intents=intents)


    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    
    @client.event
    async def on_message(message):
        # Make sure bot doesn't get stuck in an infinite loop
            if message.author == client.user:
                return            
            
            # GET MESSAGE AND SOME DATA
            username = str(message.author)
            user_message = str(message.content)             # = input("You: ") # from terminal  
            channel = str(message.channel)
            user_message.lower()
            response = get_response(user_message)           # GET RESPONSE 
            await send_message(message, user_message)
            
            # PRINT IN LOCAL TERMINAL
            print("You: ", user_message)
            print("Bot: ", response)       # RETURN ANSWER in terminal


            if response == "See you later!":     # BREAK CONVERSATION AND PROGRAM
                client.close()
                sys.exit()
                
        
    client.run(TOKEN)

chat()