import os
import discord
import markov.py

client = discord.Client()


@client.event
async def on_ready():
    print(f'Successfully connected! Logged in as {client.user}.')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$gimme_markov'):
        await message.channel.send(chains)


client.run(os.environ['DISCORD_TOKEN'])