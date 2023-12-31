// https://leetcode.com/problems/minimum-absolute-difference-in-bst

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        minval = 100000
        prev = None
        def f(root: TreeNode):
            nonlocal minval, prev
            if not root:
                return minval

            f(root.left)
            if prev:
                minval = min(minval, abs(root.val - prev.val))
            prev = root
            f(root.right)

            return minval
        return f(root)