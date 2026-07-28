# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # use a helper function sameTree to evaluate if a subtree is the same as subroot
        # check if the entire tree is a subtree or if the left/right subtrees are the same
        # subtree recursively
        if not root and not subRoot:
            return True
        if not root:
            return False
        def sameTree(r1, r2):
            if not r1 and not r2:
                return True
            if not r1 or not r2 or r1.val != r2.val:
                return False
            
            left = sameTree(r1.left, r2.left)
            right = sameTree(r1.right, r2.right)

            return left and right
        
        return sameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)