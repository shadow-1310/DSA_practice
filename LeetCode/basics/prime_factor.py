def prime_factor(N:int)->list:
    divisor = 2
    factors = []
    while divisor <= N:
        if N % divisor == 0:
            factors.append(divisor)
            N = int(N / divisor)
        else:
            divisor += 1

    return sorted(list(set(factors)))

n = 33
print(prime_factor(n))
