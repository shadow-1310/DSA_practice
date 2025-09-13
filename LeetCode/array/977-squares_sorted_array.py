class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        res = []
        while left <= right:
            square_left = nums[left] ** 2
            square_right = nums[right] ** 2
        
            if square_right > square_left:
                res.append(square_right)
                right -= 1
            else:
                res.append(square_left)
                left += 1
        return res[::-1]

