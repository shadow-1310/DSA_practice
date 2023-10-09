class Solution:
    def find_moments(self, a):
        visited = set()
        far = 0
        time = 0
        res = 0
        for i in a:
            time += 1
            far = max(i, far)
            visited.add(i)
            if far > time:
                continue
            for k in range(1, far+1):
                if k not in visited:
                    continue
            res += 1

        return res

s = Solution()

print(s.find_moments([2,1,3,5,4]))

