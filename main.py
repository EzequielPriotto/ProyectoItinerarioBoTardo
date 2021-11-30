#---------------Imports-------------------------#

import os
from typing import ContextManager
import discord
from discord import client
from discord import emoji
from discord.ext import commands
from discord.utils import DISCORD_EPOCH
import urllib.request
import json
from dotenv import load_dotenv
import random

#---------------Obtencion del token-------------------------#
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#---------------Asignaciones-------------------------#

bot = commands.Bot(command_prefix = '-b ', description = "Hola!, Soy el BoTardo, en que te puedo ayudar?")
client = discord.Client()

#---------------Seleccion random de respuesta-------------------------#

def respuestaRandom(parametro, numero):

    #Defino los arrays
    opcionesMensaje= [
        "🤖 bien, esperando a que me pidan algo ",
        "🤖 medio mal, mi dueño no me da bola",
        "🤖 con calor, necesito una pasta termica nueva",
        "🤖 con ganas de que me pidan cosas",
        "🤖 un poco aburrido, pero siempre listo para ayudar",
    ]

    opcionesFoto= [
        "https://st.depositphotos.com/3332767/5045/i/950/depositphotos_50457567-stock-photo-young-guy-waiting-for-date.jpg",
        "https://www.mediawavestore.es/12556-large_default/557315-almohada-emoticono-motivo-cara-triste-de-30-cm-o.jpg",
        "https://cdn5.dibujos.net/dibujos/pintados/201314/sol-con-sudor-naturaleza-meteorologia-pintado-por-cookie1d-9809190.jpg",
        "https://thumbs.dreamstime.com/z/%C3%BAltimo-hombre-ansioso-que-sostiene-un-reloj-65380118.jpg",
        "https://blog.diabetesforo.com/wp-content/uploads/2018/12/a1aa8d9c1c093aa66aa6d729a4823e-730x445.jpg"
    ]

    #defino cada dato
    mensaje = opcionesMensaje[numero]
    foto = opcionesFoto[numero]
          
    #retorna cada parametro por separado   
    if parametro == "mensaje": return mensaje
    if parametro == "foto": return foto

 
@bot.listen()
async def on_message(mensaje):
    #Escuchar mensajes y leer si le preguntan como esta
    if "bot como estas?" in mensaje.content.lower():

        #Selecciona un numero random para la respuesta
        numero = random.choice(range(0, 4))

        #obtiene la foto y el mensaje random
        respuestaBotMensaje = respuestaRandom("mensaje", numero)
        respuestaBotFoto = respuestaRandom("foto", numero)
        
        #crea el embebido con los datos
        embebido = discord.Embed(title=respuestaBotMensaje, color=discord.Color.green())
        embebido.set_image(url= respuestaBotFoto)

        #envia el mensaje
        await mensaje.channel.send(embed=embebido)
        await bot.process_commands(mensaje)




#---------------Mosca img-------------------------#
@bot.command(name='mosca')
async def mosca(ctx):
    imagen = 'https://media.discordapp.net/attachments/755165953905393734/828849406400790538/MOSCA.png'
    await ctx.send(imagen)

#---------------Ping pong con comando & embebido-------------------------#

@bot.command()
async def ping(ctx):
    embebido = discord.Embed(title=f"🤖 PONG", color=discord.Color.green())
    embebido.set_image(url="https://i.imgur.com/zRFj4OQ.png")

    await ctx.send(embed=embebido)


#---------------Info del server (mi server)-------------------------#

@bot.command(name='info')
async def info(ctx):
    embebido = discord.Embed(title=f"{ctx.guild.name}", description="El server mas pateado de todo discord", color=discord.Color.green())
    embebido.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embebido.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embebido.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embebido.set_thumbnail(url="https://i.imgur.com/ag28CjQ.png")

    await ctx.send(embed=embebido)








#               .-""""-.
#              /        \
#             /_        _\
#            // \      / \\
#            |\__\    /__/|
#             \    ||    /
#              \        /
#               \  __  /  \  /          ________________________________
#                '.__.'    \/          /                                 \
#                 |  |     /\         |     te acabas de encontrar       |
#                 |  |    O  O        |    con el alien Robertito!       |
#                 ----    //         O \_________________________________/
#                (    )  //        O
#               (\\     //       o
#              (  \\    )      o
#              (   \\   )   /\
#    ___[\______/^^^^^^^\__/) o-)__
#   |\__[=======______//________)__\
#   \|_______________//____________|
#       |||      || //||     |||
#       |||      || @.||     |||
#        ||      \/  .\/      ||
#                   . .
#                  '.'.`

















#---------------Interaccion con mensajes sin comando-------------------------#

@bot.listen()
async def on_message(mensaje):
    #Mostrar tutorial
    if "tutorial" in mensaje.content.lower() and "dormir" in mensaje.content.lower():
        await mensaje.channel.send('🤖 Mirate este Tutorial paa https://www.youtube.com/watch?v=Hg469wSrZhI')
        # emote = ' <:brunoOK:839359524711563264> ' para definir el emote y que sea usable
        emote = ' <:brunoOK:839359524711563264> '
        await mensaje.channel.send('🤖 No te olvides de mirarte un tutorial para despertarte govir ' + emote)
        await bot.process_commands(mensaje)

    #Mostrar gif
    elif "mostrame" in mensaje.content.lower() and  "personas" in mensaje.content.lower() and "colegio" in mensaje.content.lower() and "bot" in mensaje.content.lower():
        await mensaje.channel.send('https://media1.tenor.com/images/3ebd6d0701bb4a1ee08c7b4d9c241546/tenor.gif?itemid=16565703')    

#---------------Estado del bot-------------------------#
@bot.event
async def on_ready():    
    game = discord.Game('🤖 Esperando a ser util')
    await bot.change_presence(status=discord.Status.idle, activity=game)
    # print('Estado actualizado')
    print('\033[1;32m' + 'bot en funcionamiento...' +'\033[0;m')


#---------------Ejecucion del bot-------------------------#
bot.run(TOKEN)