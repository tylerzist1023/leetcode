// https://leetcode.com/problems/contains-duplicate

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::set<int> values;

        for(int n : nums) {
            if(values.find(n) == values.end()) {
                values.insert(n);
            } else {
                return true;
            }
        }
        return false;
    }
};