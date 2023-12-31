// https://leetcode.com/problems/search-in-rotated-sorted-array

class Solution(object):
    def search(self, nums, target, off=0):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 1:
            if nums[0] == target:
                return off
            return -1
        elif len(nums) == 2:
            if nums[1] == target:
                return off+1
            elif nums[0] == target:
                return off
            return -1
        elif len(nums) == 0:
            return -1

        left,mid,right = 0,len(nums)//2,len(nums)-1

        if target == nums[left]:
            return left+off
        elif target == nums[right]:
            return right+off
        elif target == nums[mid]:
            return mid+off

        if nums[left] < target < nums[mid]:
            return self.search(nums[left+1:mid], target, off+left+1)
        elif nums[mid] < target < nums[right]:
            return self.search(nums[mid+1:right], target, off+mid+1)

        if nums[right] < nums[mid]:
            return self.search(nums[mid+1:right], target, off+mid+1)
        elif nums[left] > nums[mid]:
            return self.search(nums[left+1:mid], target, off+left+1)

        return -1