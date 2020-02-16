import os
import json

def trunc(fp):
	fp.truncate(0)
	fp.seek(0)

def read_user(username, prop, default = 0):
	fp = open("userinfo.json", "r")
	buf = fp.read()
	fp.close()

	obj = json.loads(buf)
	try:
		return obj[username][prop]
	except:
		print("there was a error...")
		obj.update({username: {"coins": 0, "isroot": False}})
		fp = open("userinfo.json", "r+")
		trunc(fp)
		fp.write(json.dumps(obj, sort_keys=True, indent=8))
		fp.close()
		return default

def write_user(username, prop, value):
	fp = open("userinfo.json", "r+")
	obj = json.loads(fp.read())
	obj.update({username: {prop: value}})
	trunc(fp)
	fp.write(json.dumps(obj, sort_keys=True, indent=8))
	fp.close()
