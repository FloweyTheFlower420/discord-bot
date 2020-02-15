import os
import json

def setup():
	if not os.path.isfile("./config.json"):
		print("config file not found, creating one from default...")
		default = {
			"coin-chance": 100
		}
		fp = open("config.json", "w")
		fp.write(json.dumps(default, indent=8))
		fp.close()
	if not os.path.isfile("./userinfo.json"):
		print("userinfo file not found, creating empty file...")
		fp = open("userinfo.json", "w")
		fp.write("{}")
		fp.close
		
