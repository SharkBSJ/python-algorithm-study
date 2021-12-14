from typing import List

# LeetCode / 17. Letter Combinations of a Phone Number
class Solution:
    results = []
    possible_chars_dict = {
        '2': 'abc', 
        '3': 'def', 
        '4': 'ghi', 
        '5': 'jkl', 
        '6': 'mno',
        '7': 'pqrs', 
        '8': 'tuv', 
        '9': 'wxyz'
    }
    digits = ''
    result_str = []
    def dfs(self, idx: int):
        if idx == len(self.digits):
            self.results.append(''.join(self.result_str))
            return

        possible_chars = self.possible_chars_dict[self.digits[idx]]
        for ch in possible_chars:
            self.result_str.append(ch)
            self.dfs(idx + 1)
            self.result_str.pop()
        
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0 or not digits:
            return []
        self.results = []
        self.digits = digits
        self.dfs(0)
        return self.results

digits = "23"
print(Solution().letterCombinations(digits))