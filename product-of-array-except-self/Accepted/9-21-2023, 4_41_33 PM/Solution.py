// https://leetcode.com/problems/product-of-array-except-self

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        
        left = [1 for x in nums]
        right = left[:]
        for i in range(1,len(nums)):
            left[i] = nums[i-1]*left[i-1]
        for i in range(1,len(nums)):
            i_ = len(nums)-i-1
            right[i_] = nums[i_+1]*right[i_+1]
        products = [left[i]*right[i] for i in range(len(nums))]

        return products

        