from typing import Optional

# LeetCode / 234. Palindrome Linked List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        count: int = 0
        reverse_head: Optional[ListNode] = None

        current_head: Optional[ListNode] = head
        while(current_head is not None):
            count += 1
            reverse_head = ListNode(current_head.val, reverse_head)
            current_head = current_head.next
            
        current_head = head
        current_reverse_head = reverse_head
        for idx in range(int(count / 2)):
            if current_head.val != current_reverse_head.val:
                return False
            current_head = current_head.next
            current_reverse_head = current_reverse_head.next

        return True

temp = ListNode(1, None)
temp = ListNode(2, temp)
temp = ListNode(2, temp)
head = ListNode(1, temp)
print(Solution().isPalindrome(head))