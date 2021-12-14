from typing import Optional

# Leet Code / 783. Minimum Distance Between BST Nodes

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.nums = []
        def dfs(root: Optional[TreeNode]):
            if not root:
                return
            dfs(root.left)
            self.nums.append(root.val)
            dfs(root.right)
        
        dfs(root)
        result = 100000
        for i in range(0, len(self.nums) - 1, 1):
            if abs(self.nums[i + 1] - self.nums[i]) < result:
                result = abs(self.nums[i + 1] - self.nums[i])
        return result

temp1 = TreeNode(7)
temp2 = TreeNode(17)
root = TreeNode(10, temp1, temp2)
print(Solution().minDiffInBST(root))
# The number of nodes in the tree is in the range [2, 100]
# 0 <= Node.val <= 105