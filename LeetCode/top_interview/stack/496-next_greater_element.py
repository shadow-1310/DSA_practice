#this is a brute force approach
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        res = []
        for num in nums1:
            found = -1
            for i in range(len(nums2)-1, -1, -1):
                target = nums2[i]
                if target == num:
                    break
                if target > num:
                    found = target

            res.append(found)

        return res


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        num1_map = {}
        stack = []
        res = [-1]*len(nums1)
        for i, num in enumerate(nums1):
            num1_map[num] = i
        for num in nums2:
            while stack and stack[-1] < num:
                n = stack.pop()
                res[num1_map[n]] = num
            if num in num1_map:
                stack.append(num)
        return res



nums1 = [4,1,2]; nums2 = [1,3,4,2]
s = Solution()
print(s.nextGreaterElement(nums1, nums2))
nums1 = [2,4]; nums2 = [1,2,3,4]
print(s.nextGreaterElement(nums1, nums2))
