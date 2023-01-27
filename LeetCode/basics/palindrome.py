def brute(s:str)->bool:
    s = s.lower()
    test = ""
    for char in s:
        if char.isalnum():
            test += char
    print(test)
    if test == test[-1::-1]:
        return True
    else:
        return False

s = "A man, a plan, a canal: Panama"
print(brute(s))