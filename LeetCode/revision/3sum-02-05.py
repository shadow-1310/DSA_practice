def three_sum(nums):
    sorted_nums = sorted(nums)
    result = []
    n = len(nums) - 1
    for index, num in enumerate(nums):
        left = index + 1
        right = n
        while left < right and index < n - 2:
            num_sum = num + nums[left] + nums[right]
            if num_sum < 0:
                left += 1
            elif num_sum > 0:
                right -= 1 
            else:
                result.append(num, nums[left], nums[right])
            # while nums[left] == nums[left-1]:
            #     left += 1
    return result

nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))
# print(sorted(nums))