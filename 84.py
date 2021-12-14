import re
from typing import List

#LeetCode / 241. Different Ways to Add Parentheses

class Solution:
    def divide_and_conquer(self, left: int, right: int) -> set:
        result = []
        if left == right:
            result.append(self.nums[left])
            return result
        
        for i in range(left, right, 1):
            left_result = self.divide_and_conquer(left, i)
            right_result = self.divide_and_conquer(i + 1, right)
            for left_num in left_result:
                for right_num in right_result:
                    if self.cals[i] == '+':
                        result.append(left_num + right_num)
                    elif self.cals[i] == '*':
                        result.append(left_num * right_num)
                    else:
                        result.append(left_num - right_num)

        return result

    def diffWaysToCompute(self, expression: str) -> List[int]:
        nums = re.findall('[0-9]+', expression)
        self.nums = [int(num) for num in nums]
        self.cals = re.findall('[+*-]', expression)
        return self.divide_and_conquer(0, len(nums) - 1)

expression = "2*3-4*5"
print(Solution().diffWaysToCompute(expression))