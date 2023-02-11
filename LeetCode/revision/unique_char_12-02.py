def unique_char(s:str) ->str:
    count_char = {}
    for char in s:
        if char not in count_char:
            count_char[char] = 1
        else:
            count_char[char] += 1
    for index, char in enumerate(s):
        if count_char[char]== 1:
            return index
    return -1

test = 'loveleetcode'
print(unique_char(test))