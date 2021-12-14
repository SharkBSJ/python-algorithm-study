from typing import Optional

#LeetCode / 147. Insertion Sort List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num_list = []

        node = head
        while node:
            num_list.append(node.val)
            node = node.next

        for i in range(1, len(num_list)):
            idx = i
            for j in range(i - 1, -1, -1):
                if num_list[idx] <= num_list[j]:
                    num_list[idx], num_list[j] = num_list[j], num_list[idx]
                    idx = j
                else:
                    break
        
        node = head
        idx = 0
        while node:
            node.val = num_list[idx]
            node = node.next
            idx += 1
        
        # For Debugging
        #node = head
        #while node:
        #    print(node.val)
        #    node = node.next

        return head

temp = ListNode(0)
temp = ListNode(4, temp)
temp = ListNode(3, temp)
temp = ListNode(5, temp)
head = ListNode(-1, temp)
print(Solution().insertionSortList(head))