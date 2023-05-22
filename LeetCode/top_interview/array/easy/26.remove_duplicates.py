# def remove_duplicates(nums):
#     count = {}
#     for position, num in enumerate(nums):
#         if num not in count:
#             count[num] = 1
#         else:
#             nums.pop(position)
#     return len(list(count.keys()))


def remove_duplicates(nums):
    i = 0
    while i < len(nums):
        if i != 0 and nums[i] == nums[i-1]:
            nums.pop(i)
        else:
            i += 1
    return len(nums)


nums = [0,0,1,1,1,2,2,3,3,4]
print(remove_duplicates(nums))