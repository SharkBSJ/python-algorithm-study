# LeetCode / 20. Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        result: bool = True
        stack = []

        for ch in s:
            if (ch == ')' or ch =='}' or ch ==']'):
                if (len(stack) == 0):
                    result = False
                    break

                temp = stack.pop()
                if (ch == ')' and temp != '('):
                    result = False
                    break
                elif (ch == '}' and temp != '{'):
                    result = False
                    break
                elif (ch == ']' and temp != '['):
                    result = False
                    break
            else:
                stack.append(ch)

        if (len(stack) > 0):
            result = False

        return result

s = "(]"
print(Solution().isValid(s))