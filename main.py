import discord, random, os, asyncio, requests, datetime
from discord.ext import commands, tasks
from Challenges import r1, r2, r3
import sqlite3

# Crear la base de datos si no existe y conectar a ella
conn = sqlite3.connect('croco.db')
cursor = conn.cursor()

# Crear la tabla de estadísticas si no existe
cursor.execute('''CREATE TABLE IF NOT EXISTS stats (
    user_id INTEGER PRIMARY KEY,
    points INTEGER DEFAULT 0,
    completed_challenges INTEGER DEFAULT 0
)''')

conn.commit()
conn.close()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

challenge_stage = 0

@bot.event
async def on_ready():
    print('Croco está listo para ayudar!')
    channel = bot.get_channel(1278007920877113504)
    await channel.send('Hola, soy Croco! Tu consejero para un mundo mejor! Usa el comando "!funciones" para ver qué puedo hacer.')

@bot.command()
async def funciones(ctx):
    await ctx.send('''Estos son mis comandos actuales y sus funciones:
"!info": Un poco de información sobre lo que vamos a hacer.
"!reto": Pongamos a prueba tus capacidades para salvar el mundo de la contaminación.
"!estadisticas": Te muestra tus estadísticas actuales.
                   ''')

@bot.command()
async def info(ctx):
    await ctx.send('''Hola, soy Croco!
Un bot consejero destinado a cambiar el curso actual del mundo, cada día háblame y te esperarán 3 retos diarios para un planeta mejor! Conforme pase el tiempo y sigas colaborando, podrás ganar puntos y competir contra otros usuarios de todo el mundo!''')

@bot.command()
async def reto(ctx):
    global challenge_stage
    user_id = ctx.author.id
    
    conn = sqlite3.connect('croco.db')
    cursor = conn.cursor()

    # Verificar si el usuario ya existe en la base de datos
    cursor.execute('SELECT * FROM stats WHERE user_id=?', (user_id,))
    user = cursor.fetchone()

    if user is None:
        # Si no existe, crear un nuevo registro
        cursor.execute('INSERT INTO stats (user_id, points, completed_challenges) VALUES (?, ?, ?)', 
                       (user_id, 10, 1))
    else:
        # Si existe, actualizar los puntos y los retos completados
        cursor.execute('UPDATE stats SET points=points+10, completed_challenges=completed_challenges+1 WHERE user_id=?', 
                       (user_id,))

    conn.commit()
    conn.close()

    # Enviar el reto correspondiente
    if challenge_stage == 0:
        await ctx.send(r1())
        challenge_stage += 1
    elif challenge_stage == 1:
        await ctx.send(r2())
        challenge_stage += 1
    elif challenge_stage == 2:
        await ctx.send(r3())
        challenge_stage = 0


@bot.command()
async def estadisticas(ctx):
    user_id = ctx.author.id
    
    conn = sqlite3.connect('croco.db')
    cursor = conn.cursor()

    # Obtener las estadísticas del usuario
    cursor.execute('SELECT points, completed_challenges FROM stats WHERE user_id=?', (user_id,))
    user = cursor.fetchone()

    conn.close()

    if user:
        points, completed_challenges = user
        await ctx.send(f'🌟 **Estadísticas de @{ctx.author.name}:**\n'
                       f'Puntos: {points}\n'
                       f'Retos completados: {completed_challenges}')
    else:
        await ctx.send('No tienes estadísticas todavía. ¡Completa un reto para empezar! Buena suerte.')


bot.run("")
