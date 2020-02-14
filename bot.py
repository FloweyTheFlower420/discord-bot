from keep_alive import keep_alive
from getuser import read_user
from getuser import write_user
from init_conf import setup
import discord
import os
import json
import random

setup()						# setup core files

client = discord.Client()			# init discord client

fp = open("config.json", "r+")			# read configuration file
x = int(json.loads(fp.read())["coin-chance"])	# get coin chance
fp.close()					# close the file

def check_valid_coin(msg):
	return msg.author != client.user and msg.channel.name == "spam" and random.randint(1, x) == 1 and not msg.author.bot
			

@client.event					# event handler
async def on_ready():
	print("A flower joined the chat!")	# dump a msg
	print(client.user)			# get username

@client.event
async def on_message(message):
	if message.content.startswith("st!"):
		print("someone invoked me!")
	elif check_valid_coin(message):
		snowflake = str(message.author.id)
		usernick = message.author.nick

		print("Someone got some coins! (" + usernick + ")") 	# prints a message

		current_coins = read_user(snowflake, "coins") + 1	# use the 'snowflake' to store info
		write_user(snowflake, "coins", current_coins)		# write to json

		await message.channel.send("Someone got some coins! (" + usernick + ") coins: "	+ str(current_coins))

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
