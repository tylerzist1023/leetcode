// https://leetcode.com/problems/binary-tree-level-order-traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root == None:
            return []

        left_list = self.levelOrder(root.left)
        right_list = self.levelOrder(root.right)

        this_list = []
        this_list.append([root.val])

        if(len(left_list) > len(right_list)):
            for i in range(len(right_list)):
                left_list[i] = left_list[i]+right_list[i]
            this_list.extend(left_list)
        elif(len(left_list) <= len(right_list)):
            for i in range(len(left_list)):
                right_list[i] = left_list[i]+right_list[i]
            this_list.extend(right_list)
        
        return this_list