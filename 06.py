from typing import List

# LeetCode / 5. Longest Palindrome Substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result_word: str = ''
        result_num: int = 0
        for index in range(len(s)):
            temp_length: int = result_num
            while (True):
                if (temp_length + index > len(s)):
                    break

                original_str: str = s[index:index+temp_length]
                reverse_str: str = original_str[::-1]
                
                if (result_num < temp_length and original_str == reverse_str):
                    result_num = temp_length
                    result_word = original_str  
                temp_length += 1
        return result_word
        
s = "cbbd"
print(Solution().longestPalindrome(s))
            
