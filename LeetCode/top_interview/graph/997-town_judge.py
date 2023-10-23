class Solution:
    def findJudge(self, n, trust):
        incoming = [[] for i in range(n+1)]
        outgoing = [[] for i in range(n+1)]
        for a,b in trust:
            outgoing[a].append(b)
            incoming[b].append(a)

        for i in range(1, n+1):
            if len(incoming[i]) == n-1 and len(outgoing[i]) == 0:
                return i

        return -1

n = 3; trust = [[1,3],[2,3],[3,1]]
s = Solution()
print(s.findJudge(n,trust))
n = 3; trust = [[1,3],[2,3]]
print(s.findJudge(n,trust))
n = 2; trust = [[1,2]]
print(s.findJudge(n,trust))
