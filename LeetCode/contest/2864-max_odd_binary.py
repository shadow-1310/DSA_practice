#contest problem on LC
#done on 2023-09-30
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count_map = {}
        for dig in s:
            if dig in count_map:
                count_map[dig] += 1
            else:
                count_map[dig] = 1
                
        res = ''
        for i in range(count_map['1']-1):
            res += '1'
        
        if '0' in count_map:
            for i in range(count_map['0']):
                res += '0'
            
        return res + '1'
