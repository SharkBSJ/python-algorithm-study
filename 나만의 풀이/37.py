from typing import List

# LeetCode / 39. Combination Sum
class Solution:
    def dfs(self, idx):
        if idx == len(self.nums):
            self.result.append(self.elements[:])
            return 
        
        self.dfs(idx+1)
        self.elements.append(self.nums[idx])
        self.dfs(idx+1)
        self.elements.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.elements = []
        self.nums = nums
        self.dfs(0)
        return self.result
        

nums = [1,2,3]
print(Solution().subsets(nums))

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.