def brute(s:str, t:str) -> bool:
    s = s.lower()
    t = t.lower()
    unique_charcount_s = {}
    unique_charcount_t = {}
    for char in s:
        if char not in unique_charcount_s:
            unique_charcount_s[char] = 1
        else:
            unique_charcount_s[char] += 1
    
    for char in t:
        if char not in unique_charcount_t:
            unique_charcount_t[char] = 1
        else:
            unique_charcount_t[char] += 1
    if unique_charcount_s == unique_charcount_t:
        return True
    else:
        return False

s = "anagram"
t = "nagaram"
print(brute(s, t))