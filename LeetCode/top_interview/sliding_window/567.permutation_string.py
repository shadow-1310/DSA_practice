# this is correct solution . this is first attempt
def check_inclusion(s1, s2):
    if len(s1) > len(s2):
        return False
    
    map_s1 = [0]*26
    map_s2 = [0]*26

    for i in range(len(s1)):
        map_s1[ord(s1[i]) - ord('a')] += 1
        map_s2[ord(s2[i]) - ord('a')] += 1

    left = 0
    right = left + len(s1) # we initialize right pointer to one more length of s1, cause we already mapped tille len(s1)
    matches = 0

    for i in range(26):
        if (map_s1[i] == map_s2[i]):
            matches += 1

    while right < len(s2):
        if matches == 26:
            return True
        
        index_left = ord(s2[left]) - ord('a')
        map_s2[index_left] -= 1

        if map_s1[index_left] == map_s2[index_left]:
            matches += 1

        elif map_s1[index_left] == map_s2[index_left] + 1:
            matches -= 1

        index_right = ord(s2[right]) - ord('a')
        map_s2[index_right] += 1

        if map_s1[index_right] == map_s2[index_right]:
            matches += 1
        
        elif map_s1[index_right] == map_s2[index_right] - 1:
            matches -= 1

        left += 1
        right += 1

    return matches == 26 # it is necessary because the last loop is unchecked by the previous check condition


# this is also correct solution. It is copied from Neetcode Solutions
def checkInclusion(s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26


#this is a revision done on 07-09-2023, it is working fine in LC all test cases
#time complexity is O(s1 + 26*s2) and it is less optimized than previous approach
class Solution:
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        map_s1 = [0]*26
        map_s2 = [0]*26
        for i in range(len(s1)):
            idx1 = ord(s1[i]) - ord('a')
            idx2 = ord(s2[i]) - ord('a')
            map_s1[idx1] += 1
            map_s2[idx2] += 1

        def check_match(m1, m2):
            for i in range(len(m1)):
                if m1[i] != m2[i]:
                    return False

            return True

        left = 0
        right = left + len(s1) - 1

        while left <= right and right < len(s2):
            if check_match(map_s1, map_s2):
                return True

            else:
                if right + 1 < len(s2):
                    old_char_idx = ord(s2[left]) - ord('a')
                    new_char_idx = ord(s2[right+1]) - ord('a')
                    map_s2[old_char_idx] -= 1
                    map_s2[new_char_idx] += 1

                left += 1
                right += 1

        return False






s1 = "ab"
s2 = "eidbaooo"

s3 = "ab"
s4 = "eidboaoo"

s5 = 'adc'
s6 = 'dcda'

s7 = "trinitrophenylmethylnitramine"
s8 = "dinitrophenylhydrazinetrinitrophenylmethylnitramine"

# print(check_inclusion(s1, s2))
# print(check_inclusion(s3, s4))
# print(check_inclusion(s5, s6))
print(check_inclusion(s7, s8))
# print(checkInclusion(s7, s8))
