def rom_to_int(s:str):
    arabic_int = 0
    rom_int_map = {'I':1, 'V':5, 'X': 10, 'L':50, 'C':100, 'D':500, 'M':1000}
    ind = 0
    last_char = s[-1]
    for char in s[::-1]:
        if char == 'I' and (last_char == 'V' or last_char == 'X') and ind != 0:
            arabic_int -= rom_int_map[char]
        elif char == 'X' and (last_char == 'L' or last_char == 'C') and ind != 0:
            arabic_int -= rom_int_map[char]
        elif char == 'C' and (last_char == 'D' or last_char == 'M' and ind != 0):
            arabic_int -= rom_int_map[char]
        else:
            arabic_int += rom_int_map[char]
        ind += 1
        last_char = char

    return arabic_int

rom = 'MCMXCIV'
print(rom_to_int(rom))