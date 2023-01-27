def brute(x:int):
        remainder = abs(x)
        pow = len(str(remainder)) - 1
        reverse = 0
        while remainder > 0:
            unit_digit = remainder % 10
            reverse += unit_digit * (10**pow)
            remainder = remainder // 10
            pow -= 1
        if reverse >= -2**31 and reverse <= (2**31)-1:
            if x > 0:
                return reverse
            elif x < 0:
                return reverse*(-1)
            else:
                return 0
        else:
            return 0
    

x = 1534236469
print(brute(x))


