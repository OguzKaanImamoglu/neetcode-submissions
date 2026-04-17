# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 0
        res = None

        def left_first_dfs(node):
            nonlocal counter
            nonlocal res

            if not node:
                return

            left_first_dfs(node.left)
            
            if node:
                counter+= 1

            if counter == k:
                res = node.val
                
            
            left_first_dfs(node.right)

        left_first_dfs(root)
        return res
        