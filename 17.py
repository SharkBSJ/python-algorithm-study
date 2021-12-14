from typing import Optional

# LeetCode / 24. Swap Nodes in Pairs
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head is None):
            return None
        if (head.next is None):
            return head

        result_head: Optional[ListNode] = head.next
        prev: Optional[ListNode] = None

        while(head is not None and head.next is not None):
            temp = head.next
            head.next.next, head.next = head, head.next.next
            if (prev is not None):
                prev.next = temp
            prev = head
            head = head.next
        return result_head

temp = ListNode(4, None)
temp = ListNode(3, temp)
temp = ListNode(2, temp)
head = ListNode(1, temp)
print(Solution().swapPairs(head))