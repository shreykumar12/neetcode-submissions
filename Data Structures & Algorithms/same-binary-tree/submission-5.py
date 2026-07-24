# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # recursive dfs base case check if the nodes both None first 
        # then check if one is None and the other is not or the values are differnt and return false
        # then recrusively call on the 2 left and right subtrees
        # at the end left and right will be the same if the trees are the same so we return left and right
        
        
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right