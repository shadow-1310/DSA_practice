def brute(num:int) -> int:
    if num == 1:
        return 1
    else:
        return num * brute(num-1)

num = 5
print(brute(num))