def reverse(x:int):
    if x > 0:
        sign = 1
    elif x < 0:
        sign = -1
    else:
        return 0
    x = abs(x)
    pow = len(str(x)) - 1
    rev = 0
    while x > 0:
        digit = x % 10
        rev += digit * 10**pow
        pow -= 1
        x = x // 10
    rev = rev * sign
    if rev > 2**31 - 1 or rev < -2**31:
        return 0
    return rev

test = -2569008700
print(reverse(test))
