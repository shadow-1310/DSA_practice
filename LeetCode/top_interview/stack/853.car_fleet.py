# this is the correct solution. done on 06-06-2023
def car_fleet(target, position, speed):
    pair = [[p,s] for p, s in zip(position, speed)]
    stack = []

    for p, s in sorted(pair)[::-1]:
        stack.append((target - p) / s)

        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()

    return len(stack)


#this is a revision done on 2023-09-21, working on all LC testcases
class Solution:
    def carFleet(self, target, position, speed):
        data = list(zip(position, speed))
        data.sort(reverse = True)
        stack = []

        for p,s in data:
            time = (target-p)/s
            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)


class Solution:
    def carFleet(self, target, position, speed):
        stack = []
        comb = list(zip(position, speed))
        comb.sort(reverse=True))
        for pos, sped in comb:
            time = (target-pos) / spd



target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

s = Solution()
print(s.carFleet(target, position, speed))

# print(car_fleet(target, position, speed))
