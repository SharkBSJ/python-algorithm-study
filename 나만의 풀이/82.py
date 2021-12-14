from typing import List

# LeetCode / 455. Assign Cookies

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        s_idx = 0
        result = 0

        for child in g:
            while s_idx < len(s):
                if child <= s[s_idx]:
                    s_idx += 1
                    result += 1
                    break
                s_idx += 1
        
        return result
        
        
g = [1,2]
s = [1,2,3]
print(Solution().findContentChildren(g, s))