// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

class Solution:
    def removeDuplicates(self, nums: list) -> int:
        curnum = 0
        curnum_count = 0
        k = len(nums)
        i = 0
        while i < k:
            if nums[i] == curnum:
                curnum_count += 1
            else:
                curnum = nums[i]
                curnum_count = 1
            
            if curnum_count > 2:
                for j,y in enumerate(nums[i+1:]):
                    nums[i+j] = y
                k -= 1
            else:
                i += 1
        return k