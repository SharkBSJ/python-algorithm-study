from typing import List
import re

# LeetCode / 819. Most Common Word
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        #pattern = r"[ |,]"
        temp_list = re.split(r"[ |,]", paragraph)
        temp_dict = {}
        max_num = 0
        max_word = ''
        banned = [e.lower() for e in banned]
        
        for temp in temp_list:
            temp = temp.lower()
            temp = ''.join(e for e in temp if e.isalnum())
            if (temp in banned or not temp.isalpha() or len(temp) == 0):
                continue
            elif (temp in temp_dict):
                temp_dict[temp] += 1
            else:
                temp_dict[temp] = 1
            if (temp_dict[temp] > max_num):
                max_num = temp_dict[temp]
                max_word = temp
        return max_word

paragraph = "Bob. hIt, baLl"
banned = ["bob", "hit"]
print(Solution().mostCommonWord(paragraph, banned))