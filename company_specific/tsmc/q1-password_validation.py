#this question was asked in TSMC OA in IIT Delhi
class Solution:
    def sub_in_dict(self, string, common_words):
        n1 = len(string)
        for word in common_words:
            # print('-'*26)
            # print(word)
            # print('-'*26)
            n2 = len(word)
            if n1 < n2:
                continue
            for i in range(n1-n2+1):
                # print(string[i:i+n2])
                if string[i:i+n2] == word:
                    return True

        return False

        
    def getPasswordStrength(self, passwords, common_words):
        self.dict = set(common_words)
        res = []
        for pw in passwords:
            verdict = self.validate_pass(pw, common_words)
            res.append(verdict)
            # break

        return res


    def validate_pass(self, password, common_words):
        if (
            len(password) < 6 or 
            (password in self.dict) or
            self.sub_in_dict(password, common_words) or
            password.isnumeric() or 
            password.isupper() or 
            password.islower()
            ):
            return 'weak'

        else:
            return 'strong'


s = Solution()
passwords = ['iliketoCoDe', 'teaMAKEsmehappy', 'abracaDabra', 'pasSword', 'blackcoffeeISthebest']
# passwords = ['blackcoffeeISthebest']
common_words = ['coffee', 'coding', 'happy']
print(s.getPasswordStrength(passwords, common_words))
passwords = ['hello', 'chargeR', 'pass123']
common_words = ['hello', '123', 'password', 'xyz', '999']
print(s.getPasswordStrength(passwords, common_words))
