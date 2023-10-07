#this is first attempt done on 07-10-2023
class Solution:
    def shipWithinDays(self, weight, days):
        def find_days(cap):
            res = 0
            i = 0
            while i < len(weight):
                curr_sum = 0
                while i < len(weight) and curr_sum + weight[i] <= cap:
                    curr_sum += weight[i]
                    i += 1
                res += 1
                # print(curr_sum,cap)
            # print("cap and days",cap, res)
            return res

        l = max(weight)
        r = sum(weight)
        res = r

        while l <= r:
            mid = (l+r) >> 1
            req_day = find_days(mid)
            if req_day > days:
                l = mid+1
            else:
                res = min(res, mid)
                r = mid - 1

        return res

# weights = [1,2,3,4,5,6,7,8,9,10]
# days = 5
# weights = [3,2,2,4,1,4]; days = 3
weights = [1,2,3,1,1]; days = 4
s = Solution()
print(s.shipWithinDays(weights, days))
