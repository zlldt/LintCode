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
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        if root is None:
            return True
        depthleft = 0
        depthright = 0
        if root.left is not None :
            depthleft = self.depth(root.left)
        if root.right is not None:
            depthright = self.depth(root.right)
        if abs(depthleft - depthright)>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)


    def depth(self, root):
        depthleft = 0
        depthright = 0
        if root.left is not None:
            depthleft = self.depth(root.left)
        if root.right is not None:
            depthright = self.depth(root.right)
        return max(depthleft, depthright)+1
