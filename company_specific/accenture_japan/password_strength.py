class Solution:
    def check_strength(self, s):
        cond1 = False
        cond2 = False
        cond3 = False
        cond4 = False
        cond5 = False
        count = 0
        special = {
                '!',
                '@',
                '#',
                '$',
                '%',
                '^',
                '&',
                '*',
                '(',
                ')',
                '+',
                '-',
                 }
        for char in s:
            if char.islower():
                cond1 = True
            if char.isupper():
                cond2 = True

            if char in special:
                cond3 = True

            if char.isnumeric():
                cond5 = True

            count += 1

        if count >= 8:
            cond4 = True

        if cond1 and cond2 and cond3 and cond4 and cond5:
            return "Strong"
        if cond1 and cond2 and cond3 and count >= 6:
            return "Moderate"

        return "Weak"

s = Solution()
pass1 = "GeeksforGeeks@12"
pass2 = "gfg!@12"

print(s.check_strength(pass1))
print(s.check_strength(pass2))

