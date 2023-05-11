def two_sum(nums:list[int], target:int):
    diff_map = {}
    for index, num in enumerate(nums):
        diff = target - num
        if diff in diff_map:
            return [diff_map[diff], index]
        else:
            diff_map[num] = index

if __name__ == '__main__':
    nums = [2, 7, 8, 11, 45,1]
    target = 9
    print(two_sum(nums, target))
