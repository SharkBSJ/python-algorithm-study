from typing import List

# LeetCode / 191. Number of 1 Bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

n = int(0b00000000000000000000000000001011)
#print(n)
# n = -3
print(Solution().hammingWeight(n))