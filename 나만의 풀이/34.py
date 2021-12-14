from typing import List

# LeetCode / 46. Permutations
class Solution:
    def dfs(self, idx: int):
        if idx == len(self.nums):
            self.results.append(self.result[:])
            return 

        for i in range(len(self.nums)):
            if self.chk[i] == False:
                self.chk[i] = True
                self.result.append(self.nums[i])
                self.dfs(idx + 1)
                self.chk[i] = False
                self.result.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.chk = [False] * len(nums)
        self.result = []
        self.results = []
        self.dfs(0)

        return self.results

nums = [1,2,3]
print(Solution().permute(nums))