#this problem was asked in OA of TSMC in IIT Delhi
class Solution:
    def threePalindromicSubstrings(self, word):
        def is_palindrome(w):
            l = 0
            r = len(w)-1
            while l < r:
                if w[l] != w[r]:
                    return False
                l += 1
                r -= 1
            return True

        n = len(word)
        if n < 3:
            return ['Impossible']
        i = 0
        j = 1
        while i < n-2 and j < n-1:
            j = i+1
            k = j+1
            word1 = word[:i+1]
            word2 = word[i+1:j+1]
            word3 = word[j+1:]
            if not is_palindrome(word1):
                i += 1
            elif is_palindrome(word1) and (not is_palindrome(word2) or not is_palindrome(word3)):
                j = i+1
                for k in range(j, n-1):
                    word2 = word[i+1:k+1]
                    word3 = word[k+1:]
                    print(word1, word2, word3)
                    if is_palindrome(word2) and is_palindrome(word3):
                        return [word1, word2, word3]

                i += 1
            elif is_palindrome(word1) and is_palindrome(word2) and is_palindrome(word3):
                return [word1, word2, word3]
        return ['Impossible']

s = Solution()
word = 'kayakracecartenet'
print(s.threePalindromicSubstrings(word))
word = 'aardvark'
print(s.threePalindromicSubstrings(word))
word = 'tenet'
print(s.threePalindromicSubstrings(word))
word = 'aaaaa'
print(s.threePalindromicSubstrings(word))
word = 'madamciviclevel'
print(s.threePalindromicSubstrings(word))
