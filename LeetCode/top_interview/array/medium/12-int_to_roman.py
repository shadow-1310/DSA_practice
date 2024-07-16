# I tried this approach, but now working for all numbers as 1900 should be MCM not MDCD
class Solution:
    def intToRoman(self, num):
        res = []
        mapping = {
                1 : 'I',
                5 : 'V',
                10 : 'X',
                50 : 'L',
                100 : 'C',
                500 : 'D',
                1000 : 'M',
                }

        romans = [1000, 500, 100, 50, 10, 5, 1]
        for i, rom in enumerate(romans):
            mul = num // rom
            if mul == 0:
                continue
            else:
                if rom in (100, 10, 1) and (mul == 4 or mul == 9):
                    res.append(mapping[rom]+mapping[romans[i-1]])
                else:
                    res.append(mapping[rom]*mul)
                num = num % rom

        return "".join(res)

num = 1490
num = 1494
num = 1997
s = Solution()
print(s.intToRoman(num))


