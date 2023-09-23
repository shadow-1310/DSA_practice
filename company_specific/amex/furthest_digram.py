def find_distance(s):
    max_dist = -1
    hashmap = {}

    for i in range(len(s)-1):
        first = ord(s[i]) - ord('a')
        second = ord(s[i+1]) - ord('a')
        digram = (first, second)

        if digram in hashmap:
            hashmap[digram].append(i)
            dist = hashmap[digram][-1] - hashmap[digram][0]
            max_dist = max(max_dist, dist)

        else:
            hashmap[digram] = [i]

    return max_dist

s1 = 'aaa'
s2 = 'codility'
s3 = 'abbyuidhefebbefjbbdwchvj'
print(find_distance(s1))
print(find_distance(s2))
print(find_distance(s3))
