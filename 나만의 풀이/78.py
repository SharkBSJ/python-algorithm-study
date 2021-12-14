from typing import List
import sys

# LeetCode / 122. Best Time to Buy and Sell Stock II

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = sys.maxsize
        result = 0
        for i in range(len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            
            if (i + 1 == len(prices) or prices[i + 1] < prices[i]):
                result += prices[i] - min_price
                min_price = sys.maxsize
        
        return result
 
prices = [7,6,4,3,1]
print(Solution().maxProfit(prices))