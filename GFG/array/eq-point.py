#optimized approach
def eq_point(A:list[int], N:int) -> int:
    if N == 1:
        return 1
    l = 0
    r = N - 1 
    for_sum = A[l]
    rev_sum = A[r]
    
    while l < r:        
        if for_sum == rev_sum and l == r-2:
            return l+2
        elif for_sum > rev_sum:
            r -= 1
            rev_sum += A[r]
        elif for_sum < rev_sum:
            l += 1
            for_sum += A[l]
        else:
            l += 1
            r -= 1
            for_sum += A[l]
            rev_sum += A[r]
    return -1

# test cases
a = [1,3,5,2,2,1,1,1, 0,1,1,2]
st = "20 17 42 25 32 32 30 32 37 9 2 33 31 17 14 40 9 12 36 21 8 33 6 6 10 37 12 26 21 3"
a2 = [int(num) for num in st.split()]
n2 = 30
n = 12
# print(a2)
print(eq_point(a, n))
print(eq_point(a2, n2))