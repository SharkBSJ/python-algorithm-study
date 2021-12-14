from typing import List, Optional

# Leet Code / 105. Construct Binary Tree from Preorder and Inorder Traversal

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
            if not preorder or not inorder:
                return None
            
            idx: int = 0
            while idx < len(preorder):
                try :
                    inorder.index(preorder[idx])
                    break
                except :
                    pass
                idx += 1
            if idx != len(preorder):
                result = TreeNode(preorder[idx])
                left_inorder_index: int = inorder.index(preorder[idx])
                result.left = dfs(preorder[idx:], inorder[0:left_inorder_index])
                if idx + 1 != len(preorder):
                    result.right = dfs(preorder[idx + 1:], inorder[left_inorder_index + 1:])
                return result

            return None
 
        result = dfs(preorder, inorder)
        def debug_dfs(root: Optional[TreeNode]):
            if not root:
                return
            debug_dfs(root.left)
            print(root.val)
            debug_dfs(root.right)
        
        #debug_dfs(result)
        return result

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
# OUtput : [3,9,20,null,null,15,7]
print(Solution().buildTree(preorder, inorder))

# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000