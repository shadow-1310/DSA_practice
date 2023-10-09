#this was wasked in accenture japan OA, done on 07-10-2023
class Solution:
    def viz_of_ivy(self, a, n):
        first = 0
        last = max(a) + 3
        for i in range(last):
            if i == first or i == last-1:
                line = '+'
                for j in range(2*n+1):
                    line += '-'
                print(line)

            else:
                line = '|'
                for j in range(2*n+1):
                    if (j & 1) == 0:
                        line += '.'
                    elif i < a[j>>1]:
                        line += 'X'
                    elif i == a[j>>1]:
                        line += 'V'
                    else:
                        line += '.'
                print(line)

if __name__ == '__main__':
    n = int(input())
    a = map(int, input().split(' '))
    s = Solution()
    s.viz_of_ivy(a, n )

    # s = Solution()
    # s.viz_of_ivy([5,6,9,10],4)
    # s.viz_of_ivy([3,1,5],3)

