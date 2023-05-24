#this is a wrong attempt. keeping it for reminder
def permute(nums):
    result = []
    start_pos = 0
    while start_pos < len(nums):
        combination = [nums[start_pos]]
        curr_pos = 0
        while curr_pos < len(nums):
            if curr_pos != start_pos:
                combination.append(nums[curr_pos])
            
            curr_pos += 1
        
        result.append(combination)
        start_pos += 1
    
    return result

nums = [1, 2, 3]
print(permute(nums))