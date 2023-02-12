def palindrome(s:str):
    s = s.lower()
    new_s = ""
    for char in s:
        if char.isalnum():
            new_s += char
    reverse_s = new_s[::-1]
    if reverse_s == new_s:
        return True
    else:
        return False

test = "A man, a plan, a canal: Panama"
print(palindrome(test))