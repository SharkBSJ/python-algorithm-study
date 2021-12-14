from typing import List
from collections import Counter

# LeetCode / 347. Top K Frequent Elements
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_dict = Counter(nums)
        counter_dict = sorted(counter_dict.items(), key = lambda item: item[1], reverse = True)

        temp = list(counter_dict)
        result: List[int] = []
        for idx in range(k):
            result.append(temp[idx][0])

        return result

nums = [1,1,1,2,2,3]
k = 2
print(Solution().topKFrequent(nums, k))