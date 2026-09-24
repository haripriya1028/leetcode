/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void check(int target, TreeNode* root, vector<vector<int>> &ans, vector<int> &path){
        if(!root){
            return;
        }
        path.push_back(root->val);
        target-=root->val;
        if(root->left==nullptr && root->right==nullptr){
            if(target==0){
                ans.push_back(path);
            }
            path.pop_back();
            return;
        }
        check(target, root->left, ans, path);
        check(target, root->right, ans, path);
        path.pop_back();

    }
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<vector<int>> ans;
        vector<int> path;
        check(targetSum, root, ans, path);
        return ans;
    }
};