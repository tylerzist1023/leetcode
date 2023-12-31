// https://leetcode.com/problems/binary-tree-right-side-view

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if root is None:
            return []

        vals = [root.val]
        h = 1

        def dfs(root):
            nonlocal h
            h += 1
            if root is None:
                h -= 1
                return
            
            if root.right:
                if len(vals) < h:
                    vals.append(root.right.val)
                dfs(root.right)
                
            if root.left:
                if len(vals) < h:
                    vals.append(root.left.val)
                dfs(root.left)

            h -= 1

        dfs(root)

        return vals