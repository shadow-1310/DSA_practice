class Solution:
    def matchPlayersAndTrainers(self, players, trainers):
        players.sort()
        trainers.sort()
        count = 0
        n = len(trainers)
        def get_match(start, target):
            if start >= n:
                return n
            l = start
            r = n-1
            while l <= r:
                mid = (l+r) >> 1
                if target < trainers[mid]:
                    r = mid - 1
                elif target > trainers[mid]:
                    l = mid + 1
                #here even if we get a match, we have to find the leftmost allowed match
                else:
                    r = mid-1
            return l 

        curr = 0
        i = 0
        while i < len(players):
            next_pos = get_match(curr, players[i]) 
            if next_pos >= n:
                return count
            else:
                i += 1
                count += 1
                curr = next_pos + 1

        return count


s = Solution()
players = [4,7,9]
trainers = [8,2,5,8]
# players = [1,1,1]
# trainers = [10]
# players = [1]
# trainers = [1]
players = [3,2,3,2,4,3,1,4,1,4,3,2,2,1,3,3,3,1,2,4,1,1,2,4,2]
trainers = [3,4,1,4,4,3,2,4,3,3,1,4,1,2,3,4,1,3,4,4,1,2,3,4,3]
print(s.matchPlayersAndTrainers(players, trainers))
