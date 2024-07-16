def happy_number(n):
    if n == 1:
        return True
    
    all_nums = []
    while n != 1 :
        all_nums.append(n)
        digits = []

        while n > 0:
            digit = n % 10
            digits.append(digit)
            n = n // 10
        
        n = 0
        for num in digits:
            n += num**2

        if n == 1:
            return True

        if n in all_nums:
            return False


#this is a revision done on 0-09-2023, working on all testcases of LC
class Solution:
    def isHappy(self, n):
        loop = set()
        while True:
            loop.add(n)
            square = 0
            temp = n
            while temp > 0:
                square += (temp % 10)**2
                temp = temp // 10

            if square == 1:
                return True
            elif square in loop:
                return False

            n = square


#this revision was done on 14-10-2023
class Solution:
    def isHappy(self, n):
        if n == 1:
            return True
        visited = set()
        while n > 1:
            if n in visited:
                return False
            visited.add(n)
            curr_sum = 0
            while n > 0:
                curr_sum += (n % 10)**2
                n = n // 10

            n = curr_sum
            if n == 1:
                return True


#revision done on 2023-11-16
class Solution:
    def isHappy(self, n):
        seen = set()
        while n:
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
            rem = n
            n = 0
            while rem:
                dig = rem % 10
                rem = rem // 10
                n += dig ** 2



# print(happy_number(19))
# print(happy_number(2))
s  =Solution()
print(s.isHappy(19))
