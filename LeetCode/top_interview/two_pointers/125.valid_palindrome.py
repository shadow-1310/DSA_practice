def valid_palindrome(s):
    s = s.lower()
    s = s.replace(' ', '')
    test = ""
    for char in s:
        if char.isalnum():
            test += char
        else:
            continue

    left = 0
    right = len(test) - 1
    while left <= right:
        if test[left] != test[right]:
            return False
        
        left += 1
        right -= 1

    return True


class Solution:
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            while not s[left].isalnum() and left < right:
                left += 1
            while not s[right].isalnum() and right > left:
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


class Solution:
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1
        while left <= right:
            while left <= right and not s[left].isalnum():
                left += 1
            while right >= left and not s[right].isalnum():
                right -= 1

            if left <= right and s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True


s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
s3 = " "

print(valid_palindrome(s1))
print(valid_palindrome(s2))
print(valid_palindrome(s3))
