from typing import Optional

# LeetCode / 328. Odd Even Linked List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head is None):
            return 

        odd_head: Optional[ListNode] = ListNode(None)
        even_head: Optional[ListNode] = ListNode(None)

        odd_p = odd_head
        even_p = even_head
        while (head is not None and head.next is not None):
            odd_p.next = head
            even_p.next = head.next
            odd_p = odd_p.next
            even_p = even_p.next
            head = head.next.next
        
        if (head is not None):
            odd_p.next = head
            odd_p = odd_p.next
            even_p.next = None

        odd_p.next = even_head.next
        odd_head = odd_head.next

        return odd_head

temp = ListNode(5, None)
temp = ListNode(4, temp)
temp = ListNode(3, temp)
temp = ListNode(2, temp)
head = ListNode(1, temp)
print(Solution().oddEvenList(head))