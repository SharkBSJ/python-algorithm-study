from typing import List

# LeetCode / 167. Two Sum II - Input Array Is Sorted

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

    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(len(numbers)):
            result = self.binary_search(0, len(numbers), numbers, target - numbers[i])
            if result != - 1 and result != i:
                return [min(i + 1, result + 1), max(i + 1, result + 1)]

        return None

numbers = [-1,0]
target = -1
print(Solution().twoSum(numbers, target))