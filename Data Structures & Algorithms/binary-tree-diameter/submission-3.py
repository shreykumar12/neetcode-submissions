# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Recursive DFS that return the height from the node passed in
        # in that function we check the diameter by adding the heights
        # of the left and right subtree and checking if it's greater than
        # the current result

        self.res = 0

        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            self.res = max(self.res, left + right)

            return 1 + max(left, right)
        
        dfs(root)
        return self.res

            