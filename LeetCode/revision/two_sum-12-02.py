def two_sum(nums:list[int], target:int) -> list[int:]:
    hash_map = {}
    for index, num in enumerate(nums):
        diff = target - num
        if diff in hash_map:
            return [hash_map[diff], index]
        else:
            hash_map[num] = index

arr = [2, 7, 11, 15]
target = 9
print(two_sum(arr, target))