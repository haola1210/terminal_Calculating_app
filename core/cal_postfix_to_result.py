import math
def Cal(Postfix): 
    stack = []
    for i in Postfix:
        if i.isdigit(): 
            stack.append(int(i))
        else: 
            if i == '^': 
                stack.append(math.pow(stack.pop(),stack.pop()))
            elif i == 'sqrt':
                stack.append(math.sqrt(stack.pop(),stack.pop()))
            elif i == '*':
                stack.append(stack.pop() * stack.pop())
            elif i == '/': 
                stack.append(stack.pop() / stack.pop())
            elif i == '+': 
                stack.append(stack.pop() + stack.pop())
            elif i == '-':
                stack.append(stack.pop() + stack.pop())
    return stack.pop()

            