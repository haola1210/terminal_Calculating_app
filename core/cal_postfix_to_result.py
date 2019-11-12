import math
def Cal(Postfix): 
    stack = []
    for i in Postfix:
        if i.isdigit(): 
            stack.append(int(i))
        else: 
            if i == '^': 
                stack_sencond = stack.pop()
                stack.append(math.pow(stack.pop(),stack_sencond))
            elif i == 'sqrt':
                stack.append(math.sqrt(stack.pop()))
            elif i == '*':
                stack_sencond = stack.pop()
                stack.append(stack.pop() * stack_sencond)
            elif i == '/': 
                stack_sencond = stack.pop()
                stack.append(stack.pop() / stack_sencond)
            elif i == '+': 
                stack.append(stack.pop() + stack.pop())
            elif i == '-':
                stack.append(stack.pop() + stack.pop())
    return stack[-1]
            