// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        inserted = {}
        root = TreeNode()
        cur = root
        while preorder and inorder:
            if preorder[0] == inorder[0]:
                cur.val = preorder[0]
                inserted[cur.val] = cur
                
                del preorder[0]
                del inorder[0]
                if inorder and inorder[0] not in inserted.keys():
                    cur.right = TreeNode()
                    cur = cur.right
                
            elif inorder[0] not in preorder:
                while inorder[0] not in preorder:
                    cur = inserted[inorder[0]]
                    del inorder[0]
                cur.right = TreeNode()
                cur = cur.right
                cur.val = preorder[0]
            elif preorder[0] in inorder:
                cur.val = preorder[0]
                inserted[cur.val] = cur
                del preorder[0]
                cur.left = TreeNode()
                cur = cur.left
        return root