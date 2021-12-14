from typing import List

# LeetCode / 344. Reverse String
class Solution:
    def reverseString(self, s: List[str]) -> None:
        #s[:] = s[::-1]
        s.reverse()
        '''index: int = 0
        while(index < len(s) // 2):
            temp: str = s[index]
            s[index] = s[len(s) - 1 - index]
            s[len(s) - 1 - index] = temp
            index += 1'''

s: List[str] = ['a', 'b']
Solution().reverseString(s)
print(s)