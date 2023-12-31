// https://leetcode.com/problems/missing-number

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = 0
        for x in nums:
            num ^= x
        for x in range(0,len(nums)+1):
            num ^= x
        return num