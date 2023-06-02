def happy_number(n):
    if n == 1:
        return True
    
    all_nums = []
    while n != 1 :
        all_nums.append(n)
        digits = []

        while n > 0:
            digit = n % 10
            digits.append(digit)
            n = n // 10
        
        n = 0
        for num in digits:
            n += num**2

        if n == 1:
            return True

        if n in all_nums:
            return False


print(happy_number(19))