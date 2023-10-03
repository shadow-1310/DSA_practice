def find_primes(n):
    primes = [True] * (n+1)
    res = []
    p = 2
    while p**2 <= n:
        if primes[p]:
            for i in range(p**2, n+1, p):
                primes[i] = False

        p += 1
    
    for i in range(2, n+1):
        if primes[i]:
            res.append(i)

    # return res
    #following return statement can be used to find number of primes in that range
    # print((n+1)/1000)
    return sum(primes) - 2 # subtracting 2 is neccessary because first two indexes are true and they are for 0 and 1


n = 1000000
n2 = 30
print(find_primes(n))
# print(find_primes(n2))
