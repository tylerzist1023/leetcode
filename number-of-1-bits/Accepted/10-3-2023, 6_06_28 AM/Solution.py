// https://leetcode.com/problems/number-of-1-bits

class Solution(object):
    def hammingWeight(self, x):
        """
        :type n: int
        :rtype: int
        """
        x = (x & 0x55555555) + ((x >> 1) & 0x55555555)
        x = (x & 0x33333333) + ((x >> 2) & 0x33333333)
        x = (x & 0x0F0F0F0F) + ((x >> 4) & 0x0F0F0F0F)
        x = (x & 0x00FF00FF) + ((x >> 8) & 0x00FF00FF)
        x = (x & 0x0000FFFF) + ((x >> 16) & 0x0000FFFF)
        return x