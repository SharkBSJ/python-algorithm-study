from typing import Optional

# LeetCode / 206. Reverse Linked List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result_head: Optional[ListNode] = None

        while (head is not None):
            result_head = ListNode(head.val, result_head)
            head = head.next
        return result_head

temp = ListNode(5, None)
temp = ListNode(4, temp)
temp = ListNode(3, temp)
temp = ListNode(2, temp)
temp = ListNode(1, temp)
head = temp
print(Solution().reverseList(head))