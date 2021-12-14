from typing import List

# LeetCode / 937. Reorder Log Files
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs: List[str] = []
        digit_logs: List[str] = []

        for temp in logs:
            temp_list = temp.split()
            if temp_list[1][0].isnumeric():
                digit_logs.append(temp)
            else:
                letter_logs.append(temp_list)
        letter_logs.sort(key= lambda x: (x[1:], x[0]))
        result: List[str] = []
        for temp in letter_logs:
            temp_str: str = ' '.join(temp)
            result.append(temp_str)
        result = result + digit_logs
        return result

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(Solution().reorderLogFiles(logs))