from collections import defaultdict

#LeetCode / 70. Climbing Stairs

class Solution:
    def __init__(self):
        self.result = defaultdict(int)
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        if self.result[n]:
            return self.result[n]
        
        self.result[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.result[n]

print(Solution().climbStairs(3))