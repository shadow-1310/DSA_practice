def find_product(nums):
    n = len(nums)
    res = [1] * n
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(n-1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]

    return res


#this is a revision done on 07-09-2023, working on all test cases of LC
class Solution:
    def productExceptSelf(self, nums):
        product = [1]*len(nums)
        for i in range(1, len(nums)):
            product[i] = product[i-1] * nums[i-1]
        
        temp = nums[-1]
        for i in range(len(nums) -2, -1, -1):
            product[i] *= temp
            temp *= nums[i]

        return product


nums = [1,2,3,4]
print(find_product(nums))
