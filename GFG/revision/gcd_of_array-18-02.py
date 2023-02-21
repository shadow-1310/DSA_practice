def gcdOfArray(arr, n):
    if n == 1: # this condition must be added to avoid error when there is only one element in the array
        return arr[0]
    else:
        def gcd_of_two(a, b):
            m = max(a, b)
            n = min(a, b)
            if n == 0:
                return m
            else:
                return gcd_of_two(n, m%n)

        hcf = gcd_of_two(arr[0], arr[1])
        for i in range(2, n):
            hcf = gcd_of_two(hcf, arr[i])
        
        return hcf

test = [12, 24, 16, 40, 28, 2]
print(gcdOfArray(test, 6))