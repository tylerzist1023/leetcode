// https://leetcode.com/problems/climbing-stairs

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [0]*(n+1)
        dp[0] = 1
        if len(dp) > 1:
            dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-2] + dp[i-1]

        return dp[n]