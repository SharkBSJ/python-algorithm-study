from collections import defaultdict

# LeetCode / 424. Longest Repeating Character Replacement

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s_dict = defaultdict(int)
        result = k
        max_size = k
        idx = 0
        for i in range(0, k):
            s_dict[s[i]] += 1
            
        while idx + max_size < len(s):
            # Check
            temp_max = 0
            for key in s_dict:
                if temp_max < s_dict[key]:
                    temp_max = s_dict[key]

            # Move Window
            if temp_max + k >= max_size:
                if max_size > result:
                    result = max_size
                s_dict[s[idx + max_size]] += 1
                max_size += 1
            else:
                s_dict[s[idx]] -= 1
                s_dict[s[idx + max_size]] += 1
                idx += 1

        temp_max = 0
        for key in s_dict:
            if temp_max < s_dict[key]:
                temp_max = s_dict[key]
        if temp_max + k >= max_size and max_size > result:
            result = max_size

        return result

s = "ABAA"
k = 0
print(Solution().characterReplacement(s, k))