def majority(nums):
    n = len(nums)
    count_map = {}
    for num in nums:
        if num not in count_map:
            count_map[num] = 1
        else:
            count_map[num] += 1
    for key in count_map:
        if count_map[key] > n/2:
            return key
        
nums = [2,2,1,1,1,2,2]
print(majority(nums))