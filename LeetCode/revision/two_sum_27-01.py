def two_sum(arr:list, target:int) -> list:
    prev = {}
    for i, num in enumerate(arr):
        diff = target - num
        if diff in prev:
            return [prev[diff], i]
        else:
            prev[num] = i

arr = [2, 7, 11, 15]
target = 9
print(two_sum(arr, target))