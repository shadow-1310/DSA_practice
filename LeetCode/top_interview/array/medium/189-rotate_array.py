#this solution uses extra space of O(N)
class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        temp = [0]*n
        for i in range(n):
            new = (i + k) % n
            temp[new] = nums[i]

        for i in range(n):
            nums[i] = temp[i]

#this is optimized solution with O(1) extra space
class Solution:
    def rotate(self, nums, k):
        def reverse_arr(l,r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        n = len(nums)
        k = k % n
        reverse_arr(0, n-1)
        reverse_arr(0, k-1)
        reverse_arr(k, n-1)


#revision done on 2023-11-23
class Solution:
    def rotate(self, nums, k):
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        n = len(nums)
        if n == 1:
            return
        k = k % n
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)



nums1 = [1,2,3,4,5,6,7]; k1 = 3
nums2 = [-1]; k2 = 2
nums3 = [1,2]; k3 = 3
s = Solution()
s.rotate(nums1, k1)
s.rotate(nums2, k2)
s.rotate(nums3, k3)
print(nums1)
print(nums2)
print(nums3)

