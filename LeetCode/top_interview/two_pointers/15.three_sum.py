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


#revision done on 08-10-2023
class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i,num in enumerate(nums):
            if i >0  and nums[i-1] == nums[i]:
                continue
            left = i+1
            right = len(nums) - 1
            while left < right :
                curr = num + nums[left] + nums[right]
                if curr < 0:
                    left += 1
                elif curr > 0:
                    right -= 1
                else:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    while left < len(nums)  and nums[left] == nums[left-1]:
                        left += 1

        return res
                    

nums = [-1,0,1,2,-1,-4]
nums2 = [0,0,0,0]
print(three_sum(nums))
s = Solution()
print(s.threeSum(nums))
print(s.threeSum(nums2))
