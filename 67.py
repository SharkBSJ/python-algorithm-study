from typing import List

# LeetCode / 349. Intersection of Two Arrays

class Solution:
    def binary_search(self, left: int, right: int, nums: List[int], target: int):

        if left > right:
            return -1
        
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            return self.binary_search(mid + 1, right, nums, target)

        elif nums[mid] > target:
            return self.binary_search(left, mid - 1, nums, target)

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        result = []

        for i in range(len(nums2)):
            if i > 0 and nums2[i] == nums2[i-1]:
                continue
            elif self.binary_search(0, len(nums1) - 1, nums1, nums2[i]) != -1:
                result.append(nums2[i])

        return result
    
nums1 = [4,9,5]
nums2 = [9,4,9,8,4] 
print(Solution().intersection(nums1, nums2))