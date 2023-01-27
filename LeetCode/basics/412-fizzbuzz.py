def brute(n:int):
    result = []
    nums = [i for i in range(1, n+1)]
    for n in nums:
        if n % 3 == 0 and n % 5 == 0:
            result.append("FizzBuzz")
        elif n % 3 == 0:
            result.append("Fizz")
        elif n % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(n))
    return result

n = 10
print(brute(n))