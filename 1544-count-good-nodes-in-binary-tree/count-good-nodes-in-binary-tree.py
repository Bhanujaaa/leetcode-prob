# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def valid (maxval,node):
            if not node:
                return 0
            maxval=max(maxval,node.val)
            res=1 if node.val>=maxval else 0
            res+=valid(maxval,node.left)
            res+=valid(maxval,node.right)
            return res
        return valid(root.val,root)
        