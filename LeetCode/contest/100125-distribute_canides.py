#this is a contest problem 
#not optimized
class Solution:
    def distributeCandies(self, n, limit):
        cache = {}
        def backtrack(index, left):
            if index == 3 :
                if not left:
                    return 1
                else:
                    return 0
            if left < 0:
                return 0
            if (index,left) in cache:
                return cache[(index,left)]
            res = 0
            for i in range(limit+1):
                res += backtrack(index+1, left-i)
            cache[(index,left)] = res
            return res

        return backtrack(0,n)


class Solution:
    def distributeCandies(self, n, limit):
        cache = {}
        cache[0] = 1
        for i in range(1,n+1):
            cache[i] = cache[i-1] + 3

        return cache[n]

s = Solution()
n = 3; limit=3
print(s.distributeCandies(n, limit))
n = 5; limit=2
print(s.distributeCandies(n, limit))
