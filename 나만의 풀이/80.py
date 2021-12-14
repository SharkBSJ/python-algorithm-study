from typing import List
from collections import Counter
from collections import defaultdict
import sys

# LeetCode / 621. Task Scheduler

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count_dict = Counter(tasks)
        last_num = defaultdict(lambda : -sys.maxsize)
        
        result = 0
        for _ in range(len(tasks)):
            # Check Exist
            min_last_num = sys.maxsize
            for key in count_dict:
                if count_dict[key] > 0 and last_num[key] < min_last_num:
                    min_last_num = last_num[key]
            
            result += 1
            # Add Idel Time
            if min_last_num + n + 1 > result:
                result = min_last_num + n + 1

            # Choice Maximum Frequent Key
            max_key = -1
            max_num = -sys.maxsize
            for key in count_dict:
                if count_dict[key] > 0 and max_num < count_dict[key] and last_num[key] + n + 1 <= result:
                    max_key = key
                    max_num = count_dict[key]
            
            count_dict[max_key] -= 1
            last_num[max_key] = result

        return result
        
tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
print(Solution().leastInterval(tasks, n))