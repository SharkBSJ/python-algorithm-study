from typing import List

#LeetCode / 704. Binary Search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        self.nums = nums

        def binary_search(left: int, right: int, target: int) -> int:
            if left > right:
                return -1
            
            mid = (left + right) // 2
            if self.nums[mid] == target:
                return mid
            elif self.nums[mid] > target:
                return binary_search(left, mid - 1, target)
            else:
                return binary_search(mid + 1, right, target)
        
        return binary_search(0, len(nums) - 1, target)

nums = [-1,0,3,5,9,12]
target = 9
print(Solution().search(nums, target))