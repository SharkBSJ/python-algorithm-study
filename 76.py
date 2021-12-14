from collections import defaultdict

# LeetCode / 76. Minimum Window Substring

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = defaultdict(int)
        for char in t:
            t_dict[char] += 1

        s_dict = defaultdict(int)
        same_num = 0
        start = 0
        end = 0
        min_size = 10000000
        result_start_idx, result_end_idx = None, None

        while end < len(s) or (end == len(s) and same_num == len(t)):
            if same_num < len(t) and min_size > end - start:
                if s[end] in t_dict:
                    s_dict[s[end]] += 1
                    t_dict[s[end]] -= 1
                    if t_dict[s[end]] >= 0:
                        same_num += 1
                end += 1
            elif same_num < len(t) and min_size <= end - start:
                if s[end] in t_dict:
                    s_dict[s[end]] += 1
                    t_dict[s[end]] -= 1
                    if t_dict[s[end]] >= 0:
                        same_num += 1
                if s[start] in t_dict:
                    s_dict[s[start]] -= 1
                    t_dict[s[start]] += 1
                    if t_dict[s[start]] > 0:
                        same_num -= 1
                start += 1
                end += 1
            else: # same_num == len(t)
                if min_size > end - start:
                    min_size = end - start
                    result_start_idx = start
                    result_end_idx = end
                if s[start] in t_dict:
                    s_dict[s[start]] -= 1
                    t_dict[s[start]] += 1
                    if t_dict[s[start]] > 0:
                        same_num -= 1
                start += 1
                    
        if result_start_idx is None or result_end_idx is None:
            return ''
        else:
            return s[result_start_idx:result_end_idx]


s = "a"
t = "aa"
print(Solution().minWindow(s, t))