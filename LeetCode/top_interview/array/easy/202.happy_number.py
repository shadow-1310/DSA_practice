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


print(happy_number(19))
