import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()

#url to invite: https://discordapp.com/oauth2/authorize?&client_id=539032775370604545&scope=bot&permissions=8

@client.event
async def on_member_join(member):

    print('I saw that ' + member.name + ' joined one of the servers.')
    await client.send_message(member, 'Hi, thanks for joining whichever server you joined, gamer.')
    print('A welcome note has been sent to ' + member.name + ', Sir Zetaris.')

@client.event
async def on_ready():

    await client.change_presence(game=Game(name='!listvalues | V1.0 by Zetaris ', type = 3))
    print('Collecting daily Dots...') 


@client.event
async def on_message(message):

    if message.content.lower() == 'sinister king':
        await client.send_message(message.channel,'Do not speak of the great Sinister King, peasant.')

    if message.content.lower() == 'sk':
        em = discord.Embed(description='PEASANTS')
        em.set_image(url='https://cdn.discordapp.com/attachments/532906275152068610/539038897204756481/meme.png')
        await client.send_message(message.channel, embed=em)

    if message.content.lower() == 'mobese':
        em = discord.Embed(description='run while you can')
        em.set_image(url='https://cdn.discordapp.com/attachments/532906275152068610/539067942126616577/meme3.png')
        await client.send_message(message.channel, embed=em)
 
    if message.content.lower() == 'ssk':
        em = discord.Embed(description='haha mobese')
        em.set_image(url='https://cdn.discordapp.com/attachments/533682986877714444/539045211901263876/meme2.png')
        await client.send_message(message.channel, embed=em)

    if message.content.lower() == 'seaking':
        em = discord.Embed(description='haha mobese')
        em.set_image(url='https://cdn.discordapp.com/attachments/533682986877714444/539045211901263876/meme2.png')
        await client.send_message(message.channel, embed=em)

    if ('sinister king bad') in message.content.lower():
       await client.delete_message(message)

    if ('sk ugly') in message.content.lower():
       await client.delete_message(message)

    if ('sk bad') in message.content.lower():
       await client.delete_message(message)

    if ('sinister king ugly') in message.content.lower():
       await client.delete_message(message)

    if message.content.startswith('is sinister king'):
        randomlist = ["very cool.","epic","it's lit","no u"]
        await client.send_message(message.channel,(random.choice(randomlist)))

    if message.content.lower().startswith('is sinister king good'):
        randomlist = ["very cool.","epic","it's lit","yes ofc"]
        await client.send_message(message.channel,(random.choice(randomlist)))

    if message.content.lower().startswith('is sk good'):
        randomlist = ["very cool.","epic","it's lit","yes ofc"]
        await client.send_message(message.channel,(random.choice(randomlist)))
        
    if message.content.lower().startswith('is sk'):
        randomlist = ["very cool.","epic","it's lit","no u"]
        await client.send_message(message.channel,(random.choice(randomlist)))

    #if message.content.lower().startswith('who made this'):
        await client.send_message(message.channel,'<@%s> created me, he is my master.'  %('149450218125918208'))
 
    #if message.content.lower().startswith('zet'):
        await client.delete_message(message)

    #idk what more to do here epic style

client.run('NTM5MDMyNzc1MzcwNjA0NTQ1.Dy8hVw.EyRz8w-hkn57CFb9Am3D5c1U1Eg')
