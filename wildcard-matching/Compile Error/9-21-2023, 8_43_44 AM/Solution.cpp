// https://leetcode.com/problems/wildcard-matching

class Solution {
public:
    bool isMatch(string s, string p) {
        int dp[s.size()+1][p.size()+1];
        for(int si = 0; si <= s.size(); si++)
        {
            for(int pi = 0; pi <= p.size(); pi++)
            {
                dp[si][pi] = 0;
            }
        }
        dp[0][0] = 1;

        for(int i = 1; i <= s.size() i++)
        {
            if(p[i-1] == '*')
            {
                dp[0][i] = dp[0][i-1];
            }
        }

        for(int si = 1; si <= s.size(); si++)
        {
            for(int pi = 1; pi <= p.size(); pi++)
            {
                if(s[si-1] == p[pi-1] || p[pi-1] == '?')
                {
                    dp[si][pi] = dp[si-1][pi-1];
                    if(pi > 1 && p[pi-2] == '*')
                    {
                        dp[si][pi] |= dp[si-1][pi-2];
                    }
                }
                else if(p[pi-1] == '*')
                {
                    dp[si][pi] = dp[si-1][pi] || dp[si][pi-1] || dp[si-1][pi-1];
                }
                else
                {
                    dp[si][pi] = 0;
                }
            }
        }
        return dp[s.size()][p.size()];
    }
};