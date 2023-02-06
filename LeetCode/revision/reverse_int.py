def reverse(x:int)->int:
    if x >=0:
        sign = 1
    else:
        sign = 0
    x = abs(x)
    pow = len(str(x)) - 1
    rev = 0
    while x > 0:
        digit = x % 10
        rev += digit * (10**pow)
        x = x // 10
        pow -= 1
    if rev < -2**31 or rev > 2**31 - 1:
        return 0
    else:
        if sign == 1:
            return rev
        else:
            return rev * (-1)
    
        

test = -578
print(reverse(test))