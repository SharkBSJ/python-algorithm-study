from typing import Optional

# Leet Code / 938. Range Sum of BST

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.result = 0
        def dfs(root: Optional[TreeNode]):
            if not root:
                return
            if root.val >= low and root.val <= high:
                self.result += root.val
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return self.result

temp1 = TreeNode(20)
temp2 = TreeNode(10)
root = TreeNode(10, temp1, temp2)
low = 7
high = 15
print(Solution().rangeSumBST(root, low, high))