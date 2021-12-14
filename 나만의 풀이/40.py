from typing import List
import heapq

# LeetCode / 743. Network Delay Time
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = [[] for _ in range(n)]
        for temp in times:
            start = temp[0] - 1
            dest = temp[1] - 1
            cost = temp[2]
            adj_list[start].append((cost, dest))

        heap = []
        heapq.heappush(heap, (0, k - 1))
        chk = [False] * n
        max_cost = 0
        while heap:
            temp = heapq.heappop(heap)
            cost = temp[0]
            start = temp[1]
            if chk[start] == True:
                continue
            chk[start] = True
            max_cost = cost

            while adj_list[start]:
                temp = adj_list[start].pop()
                temp_cost = temp[0]
                temp_dest = temp[1]
                heapq.heappush(heap, (cost + temp_cost, temp_dest))

        # print(chk)
        for temp in chk:
            if temp == False:
                return -1
        
        return max_cost
        
        

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
print(Solution().networkDelayTime(times, n, k))