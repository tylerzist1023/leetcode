// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

class Solution:
    def removeDuplicates(self, nums: list) -> int:
        ptr = 2
        n = len(nums)
        if n <= 2:
            return n
        for i in range(2,n):
            if nums[i] != nums[ptr-2]:
                nums[ptr] = nums[i]
                ptr+=1
        return ptr