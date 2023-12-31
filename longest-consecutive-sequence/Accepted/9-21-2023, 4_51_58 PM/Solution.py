// https://leetcode.com/problems/longest-consecutive-sequence

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        best = 0
        for x in nums:
            if x-1 not in nums:
                y=x+1
                while y in nums:
                    y+=1
                if y-x > best:
                    best = y-x
        return best