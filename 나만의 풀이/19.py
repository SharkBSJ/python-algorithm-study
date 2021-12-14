from typing import Optional

# LeetCode / 92. Reverse Linked List II
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        result = head
        prev_node: Optional[ListNode] = None # For Using Reverse List
        left_node: Optional[ListNode] = None # For Using Link Left Node
        left_prev_node: Optional[ListNode] = None # For Using Link Right Node

        idx: int = 1
        while (head is not None):
            next_node = head.next
            if (idx == left - 1):
                left_prev_node = head

            if (idx >= left and idx <= right):
                if (idx == left):
                    left_node = head
                elif (idx == right):
                    if (left_prev_node is not None):
                        left_prev_node.next = head
                    left_node.next = head.next
                    head.next = prev_node
                    if (left == 1):
                        result = head
                else:
                    head.next = prev_node

            prev_node = head
            idx += 1
            head = next_node

        return result

temp = ListNode(5, None)
temp = ListNode(4, temp)
temp = ListNode(3, temp)
temp = ListNode(2, temp)
head = ListNode(1, temp)
left = 2
right = 4
print(Solution().reverseBetween(head, left, right))