from typing import Optional

# Leet Code / 110. Balanced Binary Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.result = True
        def dfs(root: Optional[TreeNode], depth: int) -> int:
            if not root:
                return depth
            left_depth = dfs(root.left, depth + 1)
            right_depth = dfs(root.right, depth + 1)
            if abs(left_depth - right_depth) > 1:
                self.result = False
            return max(left_depth, right_depth)
        dfs(root, 0)
        return self.result

temp1 = TreeNode(8)
temp1 = TreeNode(4, temp1, None)
temp2 = TreeNode(5)
temp1 = TreeNode(2, temp1, temp2)
root = TreeNode(1)
root.left = temp1
temp1 = TreeNode(6)
temp2 = TreeNode(3, temp1)
root.right = temp2
print(Solution().isBalanced(root))