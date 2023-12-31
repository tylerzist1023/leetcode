// https://leetcode.com/problems/invert-binary-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return root

        self.invertTree(root.left)
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)

        return root