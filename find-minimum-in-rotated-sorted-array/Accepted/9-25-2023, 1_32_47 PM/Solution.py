// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            if nums[0] > nums[1]:
                return nums[1]
            return nums[0]

        left,mid,right = 0,len(nums)//2,len(nums)-1
        if nums[left] < nums[mid] < nums[right]:
            return nums[0]
        elif nums[right] < nums[left] < nums[mid]:
            return self.findMin(nums[mid+1:right+1])
        elif nums[mid] < nums[right] < nums[left]:
            return self.findMin(nums[left:mid+1])
        