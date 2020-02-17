from keep_alive import keep_alive
from getuser import read_user
from getuser import write_user
from init_conf import setup
import discord
import os
import json
import random

RED = 0xcc2204

async def argerror(cmdname, channel):
	embed = discord.Embed(color = RED)
	embed.add_field(name = "Incorrect Command Useage", value = "incorrect useage; use ` st!help " + cmdname +" `", inline = False)
	await channel.send(embed = embed)
async def permerror(usernick, channel):
	embed = discord.Embed(color = RED)
	embed.add_field(name = "Permission Denied", value = "sorry, " + usernick + ", you do not have sufficient permissions to preform this action", inline = False)
	await channel.send(embed = embed)
	

setup()						# setup core files

client = discord.Client()			# init discord client

fp = open("config.json", "r+")			# read configuration file
x = int(json.loads(fp.read())["coin-chance"])	# get coin chance
fp.close()					# close the file

def check_valid_coin(msg):
	return msg.author != client.user and msg.channel.name == "spam" and random.randint(1, x) == 1 and not msg.author.bot

#async def help((message, snowflake, args, usernick):
#	if len(args) == 1:
#		await message.channel.send(		

async def coins(message, snowflake, args, usernick):
	await message.channel.send("> `you have: " + str(read_user(snowflake, "coins")) + " coins!`")

async def setroot(message, snowflake, args, usernick):
	if not read_user(snowflake, "isroot"):
		await permerror(usernick, message.channel)
		return
	
	if len(args) != 2:
		await argerror("setroot", message.channel)
		return
		
	memberlist = message.guild.members 

	for member in memberlist:
		if str(member) == args[1]:
			await message.channel.send("> ```fix\n> successfully set user '" + member.nick + "' to root\n> ```")
			write_user(str(member.id), "isroot", True)
			return

async def rmroot(message, snowflake, args, usernick):
	if not read_user(snowflake, "isroot"):
		await permerror(usernick, message.channel)
		return

	if len(args) != 2:
                await argerror("rmroot", message.channel)
                return
	
	memberlist = message.guild.members

	for member in memberlist:
		if str(member) == args[1]:
			write_user(str(member.id), "isroot", False)
			await message.channel.send("> ```fix\n> successfully set user '" + member.nick + "' to root\n> ```")
			return
async def chcoins(message, snowflake, args, usernick):
	if not read_user(snowflake, "isroot"):
                await permerror(usernick, message.channel)
                return
	
	if len(args) != 4:
		await argerror("chcoins", message.channel)
		return

	memberlist = message.guild.members
	
	for member in memberlist:
		if str(member) == args[2]:
			currsnow = str(member.id)
			nick = member.nick
			
	
	if args[1] == "set":
		try:
			count = int(args[3])
		except:
			await argerror("chcoins", message.channel)
			return
		
		write_user(currsnow, "coins", count)
		await message.channel.send("> ```fix\n> set coins of user '" + nick + "' to " + str(count) + "\n> ```")
	else:
		await argerror("chcoins", message.channel)
		return
cmdlist = {
	"coins": coins,
	"setroot": setroot,
	"chcoins": chcoins,
	"rmroot": rmroot
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
			embed = discord.Embed(color = RED)
			embed.add_field(name = "Unknown Command", value = "unknown command; use ` st!help ` for help", inline = False)
			await message.channel.send(embed = embed)
	
	elif check_valid_coin(message):
		print("Someone got some coins! (" + usernick + ")") 	# prints a message

		current_coins = read_user(snowflake, "coins") + 1	# use the 'snowflake' to store info
		write_user(snowflake, "coins", current_coins)		# write to json

		await channel.send("> `Someone got some coins! (" + usernick + ") coins: "	+ str(current_coins) + "`")

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
coro = client.run(token)
