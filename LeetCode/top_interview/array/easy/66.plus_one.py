def plus_one(digits):
    s = [str(x) for x in digits]
    string_num = "".join(s)
    num = int(string_num)
    plus_one_num = num + 1
    plus_one_list = [int(x) for x in str(plus_one_num)]
    
    return plus_one_list

input_s = [9]
print(plus_one(input_s))