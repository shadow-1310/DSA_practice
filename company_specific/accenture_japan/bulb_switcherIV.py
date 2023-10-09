def get_target(target):
    res = 0
    future = 0
    for char in target:
        if str(future) != char:
            res += 1
            future = 0 if future else 1

    return res

print(get_target('0100'))

