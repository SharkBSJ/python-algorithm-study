from typing import List
from collections import defaultdict
import sys

#LeetCode / 53. Maximum Subarray

NOT_DEFINED = -sys.maxsize
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = defaultdict(lambda: NOT_DEFINED)
        result_continue = defaultdict(lambda: NOT_DEFINED)

        def memoization(nums: List[int], n: int, is_continuous: bool) -> int:
            if n == 0:
                return nums[0]
            
            if is_continuous:
                if result_continue[n] != NOT_DEFINED:
                    return result_continue[n]
                result_continue[n] = max(0, memoization(nums, n - 1, True)) + nums[n]
                return result_continue[n]
            else:
                if result[n] != NOT_DEFINED:
                    return result[n]
                result[n] = max(memoization(nums, n - 1, False), max(0, memoization(nums, n - 1, True)) + nums[n])
                return result[n]
        
        return memoization(nums, len(nums) - 1, False)

nums = [-1,1,2,1]
print(Solution().maxSubArray(nums))