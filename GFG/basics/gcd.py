def brute(A:int, B:int) -> int:
    div = min(A, B)
    while div > 0:
        if A % div == 0 and B % div == 0:
            return div
        else:
            div -= 1


def euclidean_gcd(A:int, B:int)->int:
    m = max(A, B)
    n = min(A, B)
    if n == 0:
        return m
    else:
        return euclidean_gcd(n, m%n)

# GFG solution in class form
class Solution:
    def gcd(self, A, B):
        m = max(A, B)
        n = min(A, B)
        if n == 0:
            return m
        else:
            return Solution.gcd(self, n, m%n)

a = 14
b = 28
print(brute(a, b))
print(euclidean_gcd(a, b))
