from typing import List

# LeetCode / 393. UTF-8 Validation

MAX_BIT = 128
START_BIT = 128
START_2_BIT = 64
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        idx = 0
        while idx < len(data):
            front = data[idx]
            idx += 1

            # Get 1 Bit Number
            num = 0
            prefix_bit = MAX_BIT
            while front & prefix_bit:
                prefix_bit = prefix_bit >> 1
                num += 1
            
            if num == 1:
                return False
            if num > 4:
                return False
            
            # Pop it
            while num > 1:
                if idx == len(data) or START_BIT & data[idx] == 0 or START_2_BIT & data[idx]:
                    return False
                num -= 1
                idx += 1
            
        return True

data = [250,145,145,145,145]
print(bin(250))
print(bin(145))
print(Solution().validUtf8(data))