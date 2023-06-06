# correct solution. done one 06-06-2023
def req_days(temperatures):
    res = [0] * len(temperatures)
    mono_stack = []

    for index, temp in enumerate(temperatures):
        while mono_stack and temp > mono_stack[-1][0]:
            stack_index = mono_stack[-1][1]
            res[stack_index] = index - stack_index
            mono_stack.pop()

        mono_stack.append([temp, index])

    return res


temperatures1 = [73,74,75,71,69,72,76,73]
temperatures2 = [30,40,50,60]

print(req_days(temperatures1))
print(req_days(temperatures2))