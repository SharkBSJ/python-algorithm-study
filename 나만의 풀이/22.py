from typing import List

# Leet Code / 739. Daily Temperatures
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result: List[int] = [0] * len(temperatures)

        stack: List[tuple] = []
        for idx in range(len(temperatures)):
            if len(stack) != 0 and stack[-1][1] < temperatures[idx]:
                while (True):
                    t: tuple = stack[-1]
                    if (t[1] >= temperatures[idx]):
                        break
                    result[t[0]] = idx - t[0]
                    stack.pop()
                    if (len(stack) == 0):
                        break
            stack.append((idx, temperatures[idx]))

        return result
        
temperatures = [73,74,75,71,69,72,76,73]
print(Solution().dailyTemperatures(temperatures))