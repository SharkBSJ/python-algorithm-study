from typing import List

# LeetCode / 200. Number of Islands
class Solution:
    def dfs(self, grid: List[List[str]], i, j):
        grid[i][j] = '0'
        if i + 1 < len(grid) and grid[i + 1][j] == '1':
            self.dfs(grid, i + 1, j)
        if j + 1 < len(grid[i]) and grid[i][j + 1] == '1':
            self.dfs(grid, i, j + 1)
        if i - 1 >= 0 and grid[i - 1][j] == '1':
            self.dfs(grid, i - 1, j)
        if j - 1 >= 0 and grid[i][j - 1] == '1':
            self.dfs(grid, i, j - 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        result: int = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    result += 1
                    # print(i, j)

        return result

grid = [["1","1","1"],["0","1","0"],["1","1","1"]]
print(Solution().numIslands(grid))