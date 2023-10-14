class Solution:
    def LIS0or1(self, nums):
        lis = [1]*len(nums)

        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                diff = abs(nums[i] - nums[j])
                if diff == 0 or diff == 1:
                    lis[i] = max(lis[i], 1 + lis[j])

        return max(lis)


class Solution:
    def LIS0or1(self, N, A):
        lis = [1]*N
        for i in range(N-1, -1, -1):
            for j in range(i+1, N):
                if abs(A[i] - A[j]) == 1:
                    lis[i] = max(lis[i], 1+lis[j])

        return max(lis)


n1 = [1,2,3,4,5,3,2]
n2 = [10,9,4,5,4,8,6]
n3 = [1,2,3,2,3,7,2,1]
s = Solution()
print(s.LIS0or1(7,n1))
print(s.LIS0or1(n2))
print(s.LIS0or1(n3))
