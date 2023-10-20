def find_mean(nums):
    left = 0
    right = len(nums)-1
    min_num = nums[0]

    while left < right:
        mid = (left+right) // 2
        min_num = min(min_num, nums[mid])

        if nums[mid] < nums[0]:
            right = mid - 1
            min_num = min(min_num, nums[right])
        
        elif nums[mid] >= nums[0]:
            left = mid + 1
            min_num = min(min_num, nums[left])    

    return min_num


#this is a revision done 2023-09-22
class Solution:
    def findMin(self, nums):
        left = 0
        right = len(nums)-1

        if nums[0] > nums[-1]:
            while left <= right:
                mid = (left+right) // 2
                if nums[mid-1] > nums[mid]:
                    return nums[mid]

                if nums[mid] >= nums[0]:
                    left = mid + 1

                elif nums[mid] < nums[0]:
                    right = mid - 1

        return nums[0]

#revision done on 20-10-2023, 
class Solution:
    def findMin(self, nums):
        l = 0
        n = len(nums)
        if n == 1:
            return nums[0]
        r = n-1
        if nums[0] < nums[-1]:
            return nums[0]

        while l <= r:
            mid = (l+r) >> 1
            if mid > 0 and nums[mid-1] > nums[mid]:
                return nums[mid]
            elif nums[mid] >= nums[0]:
                l = mid+1
            elif nums[mid] < nums[0]:
                r = mid - 1
            


nums = [3,4,5,1,2]
nums2 = [4,5,6,7,0,1,2]
nums3 = [11,13,15,17]
nums4 = [1]
nums4 = [2,1]

print(find_mean(nums))
print(find_mean(nums2))
print(find_mean(nums3))
s = Solution()
print(s.findMin(nums))
print(s.findMin(nums2))
print(s.findMin(nums3))
print(s.findMin(nums4))
