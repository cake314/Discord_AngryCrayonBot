import os
import discord

from dotenv import load_dotenv

#load_dotenv("/c/Users/Cake/Desktop/.env")
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('Hello There'):
        await message.channel.send('General Kenobi!')

client.run(TOKEN)