from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz',
        }
        res = []
        
        def backtrack(i, curr):
            if i >= len(digits):
                res.append(''.join(curr))
                return
            
            for char in dict[digits[i]]:
                curr.append(char)
                backtrack(i+1, curr)
                curr.pop()
        backtrack(0, [])
        return res
            

d = '23'

s = Solution()
# print(s.letterCombinations(d))


# this is a revision done on 28-07-2023
# this is a correct solution and more optimized than previous one
class Solution:
    def letterCombinations(self, digits):
        mapping = {'2':'abc',
                    '3': 'def',
                    '4': 'ghi',
                    '5': 'jkl',
                    '6': 'mno',
                    '7': 'pqrs',
                    '8': 'tuv',
                    '9': 'wxyz'
                }
        res = []
        if len(digits) == 0:
            return res

        def dfs(index, curr):
            if index >= len(digits):
                res.append("".join(curr))
                return 

            if len(curr) > len(digits):
                return

            for char in mapping[digits[index]]:
                curr.append(char)
                dfs(index+1, curr)
                curr.pop()

        dfs(0, [])
        return res
                    


#revision done on 06-10-2023
class Solution:
    def letterCombinations(self, digits):
        res = []
        if len(digits) == 0:
            return res
        key_map = {
                '2' : 'abc',
                '3' : 'def',
                '4' : 'ghi',
                '5' : 'jkl',
                '6' : 'mno',
                '7' : 'pqrs',
                '8' : 'tuv',
                '9' : 'wxyz'
                }
        def dfs(l, curr):
            if l == len(digits):
                res.append("".join(curr))
                return
            for c in key_map[digits[l]]:
                curr.append(c)
                dfs(l+1, curr)
                curr.pop()

        dfs(0, [])
        return res

digs = "235"
test = ""
s = Solution()
print(s.letterCombinations(digs))
print(s.letterCombinations(test))

