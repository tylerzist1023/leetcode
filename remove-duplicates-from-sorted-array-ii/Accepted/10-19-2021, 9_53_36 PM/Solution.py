// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

class Solution:
    def removeDuplicates(self, nums: list) -> int:
        j = 0
        for i in nums:
            if j < 2 or i > nums[j-2]:
                nums[j] = i
                j += 1
        return j