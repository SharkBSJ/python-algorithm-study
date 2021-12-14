from typing import List

#LeetCode / 973. K Closest Points to Origin
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key= lambda x: x[0]*x[0] + x[1]*x[1])
        return points[0:k]
        
points = [[3,3],[5,-1],[-2,4]]
k = 2
print(Solution().kClosest(points, k))