import discord

RED = 0xcc2204
CYAN = 0x119f8d
GRN = 0x02a81f

async def argerror(cmdname, channel):
        embed = discord.Embed(color = RED)
        embed.add_field(name = "Incorrect Command Useage", value = "Incorrect useage; use ` mt!help " + cmdname +" `.", inline = False)
        await channel.send(embed = embed)
async def permerror(usernick, channel):
        embed = discord.Embed(color = RED)
        embed.add_field(name = "Permission Denied", value = "Sorry, " + usernick + ", you do not have sufficient permissions to preform this action.", inline = False)
        await channel.send(embed = embed)

async def usererror(username, channel):
        embed = discord.Embed(color = RED)
        embed.add_field(name = "Can't Find Person", value = "unable to find " + username + ". Maybe they are eating mochi?", inline = False)
        await channel.send(embed = embed)

helpembed = discord.Embed(title = "Mochitime Help", description = "To see a specific help page, use `mt!help [page]`.", color = CYAN)
helpembed.add_field(name = "Page 1 | Economy", value = "This page involves command that deals with money.", inline = False)

roothelpembed = discord.Embed(title = "Mochitime Help", description = "To see a specific help page, use `mt!help [page]`.", color = CYAN)
roothelpembed.add_field(name = "Page '1' | Economy", value = "This page involves command that deals with money.", inline = False)
roothelpembed.add_field(name = "Page 'm' | mochi-lord commands", value = "This page is for root commands used for debugging.", inline = False)

setroothelp = discord.Embed(color = CYAN)
setroothelp.add_field(name = "Command Help: setlord", value = "Sets user to `mochi-lord`.", inline = False)
setroothelp.add_field(name = "Useage", value = "`mt!setlord [username]`.", inline = False)
setroothelp.set_footer(text = "Requires root permissions.")

coinshelp = discord.Embed(color = CYAN)
coinshelp.add_field(name = "Command Help: mflour", value = "Displays how much coins you have.", inline = False)
coinshelp.add_field(name = "Useage", value = "`mt!mflour`. All arguments are ignored.", inline = False)

donatehelp = discord.Embed(color = CYAN)
donatehelp.add_field(name = "Command Help: donate", value = "gives mochi flour to a user")
donatehelp.add_field(name = "Useage", value = "`mt!donate [username] [amount]. \nIf you don't have enough mochi flour, nothing will happen.")

page1help = discord.Embed(color = CYAN, title = "Page 1 - Economy", description = "This page involves command that deals with mochi flour.")
page1help.add_field(name = "mflour", value = "shows how much mochi flour you have", inline = False)
page1help.add_field(name = "donate", value = "gives mochi flour to someone", inline = False)

cmdhelp = {
	"coins": coinshelp,
	"donate": donatehelp,
	"setroot": setroothelp,
	"1": page1help
}
