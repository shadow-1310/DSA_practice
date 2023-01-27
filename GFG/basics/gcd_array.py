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

arr = [18, 42, 70]
n = 3
print(brute(arr, n))