from typing import List

# LeetCode / 49. Group Anagrams
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = {}
        for temp in strs:
            temp_sorted = ''.join(sorted(temp))
            if temp_sorted in result_dict:
                result_dict[temp_sorted].append(temp)
            else:
                result_dict[temp_sorted] = []
                result_dict[temp_sorted].append(temp)

        result = []
        for i in result_dict:
            result.append(result_dict[i])
        
        return result

strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs))

    