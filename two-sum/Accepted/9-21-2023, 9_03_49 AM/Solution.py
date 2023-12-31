// https://leetcode.com/problems/two-sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i,v in enumerate(nums):
            if target-v in nums:
                complement_index = nums.index(target-v)
                if i == complement_index:
                    if target-v in nums[complement_index+1:]:
                        complement_index = nums[complement_index+1:].index(target-v)
                else:
                    return [i, complement_index]