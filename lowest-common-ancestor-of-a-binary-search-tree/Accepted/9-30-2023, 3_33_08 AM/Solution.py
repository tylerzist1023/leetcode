// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if root == None:
            return None

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left != None and right != None and (left.val == p.val and right.val == q.val or left.val == q.val and right.val == p.val):
            p.val = root.val
            return root
        elif left != None and (left.val == p.val or left.val == q.val):
            if root.val == p.val or root.val == q.val:
                return root
            else:
                return left
        elif right != None and (right.val == p.val or right.val == q.val):
            if root.val == p.val or root.val == q.val:
                return root
            else:
                return right
        else:
            return root