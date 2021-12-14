from typing import List

# LeetCode / 134. Gas Station

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start_idx = 0
        end_idx = 0
        original_n = len(gas)
        gas.extend(gas[0:len(gas) - 1])
        cost.extend(cost[0:len(cost) - 1])
        temp_sum = 0
        while start_idx < len(gas) and end_idx < len(gas):
            if temp_sum >= 0 or start_idx >= end_idx:
                temp_sum += gas[end_idx] - cost[end_idx]
                end_idx += 1
            else:
                temp_sum -= gas[start_idx] - cost[start_idx]
                start_idx += 1
            
            if end_idx - start_idx == original_n and temp_sum >= 0:
                return start_idx

        return -1
        
        
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(Solution().canCompleteCircuit(gas, cost))