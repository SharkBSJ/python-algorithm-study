# LeetCode / 706. Design HashMap

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val, next=None):
        self.val = val # (key, value)
        self.next = next

SIZE = 10007
class MyHashMap:
    def __init__(self):
        self.my_hashmap = [None] * SIZE

    def put(self, key: int, value: int) -> None:
        temp_head = self.my_hashmap[key % SIZE]
        if temp_head is None:
            self.my_hashmap[key % SIZE] = ListNode((key, value), None)
            return

        while temp_head.next is not None and temp_head.val[0] != key:
            temp_head = temp_head.next
        
        if temp_head.val[0] == key:
            temp_head.val = (key, value)
        else:
            temp_head.next = ListNode((key, value), None)

    def get(self, key: int) -> int:
        temp_head = self.my_hashmap[key % SIZE]
        if temp_head is None:
            return -1

        while temp_head.next is not None and temp_head.val[0] != key:
            temp_head = temp_head.next
        
        if temp_head.val[0] == key:
            return temp_head.val[1]
        return -1

    def remove(self, key: int) -> None:
        temp_head = self.my_hashmap[key % SIZE]
        if temp_head is None:
            return
        if temp_head.val[0] == key:
            self.my_hashmap[key % SIZE] = temp_head.next
            return
        
        while temp_head.next is not None and temp_head.next.val[0] != key:
            temp_head = temp_head.next
        
        if temp_head.next is not None and temp_head.next.val[0] == key:
            temp_head.next = temp_head.next.next

# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1,2)
obj.put(1,3)
param_1 = obj.get(1)
obj.remove(1)
param_2 = obj.get(1)

print(param_1)
print(param_2)