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
        
        if(v < a->val)
            return isAncestor(a->left, v);
        else if(v > a->val)
            return isAncestor(a->right, v);
    }
    
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(!root)
            return root;
        
        TreeNode* lca = root;
        if(lca->isAncestor(lca->left, p->val) && lca->isAncestor(lca->left, q->val))
        {
            lca = lowestCommonAncestor(root->left, p, q);
        }
        if(lca->isAncestor(lca->right, p->val) && lca->isAncestor(lca->right, q->val))
        {
            lca = lowestCommonAncestor(root->right, p, q);
        }
        
        return lca;
    }
};