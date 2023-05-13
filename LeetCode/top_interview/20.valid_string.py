# def is_valid(s):
#     prev_char = s[0]
#     for char in s[1:]:
#         if prev_char == '(' and char != ')':
#             return False
#         elif prev_char == '{' and char != '}':
#             return False
#         elif prev_char == '[' and char != ']':
#             return False
        
#         prev_char = char
#     return True


def is_valid(s):
    d = {'(' : ')',
         '{': '}',
         '[' : ']'}
    stack =[]

    for char in s:
        if char in d:
            stack.append(char)
        elif len(stack) == 0 or d[stack.pop()] != char:
            return False
    
    if len(stack) == 0:
        return True
    else:
        return False
    
input_string1 = "()[]{}"
input_string2 = "(]"
input_string3 = "{[]}"

print(is_valid(input_string1))
print(is_valid(input_string2))
print(is_valid(input_string3))