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
		

async def coins(message, snowflake, args, usernick):
	await message.channel.send("> `you have: " + str(read_user(snowflake, "coins")) + " coins!`")

async def setroot(message, snowflake, args, usernick):
	if not read_user(snowflake, "isroot"):
		await message.channel.send("> ```fix\n> sorry, " + usernick + ", you do not have sufficient permissions to preform this action\n> ```")
		return
	
	if len(args) != 2:
		await message.channel.send("> ```fix\n> incorrect useage; use st!help setroot\n> ```")
		return
		
	memberlist = message.guild.members 

	for member in memberlist:
		if str(member) == args[1]:
			write_user(str(member.id), "isroot", True)

cmdlist = {
	"coins": coins,
	"setroot": setroot 
}


@client.event					# event handler
async def on_ready():
	print("A flower joined the chat!")	# dump a msg
	print(client.user)			# get username

@client.event
async def on_message(message):
	snowflake = str(message.author.id)
	usernick = message.author.nick
	
	if message.content.startswith("st!"):
		
		print("someone invoked me!")
		cmd = message.content.split(' ')
		cmd[0] = cmd[0][3:]
		
		try:
			await cmdlist[cmd[0]](message, snowflake, cmd, usernick)
		except:
			print("there was an error...")
	elif check_valid_coin(message):
		print("Someone got some coins! (" + usernick + ")") 	# prints a message

		current_coins = read_user(snowflake, "coins") + 1	# use the 'snowflake' to store info
		write_user(snowflake, "coins", current_coins)		# write to json

		await channel.send("> `Someone got some coins! (" + usernick + ") coins: "	+ str(current_coins) + "`")

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
coro = client.run(token)
