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


# this is a revision done on 12-09-2023, but not working for GFG testcases
class Solution:
    def lcmOfArray(self, N, A):
        def get_gcd(a, b):
            if not a or not b:
                return a if not b else b

            else:
                smaller = min(a, b)
                bigger = max(a, b)

                return get_gcd(smaller, bigger % smaller)

        curr = A[0] 

        for i in range(1, N):
            curr = (curr * A[i]) // (get_gcd(curr, A[i]) / 1000000007)

        return curr 
