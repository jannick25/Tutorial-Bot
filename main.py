# Discord Dependencies
import discord
# Token
import os
# Quotes; ermöglicht HTTPS-Anfrage zum Erhalt von Daten der API; API gibt json zurück
import requests
import json
import random

# Client: Dienste des Servers in Anspruch nehmen, Verbindung aufbauen
client = discord.Client()

# Liste mit traurigen Wörtern, auf die der Bot reagieren soll
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

# Anfängliche Aufmunterungen, sollen später von Nutzern erweitert werden können
starter_encouragements = [
  "Cheer up!", 
  "Hand in there.",
  "You are a great person, eventho I can't sincerely tell anything about you at this point"
]

# Zitat der API wiedergeben
def get_quote():
# requests Modul nutzen, um Anfrage zu starten
  response = requests.get("https://zenquotes.io/api/random")
  # Antwort in json-Datei formatieren
  json_data = json.loads(response.text)
  # Zugriff nur auf den Text, nicht auf Eigenschaften oder ähnliches, q ist in dieser speziellen API die Variable mit dem Quote
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

# Event registrieren
@client.event
# Callbacks: when something happens, discord.py ist asynchrone Bibliothek. 
#on_ready event: aufgerufen, wenn der Bot bereit zur Nutzung ist 
async def on_ready():
  # 0.user: username that's logged in as, 0 wird mit client ersetzt
  print('We have logged in as {0.user}'.format(client))

@client.event
# Event: Auf Nachrichten reagieren. Es soll aber nicht reagiert werden, wenn die Nachrichten vom Bot selbst stammen
# message: Variable wird hier scheinbar deklariert
async def on_message(message):
  if message.author == client.user:
    return

# Event: Auf Nachricht mit Kommando reagieren, das $-Zeichen signalisiert Erhalt von Befehlen
  if message.content.startswith('$hello'):
# Wiedergabe einer Nachricht des Bots in einen Discord Channel
    await message.channel.send('Hello!')

  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  # Wenn eins der traurigen Wörter verwendet wird. word: deklarierte Variable
  if any(wort in msg for wort in sad_words):


# Bot wird zum Laufen gebracht. In die Klammern wird das Token des Bots kopiert. Aber replit Code ist öffentlich, daher zu Sicherheitszwecken wird eine Umgebungsvariable verwendet
client.run(os.getenv('TOKEN'))
