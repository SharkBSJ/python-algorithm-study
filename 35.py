from typing import List

# LeetCode / 77. Combinations
class Solution:
    def dfs(self, last_int: int, idx: int):
        if idx == self.k:
            self.results.append(self.result[:])
            return 

        for i in range(last_int, self.n):
            if self.chk[i] == False:
                self.chk[i] = True
                self.result.append(i + 1)
                self.dfs(i + 1, idx + 1)
                self.chk[i] = False
                self.result.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.n = n
        self.k = k
        self.chk = [False] * n
        self.result = []
        self.results = []
        self.dfs(0, 0)

        return self.results

n = 4
k = 2
print(Solution().combine(n, k))