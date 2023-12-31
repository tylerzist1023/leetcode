// https://leetcode.com/problems/binary-tree-paths

import java.util.ArrayList;
import java.util.List;

class Solution
{
    private void nodeTraverser(TreeNode root, List<String> paths, List<Integer> path)
    {
        path.add(root.val);
        if(root.left == null && root.right == null)
        {
            StringBuilder pathString = new StringBuilder(path.get(0).toString());
            for(int i = 1; i < path.size(); i++)
            {
                pathString.append("->").append(path.get(i).toString());
            }
            paths.add(pathString.toString());
        }

        if(root.left != null)
        {
            nodeTraverser(root.left, paths, path);
            path.remove(path.size() - 1);
        }
        if(root.right != null)
        {
            nodeTraverser(root.right, paths, path);
            path.remove(path.size() - 1);
        }

    }

    public List<String> binaryTreePaths(TreeNode root)
    {
        List<String> paths = new ArrayList<>();

        nodeTraverser(root, paths, new ArrayList<>());

        return paths;
    }
}