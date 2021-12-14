from collections import deque

# Leet Code / 225. Implement Stack using Queues
class MyStack:
    def __init__(self):
        self.deq = deque()

    def push(self, x: int) -> None:
        self.deq.append(x)

    def pop(self) -> int:
        result: int = None

        temp = deque()
        while not self.empty():
            t: int = self.deq.popleft()
            if not self.empty():
                temp.append(t)
            else:
                result = t

        self.deq = temp
        return result

    def top(self) -> int:
        result: int = None

        temp = deque()
        while not self.empty():
            t: int = self.deq.popleft()
            temp.append(t)
            if self.empty():
                result = t

        self.deq = temp
        return result

    def empty(self) -> bool:
        if len(self.deq) == 0:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
myStack = MyStack()
myStack.push(1)
myStack.push(2)
a = myStack.top()
b = myStack.pop()
c = myStack.empty()

print(a)
print(b)
print(c)
