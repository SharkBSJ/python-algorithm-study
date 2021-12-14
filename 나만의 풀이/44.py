from typing import Optional

# LeetCode / 687. Longest Univalue Path

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(root: Optional[TreeNode], chk_val: Optional[int]) -> int:
            if not root:
                return 0

            temp1 = dfs(root.left, root.val)
            temp2 = dfs(root.right, root.val) 
            temp = temp1 + temp2 + 1
            if temp > self.result:
                self.result = temp
            if root.val == chk_val or chk_val is None:
                return max(temp1 + 1, temp2 + 1)
            else:
                return 0

        self.result = 0
        dfs(root, None)
        return self.result - 1

# root = [3,9,20,None,None,15,7]
temp1 = TreeNode(2)
temp2 = TreeNode(2)
temp2 = TreeNode(2, temp1, temp2)
temp1 = TreeNode(3)
root = TreeNode(3, temp1, temp2)
print(Solution().longestUnivaluePath(root))