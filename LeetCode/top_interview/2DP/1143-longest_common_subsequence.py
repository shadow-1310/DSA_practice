#correct solution using 2D matrix approach
# done on 24-07-2023
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        matrix = [ [0 for i in range(len(text2)+1) ] for j in range(len(text1)+1) ]
        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    matrix[i][j] = 1+ matrix[i+1][j+1]
                else:
                    matrix[i][j] = max(matrix[i+1][j], matrix[i][j+1])

        return matrix[0][0]


class Solution:
    def longestCommonSubsequence(self, text1, text2):
        matrix = [ [ 0 for i in range(len(text2)+1)] for j in range(len(text1)+1)]

        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    matrix[i][j] = 1 + matrix[i+1][j+1]

                else:
                    matrix[i][j] = max(matrix[i+1][j], matrix[i][j+1])

        return matrix[0][0]


class Solution:
    def longestCommonSubsequence(self, text1, text2):
        cache = [ [0] * (len(text2) +1) for i in range(len(text1)+1) ] 
        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    cache[i][j] = 1 + cache[i+1][j+1]

                else:
                    cache[i][j] = max(cache[i+1][j], cache[i][j+1])

        return cache[0][0]


s = Solution()
# t1 = 'abcde'
# t2 = 'ace'
# t1 = 'abc'
# t2 = 'abc'
t1 = 'abc'
t2 = 'def'
print(s.longestCommonSubsequence(t1,t2))
