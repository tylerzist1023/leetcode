// https://leetcode.com/problems/validate-binary-search-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    prev = -2**31
    first = True

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if root == None:
            return True

        validated = True

        validated &= self.isValidBST(root.left)

        if root.val > self.prev or (self.first and self.prev == -2**31):
            self.first = False
            self.prev = root.val
        else:
            return False

        validated &= self.isValidBST(root.right)

        return validated
