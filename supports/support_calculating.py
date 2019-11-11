import re
####### priority function
def Priority(data):
	if isOperator(data):
		if data == "^":
			return 1
		if data == "*":
			return 2
		if data == "/":
			return 2
		if data == "+":
			return 3
		if data == "-":
			return 3
	else:
		return 0

######## isOperator function
def isOperator(data):
	return re.search("[\^*/+-]", data)