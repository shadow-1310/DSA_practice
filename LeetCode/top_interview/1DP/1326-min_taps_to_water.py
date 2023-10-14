#first aproach done on 12-10-2023
class Solution:
    def minTaps(self, n, ranges):
        spread = [[0,0] for i in range(n+1)]
        for i in range(n+1):
            lb = i - ranges[i]
            ub = i + ranges[i]
            spread[i] = [lb,ub]
        lb = 0
        ub = 0

        count = 0
        while ub < n:
            for l,r in spread:
                if l <= lb and r > ub:
                    ub = r
            if lb == ub:
                return -1
            lb = ub
            count += 1
            
        return count if count else -1


class Solution:
    def minTaps(self, n, ranges):
        count = 0
        lb, ub = 0, 0

        while ub < n:
            for i in range(n+1):
                if i - ranges[i] <= lb and i+ranges[i] > ub:
                    ub = i + ranges[i]
            
            if lb == ub:
                return -1
            lb = ub
            count += 1
        return count


taps = [3,4,1,1,0,0]
s = Solution()
print(s.minTaps(5, taps))
print(s.minTaps(3, [0,0,0,0]))
