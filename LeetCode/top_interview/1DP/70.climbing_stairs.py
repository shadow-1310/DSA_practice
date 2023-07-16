
#this is not a correct solution. as it is done using backtracking it consumes lot of memory
#done on 15-07-2023
class Solution:
    def climbStairs(self, n: int):
        res = []

        def dfs(curr, tot):
            if tot == n:
                res.append(curr.copy())
                return
            
            if tot > n:
                return
            
            curr.append(1)
            dfs(curr, tot+1)
            curr.pop()

            curr.append(2)
            dfs(curr, tot+2)
            curr.pop()


        dfs([], 0)
        return res
    

#this is correct solution using DP with bottom up approach
#done on 15-07-2023
class Solution:
    def climbStairs(self, n: int):
        one = 1
        two = 1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        
        return one
    

s =Solution()
print(s.climbStairs(5))