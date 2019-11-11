from supports import support_calculating as sC
def infix_to_postfix(express):
	Postfix = []
	stack = []
	for i in express:
		if not sC.isOperator(i) and i != "(" and i != ")":
			Postfix.append(i)
		else:
			if i == ")" :
				while len(stack) > 0 and stack[-1] != "(":
					Postfix.append(stack.pop())
				if len(stack) > 0:
					stack.pop()      
			else:
				while len(stack) > 0 and stack[-1] != "(" and i != "(" and sC.Priority(stack[-1]) < sC.Priority(i):
					Postfix.append(stack.pop())
				stack.append(i)

	while len(stack) > 0:
		Postfix.append(stack.pop())             
	return Postfix
