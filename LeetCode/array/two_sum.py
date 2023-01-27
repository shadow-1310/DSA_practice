def two_sum(arr: list, target: int) -> list:
    prevmap = {}
    for i, value in enumerate(arr):
        diff = target - value
        if diff in prevmap:
            return [prevmap[diff], i]
        else:
            prevmap[value] = i


nums = [2, 7, 11, 15]
target = 17
print(two_sum(nums, target))
