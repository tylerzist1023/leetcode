// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left,right = 0,0
        max_window = 0
        while left < len(prices) and right < len(prices):
            window = prices[right] - prices[left]
            if window > max_window:
                max_window = window
            if prices[right] < prices[left]:
                left = right
            right += 1
        return max_window