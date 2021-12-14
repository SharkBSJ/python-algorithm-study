# Leet Code / 622. Design Circular Queue
class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.front = 0
        self.end = 0
        self.queue = [-1] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.queue[self.end % self.k] = value
        self.end += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.front += 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.queue[self.front % self.k]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.queue[(self.end - 1) % self.k]

    def isEmpty(self) -> bool:
        return self.front == self.end

    def isFull(self) -> bool:
        return self.end - self.front == self.k


obj = MyCircularQueue(3)
param_1 = obj.enQueue(2)
print(param_1)
param_2 = obj.deQueue()
print(param_2)
param_3 = obj.Front()
print(param_3)
param_4 = obj.Rear()
print(param_4)
param_5 = obj.isEmpty()
print(param_5)
param_6 = obj.isFull()
print(param_6)