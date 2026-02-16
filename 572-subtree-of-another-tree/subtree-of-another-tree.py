# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root,subRoot):
            if not subRoot and root:
                return False
            if not root and subRoot:
                return False
            if not root and not subRoot:
                return True
            if root.val!=subRoot.val:
                return False

            if root.val==subRoot.val:
                return sameTree(root.right,subRoot.right) and sameTree(root.left, subRoot.left)

        if not subRoot and root:
            return True
        elif not root and subRoot:
            return False
        if root.val==subRoot.val:
            if sameTree(root,subRoot):
                return True
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left,subRoot)
