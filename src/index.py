import discord
from discord.ext import commands

import datetime

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Cualquier texto", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Servidor creado el: ", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Region del servidor: ", value=f"{ctx.guild.region}")
    await ctx.send(embed= embed)

@bot.command()
async def cancion_jason(ctx):
    embed = discord.Embed(title="Cancion favorita de Jason", description="Una de las canciones favoritas de Jason es ", color=discord.Color.blue())
    embed.add_field(name='Url YoutTube', value="https://www.youtube.com/watch?v=PIh2xe4jnpk")
    await ctx.send(embed=embed)

#Events
@bot.event
async def on_ready():
    print('Bot encendido y listo')

bot.run('')
