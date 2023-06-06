#correct solution. done on 06-06-2023
def eval_rpn(tokens):
    stack = []
    left = 0
    right = len(tokens)
    operators = ['+', '-', '*', '/']

    while left < right:
        token = tokens[left]

        if token not in operators:
            stack.append(token)
        
        else:
            if token == '+':
                new_val = int(stack[-2]) + int(stack[-1])
            
            elif token == '-':
                new_val = int(stack[-2]) - int(stack[-1])

            elif token == '*':
                new_val = int(stack[-2]) * int(stack[-1])

            elif token == '/':
                new_val = int(int(stack[-2]) / int(stack[-1]))

            stack.pop()
            stack.pop()
            stack.append(new_val)

        left += 1

    return stack[-1]


tokens1 = ["2","1","+","3","*"]
tokens2 = ["4","13","5","/","+"]
tokens3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
tokens4 = ["4","-2","/","2","-3","-","-"]

print(eval_rpn(tokens1))
print(eval_rpn(tokens2))
print(eval_rpn(tokens3))
print(eval_rpn(tokens4))