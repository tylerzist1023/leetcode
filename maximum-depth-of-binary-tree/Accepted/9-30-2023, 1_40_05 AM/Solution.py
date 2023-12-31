// https://leetcode.com/problems/maximum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        depth = 1
        if root.left != None:
            depth = max(depth,self.maxDepth(root.left)+1)
        if root.right != None:
            depth = max(depth,self.maxDepth(root.right)+1)
        return depth