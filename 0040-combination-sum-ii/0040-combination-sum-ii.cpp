class Solution {
public:
    void solve(vector<vector<int>>& result, vector<int>& combination, vector<int>& candidates, int start, int target){
        
        if(target==0){
            result.push_back(combination);
            return;
        }
        
        for(int i=start; i<candidates.size(); i++){
            
            if(i>start && candidates[i]==candidates[i-1]){
                continue;
            }
            if(candidates[i]>target){
                break;
            }
            combination.push_back(candidates[i]);
            solve(result, combination, candidates, i+1, target-candidates[i]);
            combination.pop_back();
        }
    }
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        vector<int> combination;
        sort(candidates.begin(), candidates.end());
        solve(result, combination, candidates, 0, target);
        return result;
    }
};