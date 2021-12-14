from typing import Optional

# LeetCode / 2. Add Two Numbers
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_head: Optional[ListNode] = ListNode(0, None)
        current_result = result_head

        temp_add: int = 0
        while (l1 is not None or l2 is not None):
            if (l2 is None):
                temp_val = temp_add + l1.val
                l1 = l1.next
            elif (l1 is None):
                temp_val = temp_add + l2.val
                l2 = l2.next
            else:
                temp_val = temp_add + l1.val + l2.val
                l1, l2 = l1.next, l2.next
            
            temp_add = 0
            if (temp_val >= 10):
                temp_val -= 10
                temp_add = 1

            current_result.next = ListNode(temp_val, None)
            current_result = current_result.next

        if (temp_add == 1):
            current_result.next = ListNode(temp_add, None)
            current_result = current_result.next
        result_head = result_head.next
        return result_head

temp = ListNode(2, None)
temp = ListNode(4, temp)
l1 = ListNode(3, temp)
temp = ListNode(5, temp)
temp = ListNode(6, temp)
l2 = ListNode(4, temp)
print(Solution().addTwoNumbers(l1, l2))