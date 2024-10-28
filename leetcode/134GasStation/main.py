
class Solution:
    # def canCompleteCircuit(self, gas, cost) -> int:
    #     for i in range(len(gas)):
    #         tank = gas[i]
    #         j = i
    #         while True:
    #             if tank - cost[j] < 0: 
    #                 break
    #             tank += gas[j+1 if j+1 < len(gas) else 0] - cost[j]
    #             j = j+1 if j+1 < len(gas) else 0
    #             if j == i:
    #                 return i
    #     return -1

    def canCompleteCircuit(self, gas, cost) -> int:
        total_tank, curr_tank = 0, 0
        starting_station = 0
        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            if curr_tank < 0:
                starting_station = i + 1
                curr_tank = 0
        return starting_station if total_tank >= 0 else -1
    


s = Solution()
print(s.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])) # 3
print(s.canCompleteCircuit([2,3,4], [3,4,3])) # -1
print(s.canCompleteCircuit([5,1,2,3,4], [4,4,1,5,1])) # 4
print(s.canCompleteCircuit([3,1,1], [1,2,2])) # 0

        