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

#revised on 14-10-2023
#here the commented line is the mistake I made
class Solution:
    def productExceptSelf(self, nums):
        product = [1]*len(nums)
        for i in range(1,len(nums)):
            product[i] = product[i-1] * nums[i-1]

        res = 1
        for i in range(len(nums)-2, -1, -1):
            res *= nums[i+1]
            # product[i] = product[i-1] * res
            product[i] *= res

        return product


class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1]*n
        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]

        postfix = 1
        for i in range(n-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res



nums = [1,2,3,4]
s = Solution()
print(s.productExceptSelf(nums))
print(find_product(nums))
