from typing import List
import heapq

#LeetCode / 215. Kth Largest Element in an Array

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [temp * -1 for temp in nums]
        heapq.heapify(nums)
        result = 0
        for _ in range(k):
            result = heapq.heappop(nums)
        
        return result * -1

nums = [3,2,1,5,6,4]
k = 2
# Output = 5
print(Solution().findKthLargest(nums, k))