"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        flag, minval,maxval= self.validate(root)
        return flag
    
    def validate(self, root):
        if root is None:
            return True, 0, 0
        minval = root.val
        maxval = root.val
        if root.left is not None:
            flag, minval, lastval = self.validate(root.left)
            if flag == False or lastval >= root.val:
                return False, 0, 0
        if root.right is not None:
            flag, lastval, maxval = self.validate(root.right)
            if flag == False or lastval <= root.val:
                return False, 0, 0
        if root.left is None and root.right is None:
            return True, root.val, root.val
        return True, minval, maxval
