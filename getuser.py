import os
import json

def trunc(fp):
	fp.truncate(0)
	fp.seek(0)

def read_user(username, prop):
	username = username.replace("#", "-")
	fp = open("userinfo.json", "r")
	buf = fp.read()
	fp.close()

	obj = json.loads(buf)
	try:
		return obj[username][prop]
	except:
		print("there was a error...")
		obj.update({username: {prop: 0}})
		fp = open("userinfo.json", "r+")
		trunc(fp)
		fp.write(json.dumps(obj, sort_keys=True, indent=8))
		fp.close()
		return 0

def write_user(username, prop, value):
	username = username.replace("#", "-")
	fp = open("userinfo.json", "r+")
	obj = json.loads(fp.read())
	obj.update({username: {prop: value}})
	trunc(fp)
	fp.write(json.dumps(obj, sort_keys=True, indent=8))
	fp.close()
