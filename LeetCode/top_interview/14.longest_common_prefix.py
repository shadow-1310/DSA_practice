def longest_prefix(strs):
    list_of_strs = sorted(strs)
    common_prefix = ""
    first = list_of_strs[0]
    last = list_of_strs[-1]
    min_char = min(len(first), len(last))
    for i in range(min_char):
        if first[i] != last[i]:
            return common_prefix
        else:
            common_prefix += first[i]
    return common_prefix

input_str = ["flower","flow","flight"]
print(longest_prefix(input_str))