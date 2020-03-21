from getuser import read_user, write_user		# user info stuff
from init_conf import setup						# setup config files
from embed import *								# pretty embeds
import discord
import os
import json
import random

setup()											# setup core files

client = discord.Client()						# init discord client

fp = open("config.json", "r+")
x = int(json.loads(fp.read())["coin-chance"])	# get coin chance
fp.close()

def search_for_user(guild, username):
	memberlist = guild.members;
	for member in memberlist:
		if str(member) == username:
			return member
	return None;

def check_valid_mochi(msg):						# coin 
	return msg.author != client.user and random.randint(1, x) == 1 and not msg.author.bot

async def helper(message, snowflake, args, usernick):
	if len(args) == 1:
		if read_user(str(message.author.id), "isroot") == True:
			await message.channel.send(embed = roothelpembed)
		else:
			await message.channel.send(embed = helpembed)	
	elif len(args) == 2:
		try:
			await message.channel.send(embed = cmdhelp[args[1]])
		except:
			print("why oh why")

async def flour(message, snowflake, args, usernick):
	embed = Discord.embed(title = "You have: " + str(read_user(snowflake, "mochi")) + "mochi flour!")
	await message.channel.send(embed = embed)

async def setlord(message, snowflake, args, usernick):
	if not read_user(snowflake, "isroot"):
		await permerror(usernick, message.channel)
		return
	
	if len(args) != 2:
		await argerror("setlord", message.channel)
		return
		
	memberlist = message.guild.members 

	member = search_for_user(message.guild, args[1])
	if member is None:
		usererror(args[1], message.channel)
		return

	write_user(str(member.id), "isroot", True)
	embed = discord.Embed(color = GRN)
	embed.add_field(name = "Success!", value = "Set user '" + member.nick + "' to mochi-lord")
	await message.channel.send(embed = embed)
	return

async def rmlord(message, snowflake, args, usernick):
	if not read_user(snowflake, "isroot"):
		await permerror(usernick, message.channel)
		return

	if len(args) != 2:
		await argerror("rmroot", message.channel)
		return
	
		member = search_for_user(message[1], asd)
		if member is None:
			usererror(message[1])
			return

		write_user(str(member.id), "isroot", False)
		
		embed = discord.Embed(color = GRN)
		embed.add_field(name = "Success!", value = member.nick + " is no longer mochi-lord")
		await message.channel.send(embed = embed)
		return
 
async def chflour(message, snowflake, args, usernick):
	if not read_user(snowflake, "isroot"):
		await permerror(usernick, message.channel)
		return
	
	if len(args) != 4:
		await argerror("chmflour", message.channel)w
		return

	member = search_for_user(message.guild, args[1])
	if member is None:
		usererror(args[1], message.channel)
		return

	currsnow = str(member.id)
	nick = member.nick
			
	
	if args[2] == "set":
		try:
			count = int(args[3])
		except:
			await argerror("chmflour", message.channel)
			return
		 
		write_user(currsnow, "mochi", count)
		embed = discord.Embed(color = GRN)
		embed.add_field(name = "Success!", value = "Set user's mochi flour to " + str(count))
		await message.channel.send(embed = embed)
	elif args[2] == "add":
		try:
			count = int(args[3])
		except:
			await argerror("chmflour", message.channel)
			return
		newcoins = read_user(currsnow, "mochi") + count
		write_user(currsnow, "mochi", newcoins)
		return
	else:
		await argerror("chmflour", message.channel)
		return

async def donate(message, snowflake, args, usernick):
	try:
		amount = int(args[2])
	except:
		await argerror("donate", messge.channel)
		return
	current_coins = read_user(str(snowflake), "mochi")
	if amount > current_coins:
		return
	new_coins_sender = read_user()	

cmdlist = {
	"flour": flour,
	"setroot": setlord,
	"chmflour": chflour,
	"rmroot": rmlord,
	"help": helper,
	"donate": donate
}

@client.event							# event handler
async def on_ready():
	print("give me all your mochi!")	# dump a msg
	print(client.user)					# get username

@client.event
async def on_message(message):
	snowflake = str(message.author.id)
	usernick = message.author.nick
	
	if message.content.startswith("mt!"):
		
		print("someone invoked me!")
		cmd = message.content.split(' ')
		cmd[0] = cmd[0][3:]
		
		try:
			await cmdlist[cmd[0]](message, snowflake, cmd, usernick)
		except:
			embed = discord.Embed(color = RED)
			embed.add_field(name = "Unknown Command", value = "Unknown command; use ` mt!help ` for help", inline = False)
			await message.channel.send(embed = embed)
	
	elif check_valid_mochi(message):
		print("Someone got some mochi flour! (" + usernick + ")") 	# prints a message

		current_mochi = read_user(snowflake, "mochi") + 1	# use the 'snowflake' to store info
		write_user(snowflake, "mochi", current_coins)		# write to json
		
		embed = Discord.embed(title = usernick + " got some mochi flour!");
		embed.set_footer("mochi flour: " + str(current_mochi))

token = os.environ.get("DISCORD_BOT_SECRET")
print("running with token: " + token)
coro = client.run(token)