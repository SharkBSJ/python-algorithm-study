from typing import List
from collections import defaultdict

#LeetCode / 198. House Robber

NOT_DEFINED = -1
class Solution:
    def __init__(self):
        self.result = defaultdict(lambda: NOT_DEFINED)

    def rob(self, nums: List[int]) -> int:
        def memoization(nums: List[int], n: int) -> int:
            if n < 0:
                return 0
            elif n == 0:
                return nums[0]

            if self.result[n] != NOT_DEFINED:
                return self.result[n]

            self.result[n] = max(memoization(nums, n - 1), memoization(nums, n - 2) + nums[n])

            return self.result[n]
        
        return memoization(nums, len(nums) - 1)

nums = [2,7,9,3,1]
print(Solution().rob(nums))