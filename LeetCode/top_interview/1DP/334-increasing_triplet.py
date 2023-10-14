class Solution:
    def increasingTriplet(self, nums):
        left = [1]*len(nums)
        right = [1]*len(nums)
        curr_min = nums[0]
        for i in range(len(nums)):
            if nums[i] < curr_min:
                curr_min = nums[i]

            left[i] = curr_min
        
        curr_max = nums[-1]
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > curr_max:
                curr_max = nums[i]

            right[i] = curr_max

        for i in range(len(nums)):
            if left[i] < nums[i] and right[i] > nums[i]:
                return True

        return False



#this revision was done on 12-10-2023
class Solution:
    def increasingTriplet(self, nums):
        left = [1]*len(nums)
        right = [1]*len(nums)
        curr_min = nums[0]
        for i in range(len(nums)):
            if nums[i] < curr_min:
                curr_min = nums[i]
            left[i] = curr_min
        curr_max = nums[-1]
        for i in range(len(nums)-1,-1,-1):
            if nums[i] > curr_max:
                curr_max = nums[i]
            right[i] = curr_max

        for i in range(len(nums)):
            if nums[i] > left[i] and nums[i] < right[i]:
                return True

        return False


s = Solution()
nums = [2,1,5,0,4,6]
print(s.increasingTriplet(nums))
print(s.increasingTriplet([1,2,3,4,5]))
print(s.increasingTriplet([1,0,2,-1,4]))
