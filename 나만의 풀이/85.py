from typing import List

#LeetCode / 509. Fibonacci Number

NOT_DEFINED = -1
class Solution:
    def __init__(self):
        self.result = [NOT_DEFINED] * 1000
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        if self.result[n] != NOT_DEFINED:
            return self.result[n]
        
        self.result[n] = self.fib(n-1) + self.fib(n-2)
        return self.result[n]

print(Solution().fib(4))