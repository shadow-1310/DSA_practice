def build_suffix_array(s):
    suffixes = sorted((s[i:], i) for i in range(len(s)))
    suffix_array = [suffix[1] for suffix in suffixes]
    return suffix_array

def build_lcp_array(s, suffix_array):
    n = len(s)
    rank = [0] * n
    lcp = [0] * n
    
    for i, suffix in enumerate(suffix_array):
        rank[suffix] = i
        
    h = 0
    for i in range(n):
        if rank[i] > 0:
            j = suffix_array[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[rank[i]] = h
            if h > 0:
                h -= 1
    
    return lcp

def find_lcs(strings):
    delimiter = chr(1)  # Using a delimiter character that is not in the original strings
    combined_string = delimiter.join(strings) + delimiter
    suffix_array = build_suffix_array(combined_string)
    lcp_array = build_lcp_array(combined_string, suffix_array)
    
    max_len = 0
    start_index = 0
    str_id = [-1] * len(combined_string)
    current_str = 0
    for i in range(len(combined_string)):
        if combined_string[i] == delimiter:
            current_str += 1
        else:
            str_id[i] = current_str
    
    n = len(strings)
    for i in range(1, len(combined_string)):
        a = suffix_array[i - 1]
        b = suffix_array[i]
        if str_id[a] != str_id[b] and lcp_array[i] > max_len:
            unique_strings = set()
            j = i
            while j > 0 and lcp_array[j] >= lcp_array[i]:
                unique_strings.add(str_id[suffix_array[j - 1]])
                unique_strings.add(str_id[suffix_array[j]])
                j -= 1
            if len(unique_strings) == n:
                max_len = lcp_array[i]
                start_index = suffix_array[i]
    
    return combined_string[start_index:start_index + max_len]

def read_seq(path):
    file = open(path, 'r')
    output = []
    curr_str = []
    for line in file:
        if line[0] != '>':
            curr_str.append(line.strip())
        else:
            output.append("".join(curr_str))
            curr_str = []

    file.close()
    print(output)
    curr_max = 0
    for str in output:
        curr_max = max(curr_max, len(str))
    print(curr_max)
    return output


if __name__ == "__main__":
    file_path = "rosalind_lcsm.txt"
    strings = read_seq(file_path)
    print(len(strings))
    # print(find_lcs(strings))
