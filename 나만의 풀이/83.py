from typing import List

#LeetCode / 241. Different Ways to Add Parentheses

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_num = nums[0]
        max_count = 1

        for i in range(1, len(nums)):
            if max_num != nums[i]:
                max_count -= 1
            else:
                max_count += 1

            if max_count == 0:
                max_num = nums[i]
                max_count = 1
        
        return max_num

nums = [2,2,1,1,1,2,2]
print(Solution().majorityElement(nums))
