def two_sum2(numbers:list[int], target:int) -> list[int]:
    n = len(numbers) - 1
    l = 0
    r = n
    while l < r:
        sum = numbers[l] + numbers[r]
        if sum > target:
            r -= 1
        elif sum < target:
            l += 1
        else:
            return [l+1, r+1]

test = [2, 7, 11, 15]
target = 9
print(two_sum2(test, target))