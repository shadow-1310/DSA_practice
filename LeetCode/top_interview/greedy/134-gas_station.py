#done on 2023-09-23
#in this approach we loop the whole array cyclewise, for each element, although it is working for top 33 testcases on LC
#it is failing on the 34th one
class Solution:
    def canCompleteCircuit(self, gas, cost):
        diff = []
        sum_gas = 0
        sum_cost = 0

        for i in range(len(gas)):
            sum_gas += gas[i]
            sum_cost += cost[i]
            diff.append(gas[i] - cost[i])

        n = len(diff)
        if sum_gas < sum_cost:
            return -1

        for i in range(n):
            total = 0
            start = i
            curr = i
            dist = 0
            while curr < n and dist <= n:
                if dist == n -1:
                    return start
                total += diff[curr]
                if total < 0:
                    break
                if curr == n - 1:
                    curr = 0
                else:
                    curr += 1

                dist += 1

        return -1


#in this solution for each element, we only iterate to the end
class Solution:
    def canCompleteCircuit(self, gas, cost):
        diff = []
        sum_gas = 0
        sum_cost = 0

        for i in range(len(gas)):
            sum_gas += gas[i]
            sum_cost += cost[i]
            diff.append(gas[i] - cost[i])

        n = len(diff)
        if sum_gas < sum_cost:
            return -1

        for i in range(n):
            start = i
            total = 0
            curr = i
            while curr < n:
                total += diff[curr]

                if total < 0:
                    break
                if curr == n-1:
                    return start
                curr += 1

        return -1



#this solution is working well on all 40 testcases of LC
#done on 2023-09-23
class Solution:
    def canCompleteCircuit(self, gas, cost):
        sum_gas = 0
        sum_cost = 0
        n = len(gas)

        for i in range(n):
            sum_gas += gas[i]
            sum_cost += cost[i]

        if sum_gas < sum_cost:
            return -1

        total = 0
        start = 0
        for i in range(n):
           total += gas[i] - cost[i]

           if total < 0:
               total = 0
               start = i+1

        return start
