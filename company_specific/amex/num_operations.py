# a function which given a string in binary number can find out after how many operation it will become zero, asked by AMEX in IITBHU
#done this on 03-09-2023
def solution(s):
    def get_base10(s):
        decimal = 0
        power = len(s) - 1

        for digit in s:
            decimal += int(digit) * (2**power)
            power -= 1

        return decimal

    num = get_base10(s)
    count = 0
    while num:
        if num % 2 == 0:
            num = num // 2
        else:
            num -= 1

        count += 1

    return count

print(solution('011100'))

