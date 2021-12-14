from typing import List
import heapq

# LeetCode / 239. Sliding Window Maximum

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        start_idx = 0
        reuslt_size = len(nums) - k + 1
        result = [-10000000] * reuslt_size
        pivot = 0
        for idx in range(k):
            heapq.heappush(heap, (-nums[idx], idx))
            if nums[pivot] <= nums[idx]:
                    pivot = idx
        temp_pivot = pivot + 1
                    
        while start_idx < reuslt_size:
            result[start_idx] = nums[pivot]
            start_idx += 1
            
            if start_idx + k - 1 < len(nums):
                heapq.heappush(heap, (-nums[start_idx + k - 1], start_idx + k - 1))
                
            if pivot < start_idx:
                while heap:
                    temp_pivot = heapq.heappop(heap)[1]
                    if temp_pivot >= start_idx:
                        pivot = temp_pivot
                        break
            elif start_idx + k - 1 < len(nums) and nums[start_idx + k - 1] >= nums[pivot]:
                pivot = start_idx + k - 1
            
        return result

nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(Solution().maxSlidingWindow(nums, k))