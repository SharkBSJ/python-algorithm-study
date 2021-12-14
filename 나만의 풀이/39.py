from typing import List
import sys

# LeetCode / 207. Course Schedule
class Solution:
    def dfs(self, idx):
        self.chk[idx] = True

        while self.adj_list[idx]:
            dest = self.adj_list[idx].pop()

            if self.chk[dest] == False:
                self.dfs(dest)

        self.route.append(idx)

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.n = numCourses
        self.adj_list = []
        self.adj_matrix = [[False] * self.n for _ in range(self.n)]
        
        for i in range(self.n):
            self.adj_list.append([])
        for temp in prerequisites:
            self.adj_list[temp[0]].append(temp[1])
            self.adj_matrix[temp[0]][temp[1]] = True
        self.chk = [False] * self.n
  
        routes = []
        for idx in range(self.n):
            if self.chk[idx] == False:
                self.route = []
                self.dfs(idx)
                routes.extend(self.route)
        routes.reverse()

        # print(routes)
        for i in range(len(routes) - 1):
            for j in range(i, len(routes)):
                if self.adj_matrix[routes[j]][routes[i]] == True:
                    return False

        return True
        

numCourses = 2
prerequisites = [[0, 1]]
print(Solution().canFinish(numCourses, prerequisites))

# 1 <= candidates.length <= 30
# 1 <= candidates[i] <= 200
# All elements of candidates are distinct.
# 1 <= target <= 500