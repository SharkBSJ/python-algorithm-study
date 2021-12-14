#LeetCode / 242. Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        if ''.join(sorted_s) == ''.join(sorted_t):
            return True
        else:
            return False

s = "rat"
t = "car"
print(Solution().isAnagram(s, t))