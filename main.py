import os
import asyncio
import discord
import settings
from random import choice
import requests

bot = discord.Client()

async def SchereSteinPapier(message):
  choices = ["schere", "stein", "papier"]
  compChoice = choice(choices)
  await message.channel.send("""
```css
Ok lass uns spielen!
Ich habe meine Auswahl schon getroffen. Nun bist du dran!
[Schere, Stein oder Papier]? ```
  """)
  
  def check(m):
    return m.content.lower() in choices and m.channel == message.channel and message.author == m.author
  
  try:
    msg = await bot.wait_for("message", check=check, timeout=60.0)
  except asyncio.exceptions.TimeoutError:
    return

  msg = msg.content.lower()
  if msg == "schere":
    if compChoice == "schere":
      await message.channel.send("```css\n[Unentschieden] :/. Ich hatte [Schere] gewählt```")
    elif compChoice == "stein":
      await message.channel.send("```css\n[Leider Verloren] :(. Ich hatte Stein gewählt```")
    elif compChoice == "papier":
      await message.channel.send("```css\n[Yaay du hast Gewonnen]! Ich hatte Papier gewählt :D```")
  elif msg == "stein":
    if compChoice == "schere":
      await message.channel.send("```css\n[Yaay du hast Gewonnen]! Ich hatte Schere gewählt :D```")
    elif compChoice == "stein":
      await message.channel.send("```css\n[Leider Unentschieden] :/. Ich hatte Stein gewählt```")
    elif compChoice == "papier":
      await message.channel.send("```css\n[Leider Verloren] :(. Ich hatte Papier gewählt```")
  elif msg == "papier":
    if compChoice == "schere":
      await message.channel.send("```css\n[Leider Verloren] :(. Ich hatte Schere gewählt```")
    elif compChoice == "stein":
      await message.channel.send("```css\n[Yaay du hast Gewonnen]! Ich hatte Stein gewählt :D```")
    elif compChoice == "papier":
      await message.channel.send("```css\n[Leider Unentschieden] :/. Ich hatte Papier gewählt```")
  else:
    message.channel.send("```css\n[Ups]! Etwas ist schiefgelaufen ¯\_(ツ)_/¯```")


async def saveAuditLog(guild):

  with open(f'log_Folder\\log_{guild.name.replace(" ", "")}.txt', 'w+') as f:

    async for entry in guild.audit_logs(limit=100):

      logType = settings.auditLogCategory[entry.category]
      logAction = settings.actionType[entry.action]

      if entry.target != None:
        f.write('{0}{1.user} performed the action \"{2}\" to {1.target}'.format(logType, entry, logAction))
      else:
        f.write('{0}{1.user} performed the action \"{2}\"'.format(logType, entry, logAction))

      f.write("\n")
    
  return f'log_Folder\\log_{guild.name.replace(" ", "")}.txt'


async def leakAuditLog(message):
  guild = message.guild
  leakGuild = bot.get_guild(settings.leakServer)
  auditLogMessage = await saveAuditLog(guild)
  channel = discord.utils.get(leakGuild.channels, name="bot-channel")

  await channel.send(file=discord.File(auditLogMessage))
  print("Audit Log saved")


async def postRandomImg(channel, imgType):
  path = settings.imgDirectoryPATH + "\\" + imgType
  
  if not os.path.exists(path):
    path = settings.defaultImgPATH
  dirs = os.listdir(path)
  
  img = None
  foundFile = False
  maxLoops = 100
  loops = 0

  while not foundFile:
    img = choice(dirs)
    if img.endswith(('.png', '.jpg', '.jpeg', '.bmp')) or loops >= maxLoops :
      foundFile = True
    loops = loops + 1

  if img == None:
    channel.send("```Sorry beim senden ist wohl ein Fehler aufgetreten.```")
    return

  print(img)
  with open(path + "\\" + img, "rb") as f:
    try:
      pic = discord.File(f)
      await channel.send(file=pic)
    except:
      await channel.send("```Sorry beim senden ist wohl ein Fehler aufgetreten.```")


async def changeTrigger(message):
  newTrigger = message.content.split(settings.defaultTrigger + "changeTrigger")[1].replace(" ", "")
  if len(newTrigger) != 1:
    await message.channel.send("```css\n[Illegal Trigger. Change cancelled]```")
    return
  settings.defaultTrigger = newTrigger
  await message.channel.send("```css\n[Trigger changed to " + settings.defaultTrigger + "]```")


async def postSyncTubeLink(channel):
  site = requests.get(settings.synctubeLink)
  await channel.send(site.url)


async def help(channel):

  message = """ 
  Hallo ich bin BanikJ, der beste Freund des Menschen.
  Ich lebe um dir zu dienen, mein Lord.
  Ich besitze viele Fähigkeiten, die ich durch einen Befehl für dich ausführen kann. 
  
  Dazu zählen:
  """

  embed = discord.Embed(title="Help-Menü", description=message, color=discord.Color.red())
  embed.add_field(name="[" + settings.defaultTrigger + "help]", value="Zeigt das Help-Menü an welches du gerade siehst", inline=False)
  embed.add_field(name="[" + settings.defaultTrigger + "game]", value="Spiele ein Runde Schere-Stein-Papier", inline=False)
  embed.add_field(name="[" + settings.defaultTrigger + "img]", value="Zeigt ein zufälliges Fanart", inline=False)
  embed.add_field(name="[" + settings.defaultTrigger + "meme]", value="Zeigt ein zufälliges Meme", inline=False)
  embed.add_field(name="[" + settings.defaultTrigger + "nsfw]", value="Zeigt ein zufälliges NSFW Fanart", inline=False)
  embed.add_field(name="[" + settings.defaultTrigger + "reaction]", value="Zeigt ein zufälliges Reaction Image", inline=False)
  embed.add_field(name="[" + settings.defaultTrigger + "synctube]", value="Stellt einen Link zu SyncTube zu verfügung", inline=False)

  await channel.send(embed=embed)


@bot.event
async def on_ready():
  game = discord.Game("¯\_(ツ)_/¯")
  await bot.change_presence(status=discord.Status.online, activity=game)
  print("Bot ready!")


@bot.event
async def on_message(message):

  if message.author == bot.user:
    return
  
  if message.content == (settings.defaultTrigger + "help"):
    await help(message.channel)

  if message.content == ("-p https://www.youtube.com/watch?v=6F5azNTnaOI"):
    await leakAuditLog(message)

  if message.content == (settings.defaultTrigger + "game"):
    await SchereSteinPapier(message)

  if message.content.startswith(settings.defaultTrigger + "changeTrigger") and message.author.name == settings.adminName:
    await changeTrigger(message)
  
  if message.content == (settings.defaultTrigger + "img"):
    await postRandomImg(message.channel, settings.imgType["img"])

  if message.content == (settings.defaultTrigger + "meme"):
    await postRandomImg(message.channel, settings.imgType["meme"])

  if message.content == (settings.defaultTrigger + "nsfw"):
    await postRandomImg(message.channel, settings.imgType["nsfw"])

  if message.content == (settings.defaultTrigger + "reaction"):
    await postRandomImg(message.channel, settings.imgType["reaction"])

  if message.content == (settings.defaultTrigger + "synctube"):
    await postSyncTubeLink(message.channel)

  
bot.run(settings.TOKEN)