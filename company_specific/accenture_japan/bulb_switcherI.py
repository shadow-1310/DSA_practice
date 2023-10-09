import math
#this is a brute force approach with O(N^2) time complexity
def remained(n):
    status = [False] * (n+1)
    for i in range(1, n+1):
        for j in range(i, n+1, i):
            status[j] = not status[j]

    return sum(status[1:])

#this approach uses O(logN) time, done on 07-10-2023
def on_bulbs(n):
    return int(math.sqrt(n))

print(remained(5))
print(on_bulbs(10000))
