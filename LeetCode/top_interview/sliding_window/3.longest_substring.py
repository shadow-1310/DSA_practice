# Although the following approach works for initial test cases, it fails in basic concept

def find_longest(s):
    if len(s) == 1:
        return 1
    
    left = 0
    count_map = {}
    right = left
    max_count = 0
    count = 0

    while left <= right and right < len(s):
        if s[right] in count_map:
            if s[right] != s[right-1]:
                left = right - 1
                right = left
            else:
                left = right
            count = 0
            count_map = {}
        else:
            count_map[s[right]] = 1
            count += 1
            max_count = max(count, max_count)
            right += 1

    return max_count

# this is the correct approach, done on 30-05-2023
def find_longest(s):
    if len(s) == 1:
        return 1
    
    left = 0
    right = left
    seen_map = {}
    max_count = 0

    while left <= right and right < len(s):
        char = s[right]
        if char in seen_map and seen_map[char] >= left:
            left = seen_map[char] + 1
        
        seen_map[char] = right
        count = right - left + 1
        max_count = max(max_count, count)
        right += 1

    return max_count


# this is a revision on 02-06-2023
# mistake was forgot to include the condition pos_map[s[right]] >= left
def find_longest_ss(s):
    if len(s) == 1:
        return 1
    
    max_count = 0
    left = 0
    right = left
    pos_map = {}

    while right < len(s):
        if s[right] in pos_map and pos_map[s[right]] >= left:
            left = pos_map[s[right]] + 1
            pos_map[s[right]] = right
            
        else:
            pos_map[s[right]] = right

        count = right - left + 1
        max_count = max(max_count, count)
        right += 1
    
    return max_count

s = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"
s4 = "abba"

print(find_longest(s))
print(find_longest(s2))
print(find_longest(s3))
print(find_longest(s4))