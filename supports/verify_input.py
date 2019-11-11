import re
def check(keys, input):
	if len(input) > 1:
		return "plz! Just type 1 character"
	else:
		strKeys = "["
		for key in keys:
			strKeys += key + ","
		strKeys += "]"
		if re.search(strKeys, input):
			return input
		else:
			return "Wrong key!"