from typing import List

# LeetCode / 39. Combination Sum
class Solution:
    def dfs(self, idx, sum):
        if sum > self.target:
            return
        if sum == self.target:
            self.result.append(self.elements[:])
            return
        for i in range(idx, len(self.nums)):
            self.elements.append(self.nums[i])
            self.dfs(i, sum + self.nums[i])
            self.elements.pop()
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.target = target
        self.nums = candidates
        self.elements = []
        self.dfs(0, 0)
        return self.result
        

candidates = [2,3,6,7]
target = 7
print(Solution().combinationSum(candidates, target))

# 1 <= candidates.length <= 30
# 1 <= candidates[i] <= 200
# All elements of candidates are distinct.
# 1 <= target <= 500