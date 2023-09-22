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


#this is a revision done on 2023-09-21
class Solution:
    def dailyTemperatures(self, temperatures):
        res = [0]*len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_temp, stack_index = stack.pop()
                days = index - stack_index
                res[stack_index] = days

            stack.append([temp, index])

        return res




temperatures1 = [73,74,75,71,69,72,76,73]
temperatures2 = [30,40,50,60]

print(req_days(temperatures1))
print(req_days(temperatures2))
