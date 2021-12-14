from typing import List
from functools import cmp_to_key

#LeetCode / 179. Largest Number

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x: int, y: int):
            x_str = str(x)
            y_str = str(y)
            str_1 = x_str + y_str
            str_2 = y_str + x_str
            if str_1 > str_2:
                return -1
            elif str_1 < str_2:
                return 1
            else:
                return 0
        
        if sum(nums) == 0:
            return '0'

        result = ''
        nums = sorted(nums, key = cmp_to_key(compare))
        for num in nums:
            result += str(num)
        return result

# nums = [3,30,34,5,9]
# nums = [34323,3432]
# nums = [432,43243]
nums = [0, 0]
print(Solution().largestNumber(nums))