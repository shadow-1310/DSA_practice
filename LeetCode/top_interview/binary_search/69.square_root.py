# the following approach doesnot work for Leetcode. 
# Although they mentioned nearest integer, they are considering the smaller closest integer only
# following approach will find the nearest integer, but it doesnot work for the test cases
def error_approach(x):
    nums = [n for n in range(1, x//2)]
    min_error = x
    dict = {}

    for num in nums:
        error = abs(num**2 - x)
        if error < min_error:
            min_error = error
            dict[min_error] = num
        else:
            continue

    return dict[min_error]


def normal(x):
    num = 1
    while num*num <= x:
        num += 1

    return num-1

#this is the most optiized approach in O(logN) time complexity
def binary_approach(x):
    left = 1
    right = x

    while left <= right:
        mid = (left+right) // 2

        if mid**2 == x:
            return mid
        elif mid**2 > x:
            right = mid - 1
        else:
            left = mid +1 

    return right

#this is a revision done on 2023-09-22
class Solution:
    def mySqrt(self, x):
        if x == 1:
            return 1
        left = 0
        right = x

        while left <= right:
            mid = (left+right)//2
            if mid ** 2 == x:
                return mid
            if mid ** 2 < x:
                left = mid + 1
            else:
                right = mid - 1

        return right



x = 110
print(error_approach(x))
print(normal(x))
print(binary_approach(x))
