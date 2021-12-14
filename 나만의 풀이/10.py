from typing import List

# LeetCode / 561. Array Partition I
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        result: int = 0
        nums.sort()
        for idx in range(0, len(nums), 2):
            result += nums[idx]
            # print(nums[idx])
        return result

nums = [1,4,3,2]
print(Solution().arrayPairSum(nums))