from typing import Optional

#LeetCode / 148. Sort List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result_array = []
        node = head
        while node:
            result_array.append(node.val)
            node = node.next
        result_array.sort()
        
        result = None
        prev = None
        temp = result
        for num in result_array:
            temp = ListNode(num)
            if prev:
                prev.next = temp
            if not result:
                result = temp
            prev = temp
        
        return result


# O(n log n)
# head = [4,2,1,3]
temp = ListNode(3)
temp = ListNode(1, temp)
temp = ListNode(2, temp)
head = ListNode(4, temp)
head = ListNode(4)
# Output : [1,2,3,4]
print(Solution().sortList(head))

result = Solution().sortList(head)
while result:
    print(result.val)
    result = result.next