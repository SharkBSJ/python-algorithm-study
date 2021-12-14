from typing import Optional

# LeetCode / 543. Diameter of Binary Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 0
        def dfs(root: Optional[TreeNode]):
            if not root:
                return 0
            left_depth = dfs(root.left) + 1
            right_depth = dfs(root.right) + 1
            if left_depth + right_depth > self.max_depth:
                self.max_depth = left_depth + right_depth
            
            return max(left_depth, right_depth)

        dfs(root)
        return self.max_depth - 2

# root = [3,9,20,None,None,15,7]
temp1 = TreeNode(15)
temp2 = TreeNode(7)
temp2 = TreeNode(20, temp1, temp2)
temp1 = TreeNode(9)
root = TreeNode(3, temp1, temp2)
print(Solution().diameterOfBinaryTree(root))