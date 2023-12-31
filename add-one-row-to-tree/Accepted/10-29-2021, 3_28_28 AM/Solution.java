// https://leetcode.com/problems/add-one-row-to-tree

class Solution
{
    public TreeNode addOneRow(TreeNode root, int val, int depth)
    {
        if(depth == 1)
        {
            return new TreeNode(val, root, null);
        }
        else if(depth > 2)
        {
            if(root.left != null) addOneRow(root.left, val, depth-1);
            if(root.right != null) addOneRow(root.right, val, depth-1);
        }
        else
        {
            root.left = new TreeNode(val, root.left, null);
            root.right = new TreeNode(val, null, root.right);
        }
        return root;
    }
}