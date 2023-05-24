def three_sum(nums):
    n = len(nums)
    nums.sort()
    first = 0
    third = n - 1
    output = []
    while first < third - 1:
        while first != 0 and first < n and nums[first] == nums[first-1]:
            first += 1

        second = first + 1 
        third = n-1
        while second < third:
            sum = nums[first] + nums[second] + nums[third]

            if sum > 0:
                third -= 1
            elif sum < 0:
                second += 1
            else:
                output.append([nums[first], nums[second], nums[third]])
                second += 1
            
                while second < third and nums[second] == nums[second-1]:
                    second += 1

        first += 1

    return output

nums = [-1,0,1,2,-1,-4]
nums2 = [0,0,0,0]
print(three_sum(nums))