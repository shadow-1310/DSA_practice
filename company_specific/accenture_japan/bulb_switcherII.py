def find_states(n, p):
    if n == 1:
        return 2
    if n == 2:
        return 2 if p == 3 else 4
    if n >= 3:
        if p == 1:
            return 4
        if p == 2:
            return 7
        else:
            return 8


print(find_states(4,2))
        
