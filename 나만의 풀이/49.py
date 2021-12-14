from typing import List

# Leet Code / 310. Minimum Height Trees

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        self.result: List[int] = []
        self.adj_list = [[] for _ in range(n)]
        self.input_num = [0] * n
        for edge in edges:
            self.adj_list[edge[0]].append(edge[1])
            self.adj_list[edge[1]].append(edge[0])
            self.input_num[edge[0]] += 1
            self.input_num[edge[1]] += 1
        init_leafs = []
        count = n
        for i in range(n):
            if self.input_num[i] == 1:
                init_leafs.append(i)
        self.result = init_leafs
        if not self.result:
            self.result = [0]
        while count > 2:
            next_leafs = []
            while init_leafs:
                src = init_leafs.pop()
                count -= 1
                for dest in self.adj_list[src]:
                    self.input_num[dest] -= 1
                    if self.input_num[dest] == 1:
                        next_leafs.append(dest)
            init_leafs = next_leafs
            self.result = next_leafs


        return self.result

n = 4
edges = [[1,0],[1,2],[1,3]]
print(Solution().findMinHeightTrees(n, edges))