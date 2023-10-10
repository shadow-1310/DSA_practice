class Solution:
    def numRollsToTarget(self, n, k, target):
        cache = {}
        def backtrack(roll, rem):
            if roll == n:
                if rem == 0:
                    return 1
                return 0

            if (roll, rem) in cache:
                return cache[(roll, rem)]

            ways = 0
            for i in range(1, k+1):
                ways += backtrack(roll+1, rem - i)
            cache[(roll, rem)] = ways
            return ways

        return backtrack(0, target) % (pow(10,9)+7)

s = Solution()
print(s.numRollsToTarget(2,6,7))
print(s.numRollsToTarget(1,6,3))
print(s.numRollsToTarget(30,30,500))
print(s.numRollsToTarget(3,6,12))

