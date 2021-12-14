# Leet Code / 1038. Binary Search Tree to Greater Sum Tree

# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.sum = 0
        def dfs(root: Optional[TreeNode]):
            if not root:
                return 
            
            dfs(root.right)
            self.sum += root.val
            root.val = self.sum
            dfs(root.left)
        dfs(root)
        return root

temp1 = TreeNode(8)
temp1 = TreeNode(4, temp1, None)
temp2 = TreeNode(5)
temp1 = TreeNode(2, temp1, temp2)
root = TreeNode(1)
root.left = temp1
temp1 = TreeNode(6)
temp2 = TreeNode(3, temp1)
root.right = temp2
print(Solution().bstToGst(root).val)