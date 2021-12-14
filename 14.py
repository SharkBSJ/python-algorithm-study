from typing import Optional

# LeetCode / 21. Merge Two Sorted Lists
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_idx = l1
        l2_idx = l2
        
        current_head: Optional[ListNode] = ListNode(-1, None)
        result = current_head
        while (True):
            if l1_idx is None and l2_idx is None:
                break
            if l1_idx is None:
                current_head.next = ListNode(l2_idx.val, None)
                current_head = current_head.next
                l2_idx = l2_idx.next
            elif l2_idx is None:
                current_head.next = ListNode(l1_idx.val, None)
                current_head = current_head.next
                l1_idx = l1_idx.next
            else:
                if l1_idx.val < l2_idx.val:
                    current_head.next = ListNode(l1_idx.val, None)
                    current_head = current_head.next
                    l1_idx = l1_idx.next
                else:
                    current_head.next = ListNode(l2_idx.val, None)
                    current_head = current_head.next
                    l2_idx = l2_idx.next
        
        return result.next

l1 = [], l2 = [0]
print(Solution().mergeTwoLists(l1, l2))