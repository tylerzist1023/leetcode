// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

class Solution:
    def removeDuplicates(self, nums: list) -> int:
        curnum = 0
        curnum_count = 0
        k = len(nums)
        for i,x in enumerate(nums):
            if x == curnum:
                curnum_count += 1
            else:
                curnum = x
                curnum_count = 1
            
            if curnum_count > 2:
                nums[i] = 10001
                k -= 1
        i = 0
        while i < k:
            if nums[i] == 10001:
                for j,y in enumerate(nums[i+1:]):
                    nums[i+j] = y
            else:
                i += 1
        return k