// https://leetcode.com/problems/minimum-absolute-difference-in-bst

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def f(root: TreeNode, arr=[]):
            if root:
                arr.append(root.val)

                f(root.left, arr=arr)
                f(root.right, arr=arr)
            return arr

        arr = sorted(set(f(root)))
        print(arr)
        smallest = arr[len(arr)-1]
        while(len(arr) > 1):
            if arr[1]-arr[0] < smallest:
                smallest = arr[1]-arr[0]
            arr.remove(arr[0])
        return smallest