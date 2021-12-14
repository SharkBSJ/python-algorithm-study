from typing import List

# LeetCode / 15. 3Sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        result_dict = {}
        nums_dict = {}
        nums.sort()
        
        for i in range(len(nums)):
            if nums[i] in nums_dict:
                nums_dict[nums[i]] += 1
            else:
                nums_dict[nums[i]] = 1

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                tempSum = (nums[i] + nums[j]) * -1
                if tempSum in nums_dict:
                    count = 1
                    if tempSum == nums[i]:
                        count += 1
                    if tempSum == nums[j]:
                        count += 1
                    if nums_dict[tempSum] < count:
                        continue
                        
                    temp = [nums[i], nums[j], tempSum]
                    temp.sort()
                    if not tuple(temp) in result_dict:
                        result_dict[tuple(temp)] = True
                        result.append(temp)

        return result

nums = [0,0,0]
print(Solution().threeSum(nums))