// https://leetcode.com/problems/subtree-of-another-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        
        if root == None or subRoot == None:
            return False

        if self.isSameTree(root,subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (p == None and q != None) or (p != None and q == None):
            return False
        elif p == None and q == None:
            return True
        elif p.val == q.val: 
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False