def brute(arr:list, n:int) -> int:
    def gcd(a:int, b:int) -> int:
        div = min(a, b)
        while div > 0:
            if a % div == 0 and b % div == 0:
                return div
            else:
                div -= 1
    hcf = arr[0]
    for i in range(1, n):
        hcf = gcd(arr[i], hcf)
    return hcf


#this is a revision done on 2023-09-12, woeking on all test cases of GFG
class Solution:
    def gcd(self, n, arr):
        def get_gcd(a,b):
            if not a or not b:
                return a if not b else b

            else:
                smaller = min(a, b)
                bigger = max(a, b )

                return get_gcd(smaller, bigger % smaller)

        curr = arr[0]
        for i in range(1, n):
            curr = get_gcd(curr, arr[i])

        return curr

arr = [18, 42, 70]
n = 3
print(brute(arr, n))
