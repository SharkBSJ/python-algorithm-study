from typing import List
import heapq

# LeetCode / 787. Cheapest Flights Within K Stops
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = [[] for _ in range(n)]
        for u, v, w in flights:
            adj_list[u].append((w, v))
        
        heap = []
        dist = [-1] * n
        dist_k = [-1] * n
        heapq.heappush(heap, (0, src, 0))
        while heap:
            temp_cost, temp_dst, temp_k = heapq.heappop(heap)
            if dist[temp_dst] == -1:
                dist[temp_dst] = temp_cost
            if dist_k[temp_dst] == -1 or dist_k[temp_dst] > temp_k:
                dist_k[temp_dst] = temp_k
            if dist[temp_dst] < temp_cost and dist_k[temp_dst] < temp_k:
                continue

            if temp_k <= k:
                for input_cost, input_dst in adj_list[temp_dst]:
                #while adj_list[temp_dst]:
                #    input_cost, input_dst = adj_list[temp_dst].pop()
                #    if temp_k != k or input_dst == dst:
                    heapq.heappush(heap, (temp_cost + input_cost, input_dst, temp_k + 1))

        return dist[dst]

n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 0
print(Solution().findCheapestPrice(n, flights, src, dst, k))