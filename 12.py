from typing import List

# LeetCode / 121. Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_list: List[int] = []
        max_list: LIst[int] = [0] * len(prices)
        result = 0

        # Get Min List (0 ~ Idx)
        min_list.append(prices[0])
        for idx in range(1, len(prices)):
            if prices[idx] < min_list[idx-1]:
                min_list.append(prices[idx])
            else:
                min_list.append(min_list[idx-1])

        # Get Max List (N-1 ~ Idx+1)
        temp_max = 0
        for idx in range(len(prices)-1, -1, -1):
            if prices[idx] > temp_max:
                temp_max = prices[idx]
            max_list[idx] = temp_max

        # Get Result (Max - Min)
        for idx in range(len(prices)):
            if max_list[idx] - min_list[idx] > result:
                result = max_list[idx] - min_list[idx]

        return result

prices = [7,6,4,3,1]
print(Solution().maxProfit(prices))