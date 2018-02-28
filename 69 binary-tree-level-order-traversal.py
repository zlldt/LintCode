"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        result=[]
        if root is None:
            return result
        self.dfs(root,0,result)
        return result
    
    def dfs(self,root,depth,result):
        if root is None:
            return
        if (len(result)-1)<depth:
            result.append([])
        result[depth].append(root.val)
        self.dfs(root.left,depth+1,result)
        self.dfs(root.right,depth+1,result)
