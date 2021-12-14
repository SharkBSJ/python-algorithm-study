from typing import Optional

# Leet Code / 617. Merge Two Binary Trees

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
            if not root1:
                return root2
            elif not root2:
                return root1
            
            root1.left = dfs(root1.left, root2.left)
            root1.right = dfs(root1.right, root2.right)
            root1.val += root2.val
            return root1
        
        return dfs(root1, root2)