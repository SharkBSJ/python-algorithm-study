from typing import List

# Leet Code / 232. Implement Queue using Stacks
class MyQueue:

    def __init__(self):
        self.stack: List[int] = []

    def push(self, x: int) -> None:
        temp: List[int] = []
        result: List[int] = []
        
        n: int = len(self.stack)
        for _ in range(n):
            temp.append(self.stack.pop())
        result.append(x)
        for _ in range(n):
            result.append(temp.pop())
        
        self.stack = result

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)

a = obj.peek()
b = obj.pop()
c = obj.empty()

print(a)
print(b)
print(c)