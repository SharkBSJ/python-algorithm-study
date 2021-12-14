from typing import List

#LeetCode / 56. Merge Intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
            
        intervals.sort()
        result = [[intervals[0][0], intervals[0][1]]]
        for [idx_1, idx_2] in intervals:
            last_idx_2 = result[-1][1]
            if idx_1 <= last_idx_2 and idx_2 > last_idx_2:
                result[-1][1] = idx_2
            elif idx_1 > last_idx_2:
                result.append([idx_1, idx_2])

        return result


intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output : [[1,6],[8,10],[15,18]]
print(Solution().merge(intervals))