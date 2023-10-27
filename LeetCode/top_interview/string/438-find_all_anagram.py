#although this solution is correct, its time complexity is O(len(s)*len(p)), which is non desirable
#done on 27-10-2023
class Solution:
    def findAnagrams(self, s, p):
        n1 = len(s)
        n2 = len(p)
        target = [0]*26
        res = []

        for char in p:
            idx = ord(char) - ord('a')
            target[idx] += 1

        l = 0
        r = n2 - 1
        while r < n1:
            curr = [0]*26
            for i in range(l, r+1):
                idx = ord(s[i]) - ord('a')
                curr[idx] += 1
            if curr == target:
                res.append(l)

            l += 1
            r += 1

        return res


#this is an efficient solution, time complexity O(len(s))
#done on 17-10-2023
class Solution:
    def findAnagrams(self, s, p):
        res = []
        n1 = len(s)
        n2 = len(p)
        if n2 > n1:
            return res
        target = [0]*26
        curr = [0]*26
        for i in range(n2):
            idx1 = ord(s[i]) - ord('a')
            idx2 = ord(p[i]) - ord('a')
            target[idx2] += 1
            curr[idx1] += 1

        if target == curr:
            res.append(0)

        l = 0
        r = n2
        while r < n1:
            rem = ord(s[l]) - ord('a')
            add = ord(s[r]) - ord('a')
            curr[rem] -= 1
            curr[add] += 1

            if curr == target:
                res.append(l+1)
            l += 1
            r += 1

        return res



s1 = "cbaebabacd"; p1 = "abc"
s2 = "abab"; p2 = "ab"
sol = Solution()
print(sol.findAnagrams(s1,p1))
print(sol.findAnagrams(s2,p2))
