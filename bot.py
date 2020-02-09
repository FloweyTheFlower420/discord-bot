from keep_alive import keep_alive
from getuser import read_user
from getuser import write_user
import discord
import os
import json
import random

client = discord.Client()
fp = open("config.json", "r+")
x = int(json.loads(fp.read())["coin-chance"])
fp.close()

@client.event
async def on_ready():
	print("A flower joined the chat!")
	print(client.user)

@client.event
async def on_message(message):
	if message.author != client.user and message.channel.name == "spam":
		if random.randint(1, x) == 1 and not message.author.bot:
			snowflake = str(message.author.id)
			usernick = message.author.nick

			print("Someone got some coins! (" + usernick + ")") 	# prints a message

			current_coins = read_user(snowflake, "coins") + 1	# use the 'snowflake' to store info
			write_user(snowflake, "coins", current_coins)		# write to json

			await message.channel.send("Someone got some coins! (" + usernick + ") coins: "	+ str(current_coins))

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
