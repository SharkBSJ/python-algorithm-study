from typing import List

# LeetCode / 238. Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product: int = 1
        result: List[int] = []
        zero_count = 0
            
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                total_product *= num
        for num in nums:
            if zero_count > 0:
                if num != 0:
                    result.append(0)
                elif zero_count >= 2:
                    result.append(0)
                else:
                    result.append(total_product)
            else:
                result.append(int(total_product / num))
        
        return result

nums = [-1,1,0,-3,3]
print(Solution().productExceptSelf(nums))