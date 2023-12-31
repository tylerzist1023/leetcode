// https://leetcode.com/problems/valid-anagram

class Solution {
public:
    bool isAnagram(string s, string t) {
        std::map<char, int> letters;
        for(char c : s) {
            if(letters.find(c) == letters.end())
            {
                letters[c] = 1;
            }
            else
            {
                letters[c]++;
            }
        }
        for(char c : t) {
            if(letters.find(c) == letters.end())
            {
                return false;
            }
            else
            {
                letters[c]--;
            }
        }

        for(auto x : letters) {
            if(x.second != 0)
                return false;
        }

        return true;
    }
};