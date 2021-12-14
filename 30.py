from collections import defaultdict

# LeetCode / 3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size: int = 0
        idx: int = 0
        counter_dict = defaultdict(int)

        while True:
            if idx + size >= len(s):
                break

            flag_duplication: bool = False
            for key in counter_dict:
                if counter_dict[key] >= 2:
                    flag_duplication = True

            if flag_duplication == False and counter_dict[s[idx + size]] == 0:
                counter_dict[s[idx + size]] += 1
                size += 1
            else:
                counter_dict[s[idx]] -= 1
                counter_dict[s[idx + size]] += 1
                idx += 1
        return size

s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))