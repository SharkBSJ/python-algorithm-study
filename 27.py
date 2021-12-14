from typing import Optional
from typing import List
import heapq

# Leet Code / 23. Merge k Sorted Lists
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result_head = ListNode(0, None)
        result = result_head

        heap = []
        for head in lists:
            while head is not None:
                heapq.heappush(heap, head.val)
                head = head.next
        
        while len(heap) > 0:
            result.next = ListNode(heapq.heappop(heap), None)
            result = result.next
            
        return result_head.next

temp = ListNode(5, None)
temp = ListNode(4, temp)
a = ListNode(1, temp)

temp = ListNode(4, None)
temp = ListNode(3, temp)
b = ListNode(1, temp)

temp = Solution().mergeKLists([a, b])
while (temp is not None):
    print(temp.val)
    temp = temp.next