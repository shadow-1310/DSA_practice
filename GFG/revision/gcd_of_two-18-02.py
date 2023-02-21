# euclidean approach
def gcd(A, B):
    m = max(A, B)
    n = min(A, B)
    if n == 0:
        return m
    else:
        return gcd(n, m%n)

num1 = 14
num2 = 28
print(gcd(num1, num2))

