# Leet Code / 641. Design Circular Deque
class Node:
    def __init__(self, value, prev: None, next: None):
        self.value = value
        self.prev = prev
        self.next = next

class MyCircularDeque:
    def __init__(self, k: int):
        self.k = k
        self.head = Node(-1, None, None)
        self.tail = self.head
        self.current_size = 0

    def init_node(self):
        self.head = Node(-1, None, None)
        self.tail = self.head
        self.current_size = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.head.value == -1:
            self.head.value = value
        else:
            self.head.prev = Node(value, None, self.head)
            self.head = self.head.prev
        self.current_size += 1

        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.tail.value == -1:
            self.tail.value = value
        else:
            self.tail.next = Node(value, self.tail, None)
            self.tail = self.tail.next
        self.current_size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.head = self.head.next
        self.current_size -= 1

        if self.isEmpty():
            self.init_node()
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        
        self.tail = self.tail.prev
        self.current_size -= 1

        if self.isEmpty():
            self.init_node()
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1

        return self.head.value

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
            
        return self.tail.value

    def isEmpty(self) -> bool:
        return self.current_size == 0

    def isFull(self) -> bool:
        return self.current_size == self.k

obj = MyCircularDeque(3)
param_1 = obj.insertLast(1)
print(param_1)
param_2 = obj.insertLast(2)
print(param_2)
param_3 = obj.insertFront(3)
print(param_3)
param_4 = obj.insertFront(4)
print(param_4)
param_5 = obj.getRear()
print(param_5)
param_6 = obj.isFull()
print(param_6)
param_7 = obj.deleteLast()
print(param_7)
param_8 = obj.insertFront(5)
print(param_8)
param_9 = obj.deleteFront()
print(param_9)
param_10 = obj.getFront()
print(param_10)