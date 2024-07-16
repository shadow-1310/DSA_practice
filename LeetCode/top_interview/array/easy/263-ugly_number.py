from math import sqrt

#I tried this approach of getting all the prime factors of n, if any factor is not 2,3,5 then return False immediately
#but this approach is not working
class Solution:
    def isUgly(self, n):
        primes = {2,3,5}
        while n & 1 == 0:
            n = n >> 1

        for i in range(3, int(sqrt(n))+1, 2):
            if n % i == 0 and i not in primes:
                return False
            while n % i == 0:
                n = n // 3

        return True

class Solution:
    def isUgly(self, n):
        if n <= 0:
            return False

        for i in [2,3,5]:
            while n % i == 0:
                n = n // i

        return n == 1


class Solution:
    def isUgly(self, n):
        if n <= 0:
            return False
        while n & 1 == 0:
            n >>= 1
        while n % 3 == 0:
            n = n // 3
        while n % 5 == 0:
            n = n // 5

        return n == 1


#revision done on 2023-11-23
class Solution:
    def isUgly(self, n):
        if n == 0:
            return False
        while n & 1 == 0:
            n = n >> 1
        while n % 3 == 0:
            n = n / 3
        while n % 5 == 0:
            n = n / 5
        
        return True if n==1 else False



n = 121
n2 = 30
s = Solution()
print(s.isUgly(n))
print(s.isUgly(n2))
