from typing import List

#LeetCode / 33. Search in Rotated Sorted Array

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min_idx = 0
        for i in range(len(nums)):
            if nums[min_idx] > nums[i]:
                min_idx = i

        self.nums = [0] * len(nums)
        for i in range(len(nums)):
            self.nums[i] = nums[(i + min_idx) % len(nums)]

        # print(self.nums)

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
        
        result = binary_search(0, len(nums) - 1, target)
        if result == -1:
            return -1
        else:
            return (result + min_idx) % len(nums)

nums = [1]
target = 0
print(Solution().search(nums, target))