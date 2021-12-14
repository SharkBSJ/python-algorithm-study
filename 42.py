from typing import Optional

# LeetCode / 104. Maximum Depth of Binary Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode]):
            if not root:
                return 0
            return max(dfs(root.left) + 1, dfs(root.right) + 1)
        return dfs(root)

# root = [3,9,20,None,None,15,7]
temp1 = TreeNode(15)
temp2 = TreeNode(7)
temp2 = TreeNode(20, temp1, temp2)
temp1 = TreeNode(9)
root = TreeNode(3, temp1, temp2)
print(Solution().maxDepth(root))