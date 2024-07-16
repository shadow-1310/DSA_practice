def shortest_string(s):
    stack = []
    for char in s:
        if stack and (char=='1' and (stack[-1]=='0' or stack[-1]=='1')):
            stack.pop()
        else:
            stack.append(char)

    return len(stack)

print(shortest_string('1011'))
s = "0011101111"
print(shortest_string(s))
s = "0010110"
print(shortest_string(s))
