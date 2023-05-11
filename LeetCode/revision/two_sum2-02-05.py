def two_sum2(numbers, target):
    left = 0
    right = len(numbers) - 1
    while left < right:
        num_sum = numbers[left] + numbers[right]
        if num_sum < target:
            left += 1
        elif num_sum > target:
            right -= 1 
        else:
            return [left+1, right+1]
        
nums = [2, 7, 11, 15]
target = 9
print(two_sum2(nums, target))