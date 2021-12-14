from typing import List

# LeetCode / 42. Trapping Rain Water
class Solution:
    def trap(self, height: List[int]) -> int:
        left_height: List[int] = [0] * len(height) # Initialization
        # right_height: List[int] = []
        
        left_sum = 0
        left_max = 0
        for idx in range(len(height)):
            if left_max < height[idx]:
                left_max = height[idx]
            left_height[idx] = left_max
            left_sum += left_height[idx] - height[idx]
        #print(f'Left SUM : {left_sum}')
        
        right_sum = 0
        right_max = 0
        for idx in range(len(height)-1, -1, -1):
            if right_max < height[idx]:
                right_max = height[idx]
            if right_max == left_max:
                break
            right_sum += left_height[idx] - right_max
        #print(f'Right SUM : {right_sum}')
        
        return left_sum - right_sum

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trap(height))