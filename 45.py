from typing import Optional

# LeetCode / 226. Invert Binary Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def debug_dfs(root: Optional[TreeNode]):
            if not root:
                return
            debug_dfs(root.left)
            print(root.val)
            debug_dfs(root.right)

        def dfs(root: Optional[TreeNode]):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            root.left, root.right = root.right, root.left

        result = root
        #debug_dfs(root)
        dfs(root)
        #debug_dfs(result)
        return result

# root = [3,9,20,None,None,15,7]
temp1 = TreeNode(15)
temp2 = TreeNode(7)
temp2 = TreeNode(20, temp1, temp2)
temp1 = TreeNode(9)
root = TreeNode(3, temp1, temp2)
print(Solution().invertTree(root))