# correct solution. done on 06-06-2023
# basic idea is we donot do any operation until we encounter nthe next operator, then we take a decision
def calculate(s):
    stack = []
    pre_op = '+'
    s += '+'
    num = 0
    
    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)

        elif char == ' ':
            continue

        else:
            if pre_op == '+':
                stack.append(num)

            elif pre_op == '-':
                stack.append(-num)

            elif pre_op == '*':
                operand = stack.pop()
                stack.append(operand * num)

            else:
                operand = stack.pop()
                stack.append(int(operand / num))

            num = 0
            pre_op = char

    return sum(stack)


s1 = "3+2*2"
s2 = " 3/2 "
s3 = " 3+5 / 2 "

print(calculate(s1))
print(calculate(s2))
print(calculate(s3))
