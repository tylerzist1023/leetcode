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
class Solution {
public:
    bool isAncestor(TreeNode* a, int v)
    {
        if(!a)
            return false;
        else if(a->val == v)
            return true;
    
        return isAncestor(a->left, v) || isAncestor(a->right, v);
    }
    
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(!root)
            return root;
        
        TreeNode* lca = root;
        if(isAncestor(lca->left, p->val) && isAncestor(lca->left, q->val))
        {
            lca = lowestCommonAncestor(root->left, p, q);
        }
        else if(isAncestor(lca->right, p->val) && isAncestor(lca->right, q->val))
        {
            lca = lowestCommonAncestor(root->right, p, q);
        }
        
        return lca;
    }
};