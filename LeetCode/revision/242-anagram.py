def anagram(s:str, t:str) -> bool:
    hash_s = {}
    hash_t = {}
    for char in s:
        if char not in hash_s:
            hash_s['char'] = 1
        else:
            hash_s['char'] += 1
    for char in t:
        if char not in hash_s:
            hash_t['char'] = 1
        else:
            hash_t['char'] += 1
    if hash_s == hash_t:
        return True
    else:
        return False

a = 'anagram'
b = 'nagaram'
print(anagram(a, b))