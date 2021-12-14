# LeetCode / 771. Jewels and Stones
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones_dict: dict = {}
        for c in stones:
            if c in stones_dict:
                stones_dict[c] += 1
            else:
                stones_dict[c] = 1
        
        result: int = 0
        for c in jewels:
            if c in stones_dict:
                result += stones_dict[c]
        
        return result

jewels = "aA"
stones = "aAAbbbb"
print(Solution().numJewelsInStones(jewels, stones))