from typing import List
import sys

# LeetCode / 406. Queue Reconstruction by Height

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        result = []
        minus_num = [0] * len(people)

        for _ in range(len(people)):
            min_num = sys.maxsize
            min_idx = -1
            for i in range(len(people)):
                if people[i][1] - minus_num[i] == 0 and min_num > people[i][0]:
                    min_num = people[i][0]
                    min_idx = i
            
            result.append(people[min_idx])

            for i in range(len(people)):
                if people[i][0] <= min_num:
                    minus_num[i] += 1

        return result

people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
print(Solution().reconstructQueue(people))