def lcmOfArray(N:list[int], A:list[int]):
    if N == 1:
        return A[0]
    else:
        def lcmOfTwo(a, b):
            m = max(a, b)
            n = min(a, b)
            if n == 0:
                gcd =  m
            else:
                gcd = lcmOfTwo(n, m%n)
            
            return (a*b) // gcd

        lcm = lcmOfTwo(A[0], A[1])
        for i in range(2, N):
            lcm = lcmOfTwo(lcm, A[i])
        return lcm

test = [17, 3, 51]
print(lcmOfArray(3, test))