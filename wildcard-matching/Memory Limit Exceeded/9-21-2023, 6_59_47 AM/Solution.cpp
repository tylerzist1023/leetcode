// https://leetcode.com/problems/wildcard-matching

class Solution {
public:
    bool isMatch(string s, string p) {
        if(p.size() == 0 && s.size() == 0)
            return true;
        else if(s.size() == 0) {
            if(p[0] == '*') {
                return isMatch(s, p.substr(1, p.size()-1));
            } else {
                return false;
            }
        } else if(p.size() == 0){
            return false;
        }

        if(s[0] == p[0] || p[0] == '?') {
            return isMatch(s.substr(1, s.size()-1), p.substr(1, p.size()-1));
        } else if(p[0] == '*') {
            if(p.size() > 1 && p[1] == '*') {
                return isMatch(s, p.substr(1, p.size()-1));
            } else {
                return (
                    isMatch(s.substr(1, s.size()-1), p) ||
                    isMatch(s.substr(1, s.size()-1), p.substr(1, p.size()-1)) ||
                    isMatch(s, p.substr(1, p.size()-1))
                );
            }
        } else {
            return false;
        }
    }
};