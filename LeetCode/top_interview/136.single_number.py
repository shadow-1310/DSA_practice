def single_number(nums):
    count_map = {}
    for num in nums:
        if num not in count_map:
            count_map[num] = 1
        else:
            count_map[num] += 1
    for key in count_map:
        if count_map[key] == 1:
            return key
        
nums = [4,1,2,1,2]
print(single_number(nums))