import bisect

def brute(a:list, b:list, M:int, N:int) -> int:
    count = 0
    for i in range(M):
        for j in range(N):
            x = a[i]
            y = b[j]
            if x ** y > y ** x:
                count += 1
    return count

M = 4
X = [2, 3, 4, 5]
N = 3 
Y = [1, 2, 3]
print(brute(X, Y, M, N))

def num_pairs(a:list, b:list, M:int, N:int) -> int:
    a.sort()
    b.sort()
    zeros = 0
    ones = 0
    twos = 0
    three = 0
    four = 0
    ans = 0
    for i in range(N):
        if b[i] == 0:
            zeros += 1
        elif b[i] == 1:
            ones += 1
        elif b[i] == 2:
            twos += 1
        elif b[i] == 3:
            three += 1
        elif b[i] == 4:
            four += 1
    for j in range(M):
        if a[j] == 0:
            continue
        elif a[j] == 1:
            ans += zeros
        elif a[j] == 2:
            count = N - bisect.bisect_right(b, a[j]) 
            ans += count
            ans += zeros + ones
            ans -= three
            ans -= four 
        else:
            count = N - bisect.bisect_right(b, a[j]) 
            ans += count
            ans += zeros + ones
            if a[j] == 3:
                ans += twos

  
    return ans

print(num_pairs(X, Y, M, N))