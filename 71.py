from typing import List

# LeetCode / 461. Hamming Distance

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        reuslt = x ^ y
        return bin(reuslt).count('1')

x = 3
y = 1
print(Solution().hammingDistance(x, y))