#this method is not working o all testcases as it has some limitation
#I kept this one to remember the mistake
class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        reverse = True
        for i in range(n-1, 0, -1):
            if nums[i] > nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
                reverse = False
                break

        def do_reverse(l,r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        if reverse:
            do_reverse(0,n-1)

        else:
            do_reverse(i+1, n-1)


#this is correct solution
#done on 30-10-2023
class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        reverse = True
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                reverse = False
                break

        def do_reverse(l,r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        if reverse:
            do_reverse(0, n-1)

        else:
            for j in range(n-1, -1, -1):
                if nums[j] > nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
            do_reverse(i+1, n-1)


s = Solution()
nums1 = [1,2,3]
nums2 = [3,2,1]
nums3 = [1,3,2]
nums4 = [1,1,5]
s.nextPermutation(nums1)
s.nextPermutation(nums2)
s.nextPermutation(nums3)
print(nums1)
print(nums2)
print(nums3)
