import re
import math
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
		return None

######## isOperator function
def isOperator(data):
	if len(data) == 1:
		return re.search("[\^*/+-]", data)
	else: 
		return None

####### make_infix function
def make_infix(express):
	infix = []
	temp = ""
	for i in range(len(express)):
		if express[i].isdigit():
			temp += express[i]
		elif express[i] == "-" and (i == 0 or i != 0 and (isOperator(express[i-1]) or express[i-1] == "(" )):
				temp += "-"
				continue
		else:
			if temp == "":
				infix.append(express[i])
			else:
				infix.append(temp)
				infix.append(express[i])
				temp = ""
	if temp.isdigit() or temp.lstrip("-").isdigit():
		infix.append(temp)
	return infix
