# LeetCode / 125. Valid Palindrome

def isAlphaNum(a: chr) -> bool:
    if (a >= 'A' and a <= 'Z') or (a >= 'a' and a <= 'z') or (a >= '0' and a <='9'):
            return True
    return False

def isPal(input: str) -> bool:
    firstIndex: int = 0
    lastIndex: int = len(input) - 1
    while (True):
        while (firstIndex < len(input) and not isAlphaNum(input[firstIndex])):
            firstIndex += 1
        while (lastIndex > 0 and not isAlphaNum(input[lastIndex])):
            lastIndex -= 1
        if (firstIndex >= lastIndex):
            break
        if (input[firstIndex].lower() != input[lastIndex].lower()):
            return False
        firstIndex += 1
        lastIndex -= 1
    return True

print(isPal('"race a car"'))
