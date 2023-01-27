def lcmOfArray(N:int, A:list) -> int:
    def gcd(a, b):
        m = max(a, b)
        n = min(a, b)
        if n == 0:
            return m
        else:
            return gcd(n, m % n)
    def lcm(a, b):
        product = a * b 
        lcm = product // gcd(a,b)
        return lcm
    lcm_of_array = A[0]
    for i in range(1, N):
        lcm_of_array = lcm(A[i], lcm_of_array)
    return lcm_of_array

a = [4, 6, 3, 8]
n = 4
print(lcmOfArray(n, a))
    
# solution for GFG in the form of class

class Solution:
    def lcmOfArray(self, N:int, A:list) -> int:
        def gcd(a, b):
            m = max(a, b)
            n = min(a, b)
            if n == 0:
                return m
            else:
                return gcd(n, m % n)
        def lcm(a, b):
            product = a * b 
            lcm = product // gcd(a,b)
            return lcm % 1000000007
        lcm_of_array = A[0]
        for i in range(1, N):
            lcm_of_array = lcm(A[i], lcm_of_array)
        return lcm_of_array % 1000000007