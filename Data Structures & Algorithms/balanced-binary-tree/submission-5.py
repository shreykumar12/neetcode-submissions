# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # recursive dfs returning if the tree is balanced and its height
        # at each subtree
        
        def dfs(root):
            # Base case: A None node is balanced and has height 0
            if not root:
                return [True, 0]
            # Get heights of left and right subtree
            # Also checks if they're balanced
            left = dfs(root.left)
            right = dfs(root.right)
            # bool: checks if left/right subtrees are balanced and if the current
            # tree from root is balanced based on subtree heights
            balance = left[0] and right[0] and (abs(left[1] - right[1]) <= 1)

            return [balance, max(left[1], right[1]) + 1]
        
        return dfs(root)[0]
