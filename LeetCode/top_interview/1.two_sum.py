def two_sum(nums, target):
    diff_map = {}
    for index, num in enumerate(nums):
        diff = target - num
        if diff in diff_map:
            return [diff_map[diff], index]
        else:
            diff_map[num] = index

nums = [2, 7, 9,11]
target = 16
print(two_sum(nums, target))