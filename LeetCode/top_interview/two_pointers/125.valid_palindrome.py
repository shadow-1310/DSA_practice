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


s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
s3 = " "

print(valid_palindrome(s1))
print(valid_palindrome(s2))
print(valid_palindrome(s3))