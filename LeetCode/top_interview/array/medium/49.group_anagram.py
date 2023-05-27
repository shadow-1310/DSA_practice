def group_anagram(strs):
    result = {}
    for word in strs:
        count = [0]*26
        for char in word:
            count[ord(char) - ord('a')] += 1

        if tuple(count) not in result:
            result[tuple(count)] = [word]
        else:
            result[tuple(count)].append(word)

    return list(result.values())
    

strs = ["eat","tea","tan","ate","nat","bat"]
strs2 = [""]
strs3 = ["a"]

print(group_anagram(strs))
print(group_anagram(strs2))
print(group_anagram(strs3))