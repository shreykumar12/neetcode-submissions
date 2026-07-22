# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        trav1 = []
        trav2 = []

        def dfs(root1, root2):
            if not root1 and not root2:
                return True
            if (not root1 and root2) or (root1 and not root2) or root1.val != root2.val:
                return False
            
            left = root1.left
            left2 = root2.left
            right = root1.right
            right2 = root2.right

            return dfs(left, left2) and dfs(right, right2)
        
        return dfs(p, q)
