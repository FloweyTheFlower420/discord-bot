import os
import json

def setup():
	if not os.path.isfile("./config.json"):
		default = {
			"coin-chance": 100
		}
		fp = open("config.json", "w")
		fp.write(json.dumps(default))
		fp.close()
	if not os.path.isfile("./userinfo.json"):
		fp = open("userinfo.json", "w")
		fp.write("{}")
		fp.close
		