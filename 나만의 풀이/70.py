from typing import List

# LeetCode / 136. Single Number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result

nums = [1]
print(Solution().singleNumber(nums))