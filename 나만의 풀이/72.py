from typing import List

# LeetCode / 371. Sum of Two Integers

MAX_MASK = 0b11111111111
MAX_BIT_MASK = 0b10000000000
class Solution:
    def getSum(self, x: int, y: int) -> int:
        x = x & MAX_MASK
        y = y & MAX_MASK
        
        result = x ^ y
        carry = x & y

        while carry != 0:
            prev_result = result
            result = result ^ (carry << 1)
            carry = prev_result & (carry << 1)

        result &= MAX_MASK
        
        if MAX_BIT_MASK & result:
            result &= MAX_MASK
            result = ~(result ^ MAX_MASK)
            
        return result 

x = 5
y = -15
print(Solution().getSum(x, y))