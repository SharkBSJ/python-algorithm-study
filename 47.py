

# Leet Code / 297. Serialize and Deserialize Binary Tree

# Definition for a binary tree node.
from typing import Deque, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []
        deque = Deque()
        deque.append(root)
        while deque:
            temp = deque.popleft()
            if temp == None:
                result.append(None)
                continue
            deque.append(temp.left)
            deque.append(temp.right)
            result.append(temp.val)

        while len(result) > 0:
            if result[len(result) - 1] == None:
                result.pop()
            else: 
                break
        
        result_str = str(result)
        result_str = result_str.replace('None', 'null')
        result_str = result_str.replace(' ', '')
        return result_str

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
            return None
        nodes = [None if val == 'null' else TreeNode(int(val))
             for val in data.strip('[]').split(',')]
        
        idx = 1
        deque = Deque()
        result = nodes[0]
        deque.append(result)
        while deque:
            root: Optional[TreeNode] = deque.popleft()
            if root == None:
                continue
            left_node = None
            if idx < len(nodes):
                left_node = nodes[idx]
                deque.append(left_node)
                idx += 1
            right_node = None
            if idx < len(nodes):
                right_node = nodes[idx]
                deque.append(right_node)
                idx += 1
            root.left = left_node
            root.right = right_node
        return result

temp1 = TreeNode(8)
temp1 = TreeNode(4, temp1, None)
temp2 = TreeNode(5)
temp1 = TreeNode(2, temp1, temp2)
root = TreeNode(1)
root.left = temp1
temp1 = TreeNode(6)
temp2 = TreeNode(3, temp1)
root.right = temp2
temp = Codec().serialize(root)
print(temp)
print(Codec().serialize(Codec().deserialize(temp)))