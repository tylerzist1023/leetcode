// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

class Solution:
    def removeDuplicates(self, nums: list) -> int:
        curnum = 0
        curnum_count = 0
        k = len(nums)
        for i in range(len(nums)):
            if nums[i] == curnum:
                curnum_count += 1
            else:
                curnum = nums[i]
                curnum_count = 1
            
            if curnum_count > 2:
                nums[i] = 10001
                k -= 1
        i = 0
        while i < k:
            print(nums)
            if nums[i] == 10001:
                for j in range(i+1, len(nums)):
                    nums[j-1] = nums[j]
                i -= 1
            i += 1
        return k