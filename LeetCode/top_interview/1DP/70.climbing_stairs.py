
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


#this is a revision done on 12-09-2023, working ok on all LC testcases
class Solution:
    def climbStairs(self, n):
        if n == 1:
            return 1
        last = 1
        penulti = 1

        for i in range(n-1):
            temp = last
            last = penulti
            penulti = temp + last

        return penulti


    

s =Solution()
print(s.climbStairs(5))
