// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#pragma GCC optimize("O3")
class Solution {
public:
    bool isAncestor(TreeNode* a, TreeNode* b)
    {
        if(!a)
            return false;
        else if(a == b)
            return true;
    
        return isAncestor(a->left, b) || isAncestor(a->right, b);
    }
    
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(!root)
            return root;
        
        TreeNode* lca = root;
        if(isAncestor(lca->left, p) && isAncestor(lca->left, q))
        {
            lca = lowestCommonAncestor(root->left, p, q);
        }
        else if(isAncestor(lca->right, p) && isAncestor(lca->right, q))
        {
            lca = lowestCommonAncestor(root->right, p, q);
        }
        
        return lca;
    }
};