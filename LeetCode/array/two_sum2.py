def two_sum2(arr: list[int], target: int) -> list[int]:
    l = 0
    n = len(arr) - 1
    r = n
    while l < r:
        sum = arr[l] + arr[r]
        if sum > target:
            r -= 1
        elif sum < target:
            l += 1
        else:
            return [l+1, r+1]


nums = [2, 7, 11, 15]
target = 9
print(two_sum2(nums, target))
